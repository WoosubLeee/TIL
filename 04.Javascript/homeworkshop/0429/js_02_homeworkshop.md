# Workshop

```javascript
function addTodo (event) {
  // 이벤트를 취소한다.
  event.preventDefault()

  // input element와 input element의 value 값을 저장한다.
  const input = document.querySelector('input')

  // li element를 생성 후 input element의 value 값을 데이터로 저장한다
  const li = document.createElement('li')
  li.innerText = input.value

  // ul 태그의 자식 태그로 위에서 생성한 li element를 넣는다.
  const ul = document.querySelector('ul')
  ul.append(li)

  // 삭제 버튼을 생성 후 li 태그의 자식 태그로 넣는다.
  const del = document.createElement('button')
  del.innerText = 'X'
  li.append(del)

  // 삭제 버튼을 클릭하면 해당 li element를 삭제한다
  del.addEventListener('click', function (event) {
    li.remove()
  })

  // li element를 클릭하면 취소선이 토글된다.
  li.addEventListener('click', function (event) {
    if (li.getAttribute('style')) {
      li.removeAttribute('style', 'text-decoration: line-through')
    } else {
      li.setAttribute('style', 'text-decoration: line-through')
    }
  })
}
```

# Homework

### 1.

- F : 재선언, 재할당 가능 여부도 다르다
- F : null은 object가 반환된다
- F : for of 를 통해 배열을 순회한다
- F : 자동 형변환으로 인해 타입이 같지 않아도 참을 반환할 수 있다
- T

### 2.

- map : 콜백 함수의 **반환 값을 요소**로 하는 **새로운 배열** 반환
- filter : 콜백 함수의 **반환 값이 참인 요소**로 하는 **새로운 배열** 반환
- find : 콜백 함수의 **반환 값이 참인 요소**를 반환
- every : **모든 요소에 대해** 콜백 함수가 참을 반환할 시 **참을 반환**
- some : 모든 요소 중 **하나라도** 콜백 함수가 참을 반환할 시 **참을 반환**
- reduce : 콜백 함수의 반환 값을 **하나의 값(acc)에 누적** 후 반환

### 3.

```javascript
nums.map((num) {
  return num ** 3
})
```