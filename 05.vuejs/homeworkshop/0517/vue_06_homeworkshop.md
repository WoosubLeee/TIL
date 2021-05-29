# Workshop

created 훅을 이용하여 Vue 인스턴스가 생성될 때 자동으로 Todo list가 불러와지도록 한다.

```vue
created: function () {
  this.getTodos()
}
```

### CORS

![image-20210517221340850](vue_06_homeworkshop.assets/image-20210517221340850.png)

주어진 코드로 Todo list를 요청하면 위와 같은 에러가 발생한다. 이 에러는 'Access-Control-Allow-Origin' 헤더가 설정되지 않았기 때문이다.

이 문제는 django-cors-headers 라이브러리로 해결할 수 있다.

settings.py에

```python
INSTALLED_APPS = [
    ...
    'corsheaders',
    ...
]
MIDDLEWARE = [
    ...,
    'corsheaders.middleware.CorsMiddleware', # 'django.middleware.common.CommonMiddleware' 보다 위에 작성
    ...,
]
```

위의 코드를 추가하고, 

```python
CORS_ALLOWED_ORIGINS = [
    "https://example.com",
]
```

CORS_ALLOWED_ORIGINS에 위와 같이 허용할 URI+호스트+포트를 적으면 된다.

### Create Todo

```vue
// clients/src/todos/CreateTodo.vue

axios({
  ...
})
  ..then((res) => {
	...
	this.$router.push({ name: 'TodoList' })
  })
```

위 코드를 추가하여 post 요청을 보내고 난 후 TodoList가 렌더링되도록 한다.

### Update Todo

```vue
// clients/src/todos/TodoList.vue

axios({
  ...
})
  ..then((res) => {
	...
	todo.completed = !todo.completed
  })
```

위 코드를 추가하여 TodoList.vue 인스턴스의 data에도 수정(completed 여부) 내용이 반영되도록 한다.

### Delete Todo

```vue
// clients/src/todos/TodoList.vue

axios({
  ...
})
  ..then((res) => {
	...
	this.getTodos()
  })
```

위 코드를 추가하여 data의 todos를 다시 받아오도록 한다.

# Homework

- T
- F
- T