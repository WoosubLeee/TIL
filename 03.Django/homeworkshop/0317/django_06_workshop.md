# Workshop

### 1. Media file with HTML input

##### 1.

`multipart/form-data`

| 속성값                              | 설명                                                         |
| ----------------------------------- | ------------------------------------------------------------ |
| `application/x-www-form-urlencoded` | 기본값으로, 모든 문자들은 서버로 보내기 전에 인코딩됨을 명시함. |
| `multipart/form-data`               | 모든 문자를 인코딩하지 않음을 명시함. 이 방식은 `<form>` 요소가 파일이나 이미지를 서버로 전송할 때 주로 사용함. |



##### 2.

`video/*, .pdf`



# Homework

### 1. Compiled Bootstrap

`base.html` 상단에 `{% load static %}`을 넣어준 후
기존 CDN을 삽입하던 자리에

css는 `<link rel="stylesheet" href="{% static 'articles/css/bootstrap.css' %}">`
js는 `<link rel="stylesheet" href="{% static 'articles/js/bootstrap.bundle.js' %}">`

를 삽입해주면 된다.