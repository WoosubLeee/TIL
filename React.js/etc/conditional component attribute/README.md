# React conditional component attribute

React에서 HTML 요소에 conditional attribute를 추가하려 할 때 일반적인 방법은 다음과 같다.

```jsx
<div className={condition && "attribute"} />
```

condition을 만족하면 attribute가 추가되고 아니면 아무것도 입력되지 않는다. value가 없지만 React에서는 이를 오류로 판단하지 않고 잘 render한다.

하지만 react-router를 사용하면서 다음과 같은 문제가 발생했다.

```jsx
<Route path="auth" element={isLogin && <Navigate to="/" replace={true} />}>
```

로그인이 되어있으면 `element`에 `Navigate` 속성을 입력하여 로그인, 회원가입 페이지를 벗어나도록 하는 코드이다. 문제는, 로그인이 되어있지 않은 경우 `element` 속성을 인식 자체를 하면 안되는데, 빈 값을 줘도 `element`란 속성이 있는 것으로 인식되어 오류를 일으키는 것이다.

```jsx
<Route path="auth" {isLogin && element={<Navigate to="/" replace={true} />}>
```

위와 같은 방법도 시도해봤는데 `isLogin`부터 인식하지 못한다.

해결책은 다음과 같다:

```jsx
const authElement = isLogin && { element: <Navigate to="/" replace={true} /> }

return (
  <Route path="auth" {...authElement}>
)
```

따로 변수를 생성하고 이를 태그 내에서 destructure한다.



## References

[How do I conditionally add attributes to React components?](https://stackoverflow.com/questions/31163693/how-do-i-conditionally-add-attributes-to-react-components)

