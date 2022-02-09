# Redux Toolkit

Redux Toolkit contains packages and functions that we think are essential for building a Redux app. Redux Toolkit builds in our suggested best practices, simplifies most Redux tasks, prevents common mistakes, and makes it easier to write Redux applications.

When you use Redux Toolkit, all the concepts that's important(actions, reducers, store setup, action creators, thunks, etc) still exist, but **Redux Toolkit provides easier ways to write that code**.



## Installation

```bash
$ npm install @reduxjs/toolkit
```



## Store setup

Setting up logic for Redux store without Redux Toolkit would look like this:

```js
// src/rootReducer.js

import { combineReducers } from 'redux'

import todosReducer from './features/todos/todosSlice'
import filtersReducer from './features/filters/filtersSlice'

const rootReducer = combineReducers({
  // Define a top-level state field named `todos`, handled by `todosReducer`
  todos: todosReducer,
  filters: filtersReducer
})

export default rootReducer
```

```js
// src/store.js

import { createStore, applyMiddleware } from 'redux'
import thunkMiddleware from 'redux-thunk'
import { composeWithDevTools } from 'redux-devtools-extension'
import rootReducer from './reducer'

const composedEnhancer = composeWithDevTools(applyMiddleware(thunkMiddleware))

const store = createStore(rootReducer, composedEnhancer)
export default store
```

Notice that the setup process takes several steps. We have to:

- Combine the slice reducers together to form the root reducer
- Import the root reducer into the store file
- Import the thunk middleware, `applyMiddleware`, and `composeWithDevTools` APIs
- Create a store enhancer with the middleware and devtools
- Create the store with the root reducer

It would be nice if we could cut down the number of steps here.

### Using `configureStore`

**Redux Toolkit has a `configureStore` API that simplifies the store setup process**. `configureStore` wraps around the Redux core `createStore` API, and handles most of the store setup for us automatically. In fact, we can cut it down to effectively one step:

```js
import { configureStore } from '@reduxjs/toolkit'

import todosReducer from './features/todos/todosSlice'
import filtersReducer from './features/filters/filtersSlice'

const store = configureStore({
  reducer: {
    // Define a top-level state field named `todos`, handled by `todosReducer`
    todos: todosReducer,
    filters: filtersReducer
  }
})

export default store
```

That one call to `configureStore` did all the work for us:

- It combined `todosReducer` and `filtersReducer` into the root reducer function, which will handle a root state that looks like `{todos, filters}`
- It created a Redux store using that root reducer
- It automatically added the `thunk` middleware
- It automatically added more middleware to check for common mistakes like accidentally mutating the state
- It automatically set up the Redux DevTools Extension connection



## Writing slices

**Redux Toolkit has a `createSlice` API that will help us simplify our Redux reducer logic and actions**. `createSlice` does several important things for us:

- We can write the case reducers as functions inside of an object, instead of having to write a `switch/case` statement
- The reducers will be able to write shorter immutable update logic
- All the action creators will be generated automatically based on the reducer functions we've provided

### Using `createSlice`

`createSlice` takes an object with three main options fields:

- `name`: a string that will be used as the prefix for generated action types
- `initialState`: the initial state of the reducer
- `reducers`: an object where the keys are strings, and the values are "case reducer" functions that will handle specific actions

Let's look at a small standalone example first.

```js
import { createSlice } from '@reduxjs/toolkit'

const initialState = []

const todosSlice = createSlice({
  name: 'todos',
  initialState,
  reducers: {
    todoAdded(state, action) {
      // ✅ This "mutating" code is okay inside of createSlice!
      state.push(action.payload)
    },
    todoToggled(state, action) {
      const todo = state.find(todo => todo.id === action.payload)
      todo.completed = !todo.completed
    },
    todosLoading(state, action) {
      return {
        ...state,
        status: 'loading'
      }
    }
  }
})

export const { todoAdded, todoToggled, todosLoading } = todosSlice.actions

export default todosSlice.reducer
```

There's several things to see in this example:

