# React hooks

## `useReducer`

```js
const [state, dispatch] = useReducer(reducer, initialArg, init);
```

- Parameters
  - reducer : `(state, action) => newState`
- Return : [state, dispatch]

`useReducer` is usually preferable to `useState` when you have complex state logic that involves multiple sub-values or when the next state depends on the previous one. `useReducer` also lets you optimize performance for components that trigger deep updates because you can pass `dispatch` down instead of callbacks.

Here's the example:

```js
const initialState = {count: 0};

function reducer(state, action) {
  switch (action.type) {
    case 'increment':
      return {count: state.count + 1};
    case 'decrement':
      return {count: state.count - 1};
    default:
      throw new Error();
  }
}

function Counter() {
  const [state, dispatch] = useReducer(reducer, initialState);
  return (
    <>
      Count: {state.count}
      <button onClick={() => dispatch({type: 'decrement'})}>-</button>
      <button onClick={() => dispatch({type: 'increment'})}>+</button>
    </>
  );
}
```

### Initializing state

1. To pass the initial state as a second argument:

   ```js
   const [state, dispatch] = useReducer(
     reducer,
     {count: initialCount}
   );
   ```

2. Lazy initialization

   To do this, you can pass an `init` function as the third argument. The initial state will be set to `init(initialArg)`.

   ```js
   function init(initialCount) {
     return {count: initialCount};
   }
   
   function reducer(state, action) {
     switch (action.type) {
       case 'increment':
         return {count: state.count + 1};
       case 'decrement':
         return {count: state.count - 1};
       case 'reset':
         return init(action.payload);
       default:
         throw new Error();
     }
   }
   
   function Counter({initialCount}) {
     const [state, dispatch] = useReducer(reducer, initialCount, init);
     return (
       <>
         Count: {state.count}
         <button
           onClick={() => dispatch({type: 'reset', payload: initialCount})}>
           Reset
         </button>
         <button onClick={() => dispatch({type: 'decrement'})}>-</button>
         <button onClick={() => dispatch({type: 'increment'})}>+</button>
       </>
     );
   }
   ```

### References

https://reactjs.org/docs/hooks-reference.html#usereducer