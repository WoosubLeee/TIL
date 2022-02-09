# `useRef`

<img src="https://drek4537l1klr.cloudfront.net/larsen3/v-3/Figures/06_img_0004.png" alt="img" style="zoom: 67%;" />

## Why use `useRef`

### 1. DOM에 접근한다

JS에서 특정 DOM을 선택해야 할 때, `getElementById` 혹은 `querySelector`와 같은 함수를 사용한다. 하지만, React에선 이 기능을 대체할 수 있는 `useRef` 훅을 제공한다. 왜 기존에 vanilla JS에서 사용하던 친숙한 `querySelector`를 지양하고 이를 대체하는 `useRef`를 사용할까?

React에서 `querySelector`를 사용하게되면, 실제 Real DOM의 요소를 가져오게 된다. 하지만 React는 Virtual DOM을 통해 Real DOM을 그리기 때문에, React가 제어하고있는 Virtual DOM 안에 있는 요소가 더 신뢰할만하다. DOM API로 Real DOM에 있는 node 를 담았지만, 이게 현재 Virtual DOM을 통해 Real DOM에 존재하는 node 인지 아닌지 확신할 수 없기 때문에 `useRef`를 사용한다.

또한, React에서 가장 중요한 개념 중 하나가 state다. React 내부에서 데이터는 컴포넌트 내의 state로 조작된다. 만약 이러한 React 시스템을 벗어나 DOM을 직접적으로 건드리게되면 이 내용들은 React가 제어하는 영역에서 벗어나게 되고, React에서 제공하는 이점들을 사용할 수 없게 된다.

```jsx
import { useRef } from "react";

const inputRef = useRef();

const foo = () => {
  return (
    <div>
      <input ref={inputRef} />
      <button onClick={() => inputRef.current.focus()}>
        이 버튼을 누르면 input에 focus 됩니다.
      </button>
    </div>
  );
};
```

### 2. 무분별한 re-rendering을 방지한다.

`useRef` 함수는 `current` 속성을 가지고 있는 객체를 반환하는데, 인자로 넘어온 초기값을 `current` 속성에 할당합니다. 이 `current` 속성은:

- 값을 변경해도 상태를 변경할 때 처럼 React 컴포넌트를 re-render 시키지 않고,
- React 컴포넌트가 re-render 될 때도 재선언, 유실되지 않는다.



## References

https://mnxmnz.github.io/react/what-is-use-ref/ ([React] useRef는 처음이라 :: 개념부터 활용 예시까지)

https://hwani.dev/useRef/ (리액트 useRef)