- We write case reducer functions inside the `reducers` object, and give them readable names
- **`createSlice` will automatically generate action creators** that correspond to each case reducer function we provide
- `createSlice` automatically returns the existing state in the default case
- **`createSlice` allows us to safely "mutate" our state!**
- But, we can also make immutable copies like before if we want to

The generated action creators will be available as `slice.actions.todoAdded`, and we typically destructure and export those individually like we did with the action creators we wrote earlier. The complete reducer function is available as `slice.reducer`, and we typically `export default slice.reducer`, again the same as before.

### Immutable updates with Immer

`createSlice` uses a library called Immer inside. Immer uses a special JS tool called a `Proxy` to wrap the data you provide, and lets you write code that "mutates" that wrapped data. But, **Immer tracks all the changes you've tried to make, and then uses that list of changes to return a safely immutably updated value**, as if you'd written all the immutable update logic by hand.

### `prepare`

```js
const todosSlice = createSlice({
  name: 'todos',
  initialState,
  reducers: {
    todoAdded(state, action) {
      const todo = action.payload
      state.entities[todo.id] = todo
    },
    todoToggled(state, action) {
      const todoId = action.payload
      const todo = state.entities[todoId]
      todo.completed = !todo.completed
    },
    todoColorSelected: {
      reducer(state, action) {
        const { color, todoId } = action.payload
        state.entities[todoId].color = color
      },
      prepare(todoId, color) {
        return {
          payload: { todoId, color }
        }
      }
    },
    todoDeleted(state, action) {
      delete state.entities[action.payload]
    }
  }
})

export const { todoAdded, todoToggled, todoColorSelected, todoDeleted } =
  todosSlice.actions

export default todosSlice.reducer
```

The action creators for `todoAdded` and `todoToggled` only need to take a single parameter:

- `todoAdded` : an entire `todo` object
- `todoToggled` : a `todo` id

But `todoColorSelected` needs multiple parameters:

- `todoColorSelected` : a `todo` id, `color`

`createSlice` lets us handle those situations by adding a "prepare callback" to the reducer. We can pass an object that has functions named `reducer` and `prepare`. When we call the generated action creator, the `prepare` function will be called with whatever parameters were passed in. It should then create and return an object that has a `payload` field (or, optionally, `meta` and `error` fields), matching the Flux Standard Action convention.



## Writing thunks

Redux Toolkit has a `createAsyncThunk` API that will generate the action types and action creators for different request status actions, and dispatches those actions automatically based on the resulting `Promise`.

### Using `createAsyncThunk`

`createAsyncThunk` accepts two arguments:

- A string that will be used as the prefix for the generated action types
- A "payload creator" callback function that should return a `Promise`. This is often written using the `async/await` syntax, since `async` functions automatically return a promise.

```js
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'

export const fetchTodos = createAsyncThunk('todos/fetchTodos', async () => {
  const response = await client.get('/fakeApi/todos')
  return response.todos
})

const todosSlice = createSlice({
  name: 'todos',
  initialState,
  reducers: {
    // omit reducer cases
  },
  extraReducers: builder => {
    builder
      .addCase(fetchTodos.pending, (state, action) => {
        state.status = 'loading'
      })
      .addCase(fetchTodos.fulfilled, (state, action) => {
        const newEntities = {}
        action.payload.forEach(todo => {
          newEntities[todo.id] = todo
        })
        state.entities = newEntities
        state.status = 'idle'
      })
  }
})
```

We pass `'todos/fetchTodos'` as the string prefix, and a "payload creator" function that calls our API and returns a promise containing the fetched data. Inside, `createAsyncThunk` will generate three action creators and action types, plus a thunk function that automatically dispatches those actions when called. In this case, the action creators and their types are:

- `fetchTodos.pending`: `todos/fetchTodos/pending`
- `fetchTodos.fulfilled`: `todos/fetchTodos/fulfilled`
- `fetchTodos.rejected`: `todos/fetchTodos/rejected`

