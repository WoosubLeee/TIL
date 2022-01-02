# `useCallback`

Returns a memoized callback. 함수를 memoization하기 위해 사용하는 hook이다.

```jsx
const memoizedCallback = useCallback(fn, deps)
```

첫번째 인자로 넘어온 함수(`fn`)를, 두번째 인자로 넘어온 배열(`deps`) 내의 값이 변경될 때까지 memoize하고 재사용할 수 있게 해준다. Component 내에 선언된 함수는 Component가 render 될 때마다 새로 생성된다. 하지만 `useCallback`을 사용하면, 해당 component가 re-render 되더라도 기존 함수를 계속 반환한다.



## Why use `useCallback`?

사실 memoize함으로써 얻는 성능의 이득은 유의미하게 크지 않을 확률이 높다. 그렇다면 왜 사용하는 것일까?

### JavaScript 함수 동등성

```js
> const add1 = () => x + y;
undefined
> const add2 = () => x + y;
undefined
> add1 === add2
false
```

JS에서 객체는 메모리 주소를 이용하여 비교하기 때문에 위와 같이 같은 내용의 함수더라도 동일하지 않다고 인식하게 된다.

### `useCallback`을 사용하지 않은 경우

```jsx
import React, { useState, useEffect } from "react";

function Profile({ userId }) {
  const [user, setUser] = useState(null);

  const fetchUser = () =>
    fetch(`https://your-api.com/users/${userId}`)
      .then((response) => response.json())
      .then(({ user }) => user);

  useEffect(() => {
    fetchUser().then((user) => setUser(user));
  }, [fetchUser]);

  // ...
}
```

위와 같은 코드는 무한 루프에 빠지게 된다.

(1) (`useEffect()` -> `fetchUser()` -> `setUser()` -> re-render -> `fetchUser()` 재생성) -> (2) (`useEffect()` -> ...

### `useCallback`을 사용한 경우

```jsx
import React, { useState, useEffect } from "react";

function Profile({ userId }) {
  const [user, setUser] = useState(null);

  const fetchUser = useCallback(
    () =>
      fetch(`https://your-api.com/users/${userId}`)
        .then((response) => response.json())
        .then(({ user }) => user),
    [userId]
  );

  useEffect(() => {
    fetchUser().then((user) => setUser(user));
  }, [fetchUser]);

  // ...
}
```

`useEffect()` -> `fetchUser()` -> `setUser()` -> re-render

re-render 되더라도 `userId`는 변경되지 않았기에 `fetchUser()` 함수는 re-render 되기 이전 함수와 동일하다(메모리 주소가 같다). 그 결과 무한 루프에 빠지지 않고 정상적으로 작동한다.



## References

https://www.daleseo.com/react-hooks-use-callback/ (React Hooks: useCallback 사용법)