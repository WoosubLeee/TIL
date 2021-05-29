# Workshop

```html
<body>
  <form action="">
    <input type="text">
    <button>Add</button>
  </form>
  <ul></ul>
    
  <script>
    const todoForm = document.querySelector('form')
    todoForm.addEventListener('submit', function (event) {
      event.preventDefault()
      const todo = document.createElement('li')
      const input = document.querySelector('input')
      todo.innerText = input.value
      const todoList = document.querySelector('ul')
      todoList.append(todo)

      event.target.reset()
    })
  </script>
</body>
```

- `const todoForm = document.querySelector('form')` : form 요소를 선택하여 초기화
- `todoForm.addEventListener('submit', function (event)` : todoForm 요소에 submit event가 발생하면 function을 수행함
- `event.preventDefault()` : submit event의 기본 동작(form 내용 제출)을 수행하지 않도록 함
- `const todo = document.createElement('li')` : input 내용을 담을 li 태그 초기화
- `todo.innerText = input.value` : todo에 담을 내용을 저장
- `todoList.append(todo)` : todoList(ul 태그)의 자식 노드로 todo를 추가
- `event.target.reset()` : event 발생 시 target을 reset한다



# Homework

### 1.

- T
- T
- T
- F : appendchild도 있다

### 2.

- click : 포인터 장치로 클릭했을 때
- mouseover : 포인터 장치가 element 위로 이동했을 때
- mouseout : 포인터 장치가 element 위에서 밖에로 이동했을 때
- keydown : 키를 눌렀을 때
- keyup : 키를 뗐을 때
- load : 파일이 성공적으로 읽혔을 때
- scroll : 화면을 scroll할 때
- change : input, select, textarea 요소의 내용에 변화가 일어난 후 focus가 옮겨졌을 때
- input : input, select, textarea 요소의 내용에 변화가 일어났을 때

### 3.

(a) : querySelector

(b) : addEventListener

(c) : 'click'