However, these action creators and types are being defined *outside* of the `createSlice` call. We can't handle those inside of the `createSlice.reducers` field, because those generate new action types too. We need a way for our `createSlice` call to listen for *other* action types that were defined elsewhere.

**`createSlice` also accepts an `extraReducers` option, where we can have the same slice reducer listen for other action types**. This field should be a callback function with a `builder` parameter, and we can call `builder.addCase(actionCreator, caseReducer)` to listen for other actions.

So, here we've called `builder.addCase(fetchTodos.pending, caseReducer)`. When that action is dispatched, we'll run the reducer that sets `state.status = 'loading'`, same as it did earlier when we wrote that logic in a switch statement. We can do the same thing for `fetchTodos.fulfilled`, and handle the data we received from the API.

A few other quick notes for reference:

- You can only pass one argument to the thunk when you dispatch it. If you need to pass multiple values, pass them in a single object
- The payload creator will receive an object as its second argument, which contains `{getState, dispatch}`, and some other useful values
- The thunk dispatches the `pending` action before running your payload creator, then dispatches either `fulfilled` or `rejected` based on whether the `Promise` you return succeeds or fails



## Normalizing state

 **Redux Toolkit includes a `createEntityAdapter` API that has prebuilt reducers for typical data update operations with normalized state**. This includes adding, updating, and removing items from a slice. **`createEntityAdapter` also generates some memoized selectors for reading values from the store**.

### Using `createEntityAdapter`

Calling `createEntityAdapter` gives us an "adapter" object that contains several premade reducer functions, including:

- `addOne` / `addMany`: add new items to the state
- `upsertOne` / `upsertMany`: add new items or update existing ones
- `updateOne` / `updateMany`: update existing items by supplying partial values
- `removeOne` / `removeMany`: remove items based on IDs
- `setAll`: replace all existing items

We can use these functions as case reducers, or as "mutating helpers" inside of `createSlice`.

The adapter also contains:

- `getInitialState`: returns an object that looks like `{ ids: [], entities: {} }`, for storing a normalized state of items along with an array of all item IDs
- `getSelectors`: generates a standard set of selector functions

```js
import {
  createSlice,
  createAsyncThunk,
  createEntityAdapter
} from '@reduxjs/toolkit'

const todosAdapter = createEntityAdapter()

const initialState = todosAdapter.getInitialState({
  status: 'idle'
})

const todosSlice = createSlice({
  name: 'todos',
  initialState,
  reducers: {
    // omit some reducers
    // Use an adapter reducer function to remove a todo by ID
    todoDeleted: todosAdapter.removeOne,
    completedTodosCleared(state, action) {
      const completedIds = Object.values(state.entities)
        .filter(todo => todo.completed)
        .map(todo => todo.id)
      // Use an adapter function as a "mutating" update helper
      todosAdapter.removeMany(state, completedIds)
    }
  },
  extraReducers: builder => {
    builder
      .addCase(fetchTodos.pending, (state, action) => {
        state.status = 'loading'
      })
      .addCase(fetchTodos.fulfilled, (state, action) => {
        todosAdapter.setAll(state, action.payload)
        state.status = 'idle'
      })
      // Use another adapter function as a reducer to add a todo
      .addCase(saveNewTodo.fulfilled, todosAdapter.addOne)
  }
})
```

`getInitialState` allows us to pass in additional state fields that will be included. In this case, we've passed in a `status` field, giving us a final todos slice state of `{ids, entities, status}`, much like we had before.

We can also replace some of our todos selector functions as well. The `getSelectors` adapter function will generate selectors like `selectAll`, which returns an array of all items, and `selectById`, which returns one item. However, since `getSelectors` doesn't know where our data is in the entire Redux state tree, we need to pass in a small selector that returns this slice out of the whole state tree.

```js
import {
  createSelector
} from '@reduxjs/toolkit'

export const { selectAll: selectTodos, selectById: selectTodoById } =
  todosAdapter.getSelectors(state => state.todos)
```



## References

https://redux.js.org/tutorials/fundamentals/part-8-modern-redux