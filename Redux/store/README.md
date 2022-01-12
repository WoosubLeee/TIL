# Redux store

## What is store?

The Redux **store** brings together the state, actions, and reducers that make up your app. The store has several responsibilities:

- Holds the current application state inside
- Allows access to the current state via `store.getState()`;
- Allows state to be updated via `store.dispatch(action)`;
- Registers listener callbacks via `store.subscribe(listener)`;
- Handles unregistering of listeners via the `unsubscribe` function returned by `store.subscribe(listener)`.

It's important to note that **you'll only have a single store in a Redux application**. When you want to split your data handling logic, you'll use reducer composition and create multiple reducers that can be combined together, instead of creating separate stores.



## Creating a store

The Redux core library has a `createStore` API that will create the store. Call `createStore` and pass in the root reducer.

```js
import { createStore } from 'redux'
import rootReducer from './reducer'

const store = createStore(rootReducer)

export default store
```

### Loading initial state

`createStore` can also accept a `preloadedState` value as its second argument. You could use this to add initial data when the store is created, such as values that were included in an HTML page sent from the server, or persisted in `localStorage` and read back when the user visits the page again, like this:

```js
const store = createStore(rootReducer, preloadedState)
```



## Dispatching actions

Every time we call `store.dispatch(action)`:

- The store calls `rootReducer(state, action)`
  - That root reducer may call other slice reducers inside of itself, like `todosReducer(state.todos, action)`
- The store saves the new state value inside
- The store calls all the listener subscription callbacks
- If a listener has access to the `store`, it can now call `store.getState()` to read the latest state value



## Configuring the store

`createStore` can also take one more argument, which is used to customize the store's abilities and give it new powers. Redux stores are customized using something called a **store enhancer**. A store enhancer is like a special version of `createStore` that adds another layer wrapping around the original Redux store. An enhanced store can then change how the store behaves, by supplying its own versions of the store's `dispatch`, `getState`, and `subscribe` functions instead of the originals.



## Middleware

Redux uses a special kind of addon called middleware to let us customize the `dispatch` function. Redux middleware provides a third-party extension point between dispatching an action, and the moment it reaches the reducer.

### Writing custom middleware

```js
const middleware = storeAPI => next => action => {
  // 하고 싶은 작업...
}
```

기본 구조는 위와 같다. 함수를 연달아 두 번 return 하는 함수이다. 이를 `function` 키워드를 사용하여 작성하면 다음과 같다.

```js
function middleware(storeAPI) {
  return function wrapDispatch(next) {
    return function handleAction(action) {
      // 하고 싶은 작업...
    };
  };
};
```

함수 인자들을 단계별로 살펴보면:

1. `storeAPI` : store 인스턴스이다. `dispatch()`, `getState()`, `subscribe()` 와 같은 함수들이 들어있다.
2. `next` : 다음 middleware로 action을 전달하는 함수이다. `next(action)` 과 같은 형태로 사용한다. 만약 다음 middleware가 없다면 reducer로 action을 전달한다. 만약 `next`를 호출하지 않는다면 action이 무시 처리되어 reducer로 전달되지 않는다.
3. `action` : 현재 처리하고 있는 액션 객체

middleware는 다음과 같은 구조로 작동한다. store에는 여러 개의 middleware를 등록할 수 있다. 새로운 action이 `dispatch`되면 첫번째로 등록한 middleware가 호출된다. 만약 middleware에서 `next(action)`을 호출하게 되면 다음 middleware로 action이 넘어간다. 그리고 만약 `store.dispatch()`를 호출하면 다른 action을 추가적으로 발생시킬 수도 있다.

<img src="https://i.imgur.com/fZs5yvY.png" alt="img" style="zoom: 33%;" />

```js
const loggerMiddleware = storeAPI => next => action => {
  console.log('dispatching', action)
  let result = next(action)
  console.log('next state', storeAPI.getState())
  return result
  // Any middleware can return any value, and the return value from the first middleware in the pipeline is actually returned when you call store.dispatch().
}
```

Whenever an action is dispatched:

- The first part of the `handleAction` function runs, and we print `'dispatching'`
- We pass the action to the `next` section, which may be another middleware or the real `store.dispatch`
- Eventually the reducers run and the state is updated, and the `next` function returns
- We can now call `storeAPI.getState()` and see what the new state is
- We finish by returning whatever `result` value came from the `next` middleware





## References

https://redux.js.org/tutorials/fundamentals/part-4-store

https://react.vlpt.us/redux-middleware/02-make-middleware.html (2. 미들웨어 만들어보고 이해하기)