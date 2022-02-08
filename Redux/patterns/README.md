# Redux patterns

Real world Redux applications use some additional patterns on top of basics. It's important to note that **none of these patterns are required to use Redux!** But, there are very good reasons why each of these patterns exists, and you'll see some or all of them in almost every Redux codebase.



## Action creators

An **action creator** is a function that creates and returns an action object. We typically use these so we don't have to write the action object by hand every time:

```js
const todoAdded = text => {
  return {
    type: 'todos/todoAdded',
    payload: text
  }
}
```

We then use them by **calling the action creator**, and then **passing the resulting action object directly to `dispatch`**:

```js
store.dispatch(todoAdded('Buy milk'))
```

This doesn't change anything about how the application works, or how the Redux data flow behaves - we're still creating action objects, and dispatching them. But, instead of writing action objects directly in our code all the time, we're now using action creators to prepare those action objects before they're dispatched.



## Memoized selectors

다음과 같은 selector를 사용할 때엔 문제점이 있다:

```js
const selectTodoIds = state => state.todos.map(todo => todo.id)
```

 `array.map()` always returns a new array reference. We know that the React-Redux `useSelector` hook will re-run its selector function after *every* dispatched action, and if the selector result changes, it will force the component to re-render.

In this example, **calling `useSelector(selectTodoIds)` will always cause the component to re-render after every action, because it's returning a new array reference!**

There's an option here: we could use "memoized" selectors. **Memoized selector functions** are selectors that save the most recent result value, and if you call them multiple times with the same inputs, will return the same result value. If you call them with *different* inputs than last time, they will recalculate a new result value, cache it, and return the new result.

### `createSelector`

The **Reselect library provides a `createSelector` API that will generate memoized selector functions**. `createSelector` accepts one or more "input selector" functions as arguments, plus an "output selector", and returns the new selector function. Every time you call the selector:

- All "input selectors" are called with all of the arguments
- If any of the input selector return values have changed, the "output selector" will re-run
- All of the input selector results become arguments to the output selector
- The final result of the output selector is cached for next time

#### ex)

First, we need to install Reselect:

```bash
$ npm install reselect
```

Then, we can import and call `createSelector`.

```js
import { createSelector } from 'reselect'

export const selectTodoIds = createSelector(
  // First, pass one or more "input selector" functions:
  state => state.todos,
  // Then, an "output selector" that receives all the input results as arguments
  // and returns a final result value
  todos => todos.map(todo => todo.id)
)
```

`state.todos`(input selectors)가 변하지 않는다면, `todos.map(todo => todo.id)`의 값(output selector result)도 변하지 않으므로, 새로운 reference의 id 배열이 아닌, 기존에 memoize 해놨던 배열을 반환한다.

### Selectors with multiple arguments

Input selector로 여러 개를 전달할 수도 있다:

```js
export const selectFilteredTodos = createSelector(
  // First input selector: all todos
  state => state.todos,
  // Second input selector: current status filter
  state => state.filters.status,
  // Output selector: receives both values
  (todos, status) => {
    if (status === StatusFilters.All) {
      return todos
    }

    const completedStatus = status === StatusFilters.Completed
    // Return either active or completed todos based on filter
    return todos.filter(todo => todo.completed === completedStatus)
  }
)
```



## Flux standard actions

Redux has the "Flux Standard Actions" convention, or "FSA". This is a suggested approach for how to organize fields inside of action objects, so that developers always know what fields contain what kind of data. The FSA pattern is widely used in the Redux community.

The FSA convention says that:

- If your action object has any actual data, that "data" value of your action should always go in `action.payload`
- An action may also have an `action.meta` field with extra descriptive data
- An action may have an `action.error` field with error information

So, *all* Redux actions MUST:

- be a plain JavaScript object
- have a `type` field

And if you write your actions using the FSA pattern, an action MAY

- have a `payload` field
- have an `error` field
- have a `meta` field



## Normalized state

In large Redux apps, it is common to store data in a **normalized state structure**. "Normalization" means:

- Making sure there is only one copy of each piece of data
- Storing items in a way that allows directly finding items by ID
- Referring to other items based on IDs, instead of copying the entire item

For example, in a blogging application, you might have `Post` objects that point to `User` and `Comment` objects. There might be many posts by the same person, so if every `Post` object includes an entire `User`, we would have many copies of the same `User` object. Instead, a `Post` object would have a user ID value as `post.user`, and then we could look up `User` objects by ID as `state.users[post.user]`.

This means we typically organize our data as objects instead of arrays, where the item IDs are the keys and the items themselves are the values, like this:

```js
const rootState = {
  todos: {
    status: 'idle',
    entities: {
      2: { id: 2, text: 'Buy milk', completed: false },
      7: { id: 7, text: 'Clean room', completed: true }
    }
  }
}
```

And the reducers should change like this:

```js
const initialState = {
  status: 'idle',
  entities: {}
}

export default function todosReducer(state = initialState, action) {
  switch (action.type) {
    case 'todos/todoAdded': {
      const todo = action.payload
      return {
        ...state,
        entities: {
          ...state.entities,
          [todo.id]: todo
        }
      }
    }
    case 'todos/todoToggled': {
      const todoId = action.payload
      const todo = state.entities[todoId]
      return {
        ...state,
        entities: {
          ...state.entities,
          [todoId]: {
            ...todo,
            completed: !todo.completed
          }
        }
      }
    }
  }
}
```

Because our `state.entities` field is now an object instead of an array, we have to use nested object spread operators to update the data instead of array operations. Also, we can't loop over objects the way we loop over arrays, so there's several places where we have to use `Object.values(entities)` to get an array of the todo items so that we can loop over them.



## References

https://redux.js.org/tutorials/fundamentals/part-7-standard-patterns
