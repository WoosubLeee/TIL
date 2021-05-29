# Workshop

```python
# articles/views.py

@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)

        if article.like_users.filter(pk=request.user.pk).exists():
        # if request.user in article.like_users.all():
            # 좋아요 취소
            article.like_users.remove(request.user)
            liked = False
        else:
            # 좋아요 누름
            article.like_users.add(request.user)
            liked = True
        like_status = {
            'liked': liked,
            'like_count': article.like_users.count()
        }
        return JsonResponse(like_status)
    return redirect('accounts:login')
```

```javascript
# articles/templates/articles/index.html

<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
  const likeForm = document.querySelector("#like-form")
  likeForm.addEventListener('submit', function (event) {
    event.preventDefault()
    const articleId = event.target.dataset.articleId
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/articles/${articleId}/likes/`,
      headers: {'X-CSRFToken': csrftoken }
    })
    .then (response => {
      const likeBtn = document.querySelector("#like-btn")
      const liked = response.data.liked
      if (liked) {
        likeBtn.innerText = "좋아요 취소"
      } else {
        likeBtn.innerText = "좋아요"
      }
      const likeCnt = document.querySelector("#like-count")
      const likeCntRes = response.data.like_count
      likeCnt.innerText = likeCntRes
    })
  })
</script>
```

# Homework

#### 1.

- T
- T
- T

#### 2.

1. - Call Stack : `console.log('Hello SSAFY!')` 실행

   - Web API :

   - Task Queue :

     

2. - Call Stack : `setTimeout` 실행 - 3초간 대기

   - Web API :

   - Task Queue:

     

3. - Call Stack :

   - Web API : `setTimeout`이 대기하기 위해 들어옴

   - Task Queue :

     

4. - Call Stack : `console.log('Bye')` 실행

   - Web API : `setTimeout`

   - Task Queue :

     

5. - Call Stack :

   - Web API :

   - Task Queue : `setTimeout`이 3초 대기를 끝내고 실행을 위해 들어옴

     

6. - Call Stack : `setTimeout` - Event Loop가 실행시킨다
   - Web API :
   - Task Queue :

#### 3.

- Concurrency : 여러 작업을 동시에 수행한다. 한 작업을 다 끝내고 다음 작업을 시작하는게 아닌 동시에 다수의 작업을 진행할 수 있다.(엄밀히 말하면 '동시'에 수행하는 것은 아니다. ex - 작업1을 조금 수행, 작업2를 조금 수행, 작업1 마무리, 작업2 마무리)
- Parallelism : 작업을 다수의 sub-task로 파편화시켜 동시에 수행하는 것이다.