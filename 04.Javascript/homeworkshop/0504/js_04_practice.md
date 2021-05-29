# Practice

```python
# accounts/views.py

@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        you = get_object_or_404(get_user_model(), pk=user_pk)
        # 나 자신은 팔로우 할 수 없다
        if you != request.user:
            if you.followers.filter(pk=request.user.pk).exists():
            # if request.user in you.followers.all():
                you.followers.remove(request.user)
                followed = False
            else:
                you.followers.add(request.user)
                followed = True
            follow_status = {
                'followed': followed,
                'follower_count': you.followers.count()
            }
        return JsonResponse(follow_status)
    return redirect('accounts:login')
```

```python
follow_status = {
    'followed': followed,
    'follower_count': you.followers.count()
}
```

와 같이 follow를 하고 있는지 여부와, 해당 계정의 follower 수를 담아 response로 전달한다.

```html
# accounts/templates/accounts/profile.html

<div>
  팔로잉 : {{ followings|length }} / 팔로워 : 
  <span id="follower-cnt">{{ followers|length }}</span>
</div>
{% if request.user != person %}
  <div>
    <form id="follow-form" data-user-id="{{ person.pk }}">
      {% csrf_token %}
      {% if request.user in followers %}
        <button id="follow-btn" style="background-color: white"}>Unfollow</button>
      {% else %}
        <button id="follow-btn" style="background-color: darkturquoise">Follow</button>
      {% endif %}
    </form>
  </div>
{% endif %}
```

script에서 이용할 태그들에 id나 class를 설정해준다.

- `data-user-id="{{ person.pk }}"` : JS에서 이용할 수 있도록 data를 저장해 준다

```javascript
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
  const followForm = document.querySelector('#follow-form')
  followForm.addEventListener('submit', function (event) {
    event.preventDefault()
    const userId = event.target.dataset.userId
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    axios({
        method: 'post',
        url: `http://127.0.0.1:8000/accounts/${userId}/follow/`,
        headers: {'X-CSRFToken': csrftoken }
    })
    .then (response => {
      const followBtn = document.querySelector('#follow-btn')
      const followed = response.data.followed
      const followerCntRes = response.data.follower_count
      if (followed) {
        followBtn.innerText = "Unfollow"
        followBtn.setAttribute("style", "background-color: white")
      } else {
        followBtn.innerText = "Follow"
        followBtn.setAttribute("style", "background-color: darkturquoise")
      }
      const followerCnt = document.querySelector("#follower-cnt")
      followerCnt.innerText = followerCntRes
    })
  })
</script>
```

- `followForm.addEventListener('submit', function (event) {` : followForm에 submit 이벤트가 발생했을 경우 콜백 함수를 실행한다.

- `const userId = event.target.dataset.userId` : data- 속성을 사용하여 저장한 userId 값을 초기화한다.

- ```javascript
  axios({
    method: 'post',
    url: `http://127.0.0.1:8000/accounts/${userId}/follow/`,
    headers: {'X-CSRFToken': csrftoken }
  })
  ```

  promise 사용을 위해 axios를 활용

- ```javascript
  const followed = response.data.followed
  const followerCntRes = response.data.follower_count
  ```

  views.py에서 넘어온 데이터를 초기화한다.