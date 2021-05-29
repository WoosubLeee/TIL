# Workshop

### 1

```
# articles/models.py

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

- `article = models.ForeignKey(Article, on_delete=models.CASCADE)` : 1:N 참조를 하기 위해 ForeignKey를 활용
  - `on_delete=models.CASCADE` : 참조한 모델(Article)이 삭제되면 Comment도 자동으로 삭제되도록 설정

### 2

![ezgif.com-gif-maker](django_10_homework.assets/ezgif.com-gif-maker.gif)

```
# articles/forms.py

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ('article',)
```

Comment를 달 수 있는 ModelForm을 만든다.

```
# articles/urls.py

urlpatterns = [
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
]
```

```
# articles/views.py

def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article_id = pk
            comment.save()
            return redirect('articles:detail', pk)
        article = Article.objects.get(pk=pk)
        context = {
            'comment_form': comment_form,
            'article': article,
        }
        return render(request, 'articles/detail.html', context)
    return redirect('articles:login')
```

- `comment = comment_form.save(commit=False)`

  comment가 참조할 article의 id를 지정해줘야 하는데 comment를 저장하기 전에는 지정할 수 없다.
  하지만 저장을 하려면 article의 id값이 필요하기 때문에 `commit=False`를 통해 DB까진 저장하지 않고 임시로 저장한 다음
  article_id값을 지정해 준 후 저장하게 된다.

```
# articles/templates/articles/detail.html

<form action="{% url 'articles:comments_create' article.pk %}" method="POST">
  {% csrf_token %}
  {{ comment_form }}
  <input type="submit">
</form>
```

### 3

```
# articles/views.py

@require_safe
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)
```

```
# articles/templates/articles/detail.html

<ul>
  {% for comment in comments %}
    <li>
      {{ comment }}
      <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="삭제">
      </form>
    </li>
  {% endfor %}
</ul>
```

### 4

### ![ezgif.com-gif-maker](django_10_homework.assets/ezgif.com-gif-maker-1616593056355.gif)

```
# articles/urls.py

urlpatterns = [
    path('<int:pk>/comments/<int:comment_pk>/delete', views.comments_delete, name='comments_delete'),
]
```

article pk값과 comment pk값 둘 다 넘겨줘야 한다.

```
# articles/views.py

@require_POST
def comments_delete(request, pk, comment_pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()
        return redirect('articles:detail', pk)
```

```
# articles/templates/articles/detail.html

<form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
  {% csrf_token %}
  <input type="submit" value="삭제">
</form>
```



# Homework

### 1. Lookup

- exact

  정확히 일치하는 값을 찾는다.

- iexact

  대소문자는 구분하지 않고 값을 찾는다.

- contains

  대소문자는 구분하며, 포함하고 있는 값을 찾는다.

### 2. 1:N 관계 설정

- CASCADE

  참조된 객체가 사라지면 참조하고 있는 객체도 삭제한다.

- PROTECT

  어떤 객체를 삭제할 때 이 객체를 참조하고 있는 다른 개체가 있으면 ProtectError가 발생하여 삭제를 막는다.

- SET_NULL

  참조된 객체가 사라지면 참조하고 있는 객체의 ForeignKey를 null로 바꾼다.

### 3. comment create view

commit=False

### 4. 1:N DB API

article.comment_set.all()