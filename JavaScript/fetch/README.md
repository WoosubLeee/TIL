# `fetch()`

`fetch()` 함수는 HTTP 요청 전송 기능을 제공하는 web API 이다.

## How to use

`fetch()` 함수는 첫번째 인자로 URL, 두번째 인자로 options 객체를 받고, `Promise` 객체를 반환한다. 호출이 성공한 경우 `response` 객체를 resolve하고, 실패한 경우 `error` 객체를 reject한다.

```js
fetch(url, options)
  .then((response) => console.log("response:", response))
  .catch((error) => console.log("error:", error));
```

`options` 객체에는 `method`(HTTP 방식), `headers`(HTTP 요청 header), `body`(HTTP 요청 전문) 등을 설정해줄 수 있다. `response` 객체로부터는 `status`(HTTP 응답 상태), `headers`(HTTP 응답 헤더), `body`(HTTP 응답 전문) 등을 읽어올 수 있다.

### `GET` method

`fetch()` 함수는 `GET` 방식이 default로 `options` 인자가 따로 필요없다.

```js
fetch(API_URL)
  .then((response) => response.json())
  .then((data) => console.log(data));
```

### `POST` method

`method` 옵션을 `POST`로 지정해주고, 데이터 형식에 맞는 `Content-Type`을 설정해준다. 아래에서는 일반적으로 많이 사용되는 JSON을 지정해주었다.

```js
fetch(API_URL, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    title: 'Test',
    body: 'I am testing!'',
    userId: 1,
  }),
})
  .then((response) => response.json())
  .then((data) => console.log(data))
```

### `PUT`, `DELETE` method

`method`를 각각 `PUT`, `DELETE`로 변경하는 것을 제외하고는 `POST` 방식과 거의 흡사하다.



## References

https://www.daleseo.com/js-window-fetch/ ([자바스크립트] fetch() 함수로 원격 API 호출하기)

https://velog.io/@eunjin/JavaScript-fetch-%ED%95%A8%EC%88%98-%EC%93%B0%EB%8A%94-%EB%B2%95-fetch-%ED%95%A8%EC%88%98%EB%A1%9C-HTTP-%EC%9A%94%EC%B2%AD%ED%95%98%EB%8A%94-%EB%B2%95 ([JavaScript] fetch 함수 쓰는 법, fetch 함수로 HTTP 요청하는 법)