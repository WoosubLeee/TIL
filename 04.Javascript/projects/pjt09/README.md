# Project 09

> 20210507에 진행한 프로젝트입니다.

### 리뷰 좋아요 기능

```python
# community/views.py

@require_POST
def like(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        user = request.user

        if review.like_users.filter(pk=user.pk).exists():
            review.like_users.remove(user)
            liked = False
        else:
            review.like_users.add(user)
            liked = True
        like_status = {
            'liked': liked,
            'count': review.like_users.count()
        }
        return JsonResponse(like_status)
    return HttpResponse(status=401)
```

```html
# community/templates/community/detail.html

<form id="like-form" data-review-id="{{ review.pk }}">
  {% csrf_token %}
  {% if request.user in review.like_users.all %}
    <button class="btn btn-link">
      <i id="like-icon" class="fas fa-heart fa-lg" style="color:crimson;"></i>
    </button>
  {% else %}
    <button class="btn btn-link">
      <i id="like-icon" class="fas fa-heart fa-lg" style="color:black;"></i>
    </button>
  {% endif %}
</form>
<p id="like-count">{{ review.like_users.all|length }}명이 좋아합니다</p>
```

```javascript
# community/templates/community/detail.html

<script>
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
  const form = document.querySelector('#like-form')
  form.addEventListener('submit', function (event) {
    event.preventDefault()
    const reviewId = event.target.dataset.reviewId
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/community/${reviewId}/like/`,
      headers: {'X-CSRFToken': csrftoken }
    })
    .then (response => {
      const liked = response.data.liked
      const count = response.data.count
      const likeIcon = document.querySelector('#like-icon')
      const likeCnt = document.querySelector('#like-count')
      if (liked) {
        likeIcon.setAttribute("style", "color:crimson;")
      } else {
        likeIcon.setAttribute("style", "color:black;")e
      }
      likeCnt.innerText = `${count}명이 좋아합니다`
    })
    .catch (error => {
      if (error.response.status === 401) {
        alert('로그인 후 이용해주세요')
        location.href = 'http://127.0.0.1:8000/accounts/login/'
      }
    })
  })
</script>
```

### 유저 팔로우 기능

```python
# accounts/views.py

@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=user_pk)
        user = request.user
        if person != user:
            if person.followers.filter(pk=user.pk).exists():
                person.followers.remove(user)
                followed = False
            else:
                person.followers.add(user)
                followed = True
            follow_status = {
                'followed': followed,
                'count': person.followers.count()
            }
            return JsonResponse(follow_status)
    return HttpResponse(status=401)
```

```html
# accounts/templates/accounts/_follow.html

<p class="lead">
  팔로잉 : {{ followings|length }} / 팔로워 : <span id="follower-count">{{ followers|length }}</span>
</p>

<form id="follow-form" data-person-id="{{ person.pk }}">
  {% csrf_token %}
  {% if request.user in followers %}
    <button id="follow-button" class="btn-secondary btn-lg" role="button">Unfollow</button>
  {% else %}
    <button id="follow-button" class="btn-primary btn-lg" role="button">Follow</button>
  {% endif %}
</form>
```

```javascript
# accounts/templates/accounts/_follow.html

<script>
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
  const form = document.querySelector('#follow-form')
  form.addEventListener('submit', function (event) {
    event.preventDefault()
    const personId = event.target.dataset.personId
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/accounts/follow/${personId}/`,
      headers: {'X-CSRFToken': csrftoken }
    })
    .then (response => {
      const followed = response.data.followed
      const count = response.data.count
      const followBtn = document.querySelector('#follow-button')
      const followerCnt = document.querySelector('#follower-count')
      if (followed) {
        followBtn.setAttribute('class', 'btn-primary btn-lg')
        followBtn.innerText = 'Unfollow'
      } else {
        followBtn.setAttribute('class', 'btn-secondary btn-lg')
        followBtn.innerText = 'Follow'
      }
      followerCnt.innerText = count
    })
    .catch (error => {
      if (error.response.status === 401) {
        alert('로그인 후 이용해주세요')
        location.href = 'http://127.0.0.1:8000/accounts/login/'
      }
    })
  })
</script>
```

### 영화 추천 알고리즘

```python
# movies/views.py

@require_GET
def recommended(request):
    movies = Movie.objects.all()
    movies = sample(list(movies), 10)
    context = {
        'movies': movies,
    }
    return render(request, 'movies/recommended.html', context)
```

```html
# movies/templates/movies/recommended.html

<div class="row row-cols-1 row-cols-md-5 g-4">
  {% for movie in movies %}
    <div class="col">
      <div class="card h-100">
        <img src="{{ movie.poster_path }}" class="card-img-top">
        <a href="{% url 'movies:detail' movie.pk %}" class="text-decoration-none text-dark">
          <div class="card-body">
            <h5 class="card-title">{{ movie.title }}</h5>

            <p>
              {% for genre in movie.genres.all %}
                <span>{{ genre.name }}</span>
              {% endfor %}
            </p>

            {% if movie.overview %}
              <p class="card-text">{{ movie.overview|truncatechars:60 }}</p>
            {% else %}
              <p class="card-text">줄거리 없음</p>
            {% endif %}
          </div>
        </a>
      </div>
    </div>
  {% endfor %}
</div>
```

### Points

- 영화 추천 알고리즘을 javascript를 사용해 구현해보려 하였으나 쉽지 않았다. 기초부터 차근히 공부해야 할 것 같다.