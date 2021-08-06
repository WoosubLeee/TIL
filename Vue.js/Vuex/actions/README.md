# Actions

## Mutations와의 차이점

- Actions commit mutations, mutations mutate the state.

  Actions -> Mutations -> State

- Actions can contain 비동기 operations.

## context

```js
actions: {
  increment (context) {
    context.commit('increment')
  }
}
```

action handlers는 context object를 받는데, context object를 통해 mutation을 commit(`context.commit`)하고, state와 getters에 접근(`context.state`, `context.getters`)할 수 있다. 다른 action을 call 하는 것도(`context.dispatch`) 가능하다.

## Dispatching actions

Actions are triggered by

```js
store.dispatch('increment')
```

mutation을 사용해 `store.commit('increment')`와 같이 똑같은 동작을 수행할 수 있음에도 action을 사용하는 이유가 무엇일까?

=> **Mutations have to be synchronous**. Actions를 사용해 **asynchronous** operaions를 수행할 수 있다.