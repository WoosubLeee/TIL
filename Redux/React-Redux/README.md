# React-Redux

React-Redux includes its own custom hooks, which you can use in your own components. The React-Redux hooks give your React component the ability to talk to the Redux store by reading state and dispatching actions.



## `useSelector`

The `useSelector` hook lets your React components read data from the Redux store. `useSelector` accepts a single function, which we call a **selector** function. A **selector** is a function that takes the entire Redux store state as its argument, reads some value from the state, and returns that result.

For example, if our state has an array of todo items as `state.todos`, we can write a small selector function that returns that todos array:

```js
const selectTodos = state => state.todos
```

`useSelector` **automatically subscribes to the Redux store** for us. That way, any time an action is dispatched, it will call its selector function again right away. If the value returned by the selector changes from the last time it ran, `useSelector` will force our component to re-render with the new data.

However, there's a very important thing to remember here. **`useSelector` compares its results using strict `===` reference comparisons, so the component will re-render any time the selector result is a new reference!** This means that if you create a new reference in your selector and return it, your component could re-render *every* time an action has been dispatched, even if the data really isn't different.

For example, passing this selector to `useSelector` will cause the component to *always* re-render, because `array.map()` always returns a new array reference:

```js
// Bad: always returning a new reference
const selectTodoDescriptions = state => {
  // This creates a new array reference!
  return state.todos.map(todo => todo.text)
}
```

It's recommend prefixing selector function names with the word `select` combined with a description of the value being selected.

### Multiple selectors

**We can call `useSelector` multiple times within one component**. In fact, this is actually a good idea - **each call to `useSelector` should always return the smallest amount of state possible**.

### Selecting Data in List Items by ID

When selecting an array object, there's a potential performance problem.

- Changing one todo object means creating copies of both the todo and the `state.todos` array, and each copy is a new reference in memory
- When `useSelector` sees a new reference as its result, it forces its component to re-render
- So, any time *one* todo object is updated (like clicking it to toggle its completed status), the whole `<TodoList>` parent component will re-render
- Then, because React re-renders all child components recursively by default, it also means that *all* of the `<TodoListItem>` components will re-render, even though most of them didn't actually change at all!

To prevent this, you can pass list IDs from the store as props, then each list item can use that ID to find the right item object it needs.

```jsx
// TodoList.js

const selectTodoIds = state => state.todos.map(todo => todo.id)

const TodoList = () => {
  const todoIds = useSelector(selectTodoIds)

  const renderedListItems = todoIds.map(todoId => {
    return <TodoListItem key={todoId} id={todoId} />
  })

  return <ul className="todo-list">{renderedListItems}</ul>
}
```

```jsx
// TodoListItem.js

const selectTodoById = (state, todoId) => {
  return state.todos.find(todo => todo.id === todoId)
}

// Destructure `props.id`, since we only need the ID value
const TodoListItem = ({ id }) => {
  // Call our `selectTodoById` with the state _and_ the ID value
  const todo = useSelector(state => selectTodoById(state, id))
  const { text, completed, color } = todo

  const dispatch = useDispatch()

  const handleCompletedChanged = () => {
    dispatch({ type: 'todos/todoToggled', payload: todo.id })
  }

  // omit other change handlers
  // omit other list item rendering logic and contents

  return (
    <li>
      <div className="view">{/* omit other rendering output */}</div>
    </li>
  )
}
```

But there's also a problem with this, though. In this case, the *contents* of the IDs array should be the same if we're toggling a todo, because we're still showing the same todo items - we haven't added or deleted any. But, the array *containing* those IDs is a new reference, so `<TodoList>` will re-render when it really doesn't need to.

One possible solution to this is to change how `useSelector` compares its values to see if they've changed. `useSelector` can take a comparison function as its second argument. A comparison function is called with the old and new values, and returns `true` if they're considered the same. If they're the same, `useSelector` won't make the component re-render.

React-Redux has a `shallowEqual` comparison function we can use to check if the items *inside* the array are still the same. Let's try that:

```jsx
// TodoList.js

const selectTodoIds = state => state.todos.map(todo => todo.id)

const TodoList = () => {
  const todoIds = useSelector(selectTodoIds, shallowEqual)

  const renderedListItems = todoIds.map(todoId => {
    return <TodoListItem key={todoId} id={todoId} />
  })

  return <ul className="todo-list">{renderedListItems}</ul>
}
```



## `useDispatch`

 `useDispatch` hook gives us the store's `dispatch` method as its result. So, we can call `const dispatch = useDispatch()` in any component that needs to dispatch actions, and then call `dispatch(someAction)` as needed.



## `Provider`

To tell React-Redux what store we want to use in our components, we render a **`<Provider>` component around our entire `<App>`, and passing the Redux store as a prop to `<Provider>`**.

```jsx
ReactDOM.render(
  <React.StrictMode>
    <Provider store={store}>
      <App />
    </Provider>
  </React.StrictMode>,
  document.getElementById('root')
)
```



## References

https://redux.js.org/tutorials/fundamentals/part-5-ui-react

