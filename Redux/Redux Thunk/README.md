# Redux Thunk

> Redux Fundamentals tutorial, Part 6 를 정리한 내용이다.

## Redux middleware and Side effects

Most real applications need to work with data from a server, by making HTTP API calls to fetch and save items. But a Redux store doesn't know anything about async logic. Any asynchronicity has to happen outside the store.

Earlier, we said that Redux reducers must never contain "side effects". **A "side effect" is any change to state or behavior that can be seen outside of returning a value from a function**.

**Redux middleware were designed to enable writing logic that has side effects**. A Redux middleware can do anything when it sees a dispatched action: log something, modify the action, delay the action, make an async call, and more. 

Also, since middleware form a pipeline around the real `store.dispatch` function, this also means that we could actually pass something that *isn't* a plain action object to `dispatch`, as long as a middleware intercepts that value and doesn't let it reach the reducers.

Middleware also have access to `dispatch` and `getState`. That means you could write some async logic in a middleware, and still have the ability to interact with the Redux store by dispatching actions.

### Using middleware to enable async logic

Middleware를 사용하여 API 요청 로직을 다음과 같이 구현할 수 있다.

```js
import { client } from '../api/client'

const fetchTodosMiddleware = storeAPI => next => action => {
  if (action.type === 'todos/fetchTodos') {
    // Make an API call to fetch todos from the server
    client.get('todos').then(todos => {
      // Dispatch an action with the todos we received
      storeAPI.dispatch({ type: 'todos/todosLoaded', payload: todos })
    })
  }

  return next(action)
}
```

### Writing an async function middleware

We could pass a function to `dispatch`, instead of an action object. We could have our middleware check to see if the "action" is actually a function instead, and if it's a function, call the function right away. That would let us write async logic in separate functions, outside of the middleware definition.

```js
const asyncFunctionMiddleware = storeAPI => next => action => {
  // If the "action" is actually a function instead...
  if (typeof action === 'function') {
    // then call the function and pass `dispatch` and `getState` as arguments
    return action(storeAPI.dispatch, storeAPI.getState)
  }

  // Otherwise, it's a normal action - send it onwards
  return next(action)
}
```

Then we could use that middleware like this.

```js
const middlewareEnhancer = applyMiddleware(asyncFunctionMiddleware)
const store = createStore(rootReducer, middlewareEnhancer)

// Write a function that has `dispatch` and `getState` as arguments
const fetchSomeData = (dispatch, getState) => {
  // Make an async HTTP request
  client.get('todos').then(todos => {
    // Dispatch an action with the todos we received
    dispatch({ type: 'todos/todosLoaded', payload: todos })
    // Check the updated store state after dispatching
    const allTodos = getState().todos
    console.log('Number of todos after loading: ', allTodos.length)
  })
}

// Pass the _function_ we wrote to `dispatch`
store.dispatch(fetchSomeData)
// logs: 'Number of todos after loading: ###'
```



## Redux async data flow

![Redux async data flow diagram](README.assets/ReduxAsyncDataFlowDiagram-d97ff38a0f4da0f327163170ccc13e80.gif)



## Using the Redux Thunk middleware

As it turns out, Redux already has an official version of that "async function middleware", called the **Redux "Thunk" middleware**. The thunk middleware allows us to write functions that get `dispatch` and `getState` as arguments. The thunk functions can have any async logic we want inside, and that logic can dispatch actions and read the store state as needed.

### Configuring the store

```bash
$ npm install redux-thunk
```

```js
import { createStore, applyMiddleware } from 'redux'
import thunkMiddleware from 'redux-thunk'
import { composeWithDevTools } from 'redux-devtools-extension'
import rootReducer from './reducer'

const composedEnhancer = composeWithDevTools(applyMiddleware(thunkMiddleware))

// The store now has the ability to accept thunk functions in `dispatch`
const store = createStore(rootReducer, composedEnhancer)
export default store
```

### Fetching data from a server

```js
import { client } from '../../api/client'

const initialState = []

export default function todosReducer(state = initialState, action) {
  switch (action.type) {
    // omit other reducer cases
    case 'todos/todosLoaded': {
      // Replace the existing state entirely by returning the new value
      return action.payload
    }
    default:
      return state
  }
}

// Thunk function
export async function fetchTodos(dispatch, getState) {
  const response = await client.get('/fakeApi/todos')
  dispatch({ type: 'todos/todosLoaded', payload: response.todos })
}
```

```jsx
import store from './store'
import { fetchTodos } from './features/todos/todosSlice'

store.dispatch(fetchTodos)

ReactDOM.render(
  <React.StrictMode>
    <Provider store={store}>
      <App />
    </Provider>
  </React.StrictMode>,
  document.getElementById('root')
)
```

### Saving data

We also need to update the server whenever we try to create a new todo item. Instead of dispatching the `'todos/todoAdded'` action right away, we should make an API call to the server with the initial data, wait for the server to send back a copy of the newly saved todo item, and *then* dispatch an action with that todo item.

However, if we start trying to write this logic as a thunk function, we're going to run into a problem:

```js
async function saveNewTodo(dispatch, getState) {
  // ❌ We need to have the text of the new todo, but where is it coming from?
  const initialTodo = { text }
  const response = await client.post('/fakeApi/todos', { todo: initialTodo })
  dispatch({ type: 'todos/todoAdded', payload: response.todo })
}
```

We need a way to write one function that accepts `text` as its parameter, but then creates the actual thunk function so that it can use the `text` value to make the API call. Our outer function should then return the thunk function so that we can pass to `dispatch` in our component.

```js
// Write a synchronous outer function that receives the `text` parameter:
export function saveNewTodo(text) {
  // And then creates and returns the async thunk function:
  return async function saveNewTodoThunk(dispatch, getState) {
    // ✅ Now we can use the text value and send it to the server
    const initialTodo = { text }
    const response = await client.post('/fakeApi/todos', { todo: initialTodo })
    dispatch({ type: 'todos/todoAdded', payload: response.todo })
  }
}
```

```jsx
const handleKeyDown = e => {
  // If the user pressed the Enter key:
  const trimmedText = text.trim()
  if (e.which === 13 && trimmedText) {
    // Create the thunk function and immediately dispatch it
    dispatch(saveNewTodo(trimmedText))
    setText('')
  }
}
```



## References

https://redux.js.org/tutorials/fundamentals/part-6-async-logic

