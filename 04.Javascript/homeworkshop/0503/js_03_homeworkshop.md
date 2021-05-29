# Workshop

```javascript
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
  const API_URI = 'https://dog.ceo/api/breeds/image/random'
  
  function getDog () {
    // axios를 사용하여 API_URI로 GET 요청을 보낸다.
    const myPromise = axios.get(API_URI)

    // .then 메서드를 통해 요청이 성공적인 경우의 콜백함수를 정의한다.
    myPromise
      .then((response) => {
        res = response
    // 응답객체의 데이터에서 이미지에 대한 리소스를 img 요소의 src 속성으로 할당한다.
        const img = document.querySelector('img')
        img.setAttribute('src', res.data.message)
      })
  }

  const button = document.querySelector('button')
  button.addEventListener('click', getDog)
</script>
```

# Homework

#### 1.

- T
- F : Task Queue에서 대기한다
- T
- T

#### 2.

- 동기 : 직렬식 - 요청을 보내고 응답을 받아야지만 다음 동작이 이루어진다.
- 비동기 : 병렬식 - 요청을 보내고 응답이 오지 않았더라도 다음 동작을 수행한다.

#### 3.

(a) : get

(b) : then

(c) : response