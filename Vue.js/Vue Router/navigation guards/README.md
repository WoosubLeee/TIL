# navigation guards

## What is navigation guards?

The navigation guards provided by `vue-router` are used to guard navigations by redirecting it or canceling it.

## 3 arguments of guard function

- `to` : The target route object
- `from` : The current route being navigated away from
- `next` : This function must be called to resolve the hook. Or the navigation is considered pending.
  - `next()` : Move on to the next hook. If no hooks are left, the navigation is confirmed.
  - `next(false)` : Abort the current navigation.
  - `next('/')`, `next({ path: '/' })` : Redirect to a different location.

Make sure that the `next` function should be called.

## 3 ways to hook into the route navigation process

- globally
- per-route
- in-component

### globally

#### global before guards

Global before guards are called in creation order, whenever a navigation is triggered. Guards may be resolved **asynchronously**. Navigation is considered **pending** before all hooks have been resolved.

```js
const router = new VueRouter({ ... })

router.beforeEach((to, from, next) => {
  // ...
})
```

#### global after hooks

Unlike guards, these hooks do not get a `next` function

```js
router.afterEach((to, from) => {
  // ...
})
```

### per-route

You can define `beforeEnter` guards.

```js
const router = new VueRouter({
  routes: [
    {
      path: '/foo',
      component: Foo,
      beforeEnter: (to, from, next) => {
        // ...
      }
    }
  ]
})
```

These guards have the exact same signature as global before guards.

### in-component

```js
const Foo = {
  template: `...`,
  beforeRouteEnter(to, from, next) {
    // ...
  },
  beforeRouteUpdate(to, from, next) {
    // ...
  },
  beforeRouteLeave(to, from, next) {
    // ...
  }
}
```

#### `beforeRouteEnter`

Called before the route is confirmed.

Doesn't have access to `this` component instance. But you can access the instance by passing a callback to `next`. The callback will be called when the navigation is confirmed, and the component instance will be passed to the callback as the argument.

```js
beforeRouteEnter (to, from, next) {
  next(vm => {
    // access to component instance via `vm`
    // vm === this
  })
}
```

#### `beforeRouteUpdate`

컴포넌트를 재사용 할 경우에 발생하는 훅이다.

For example, for a route with dynamic params `/foo/:id`, when we navigate from `/foo/1` to `/foo/2`, the same component is reused. Then this hook will be called.

Has access to `this` component instance.

#### `beforeRouteLeave` 

Called when the route is about to be navigated away from. Has access to `this` component instance.

It's usually used to prevent the user from accidentally leaving the route with unsaved edits. The navigation can be canceled by calling `next(false)`.

```js
beforeRouteLeave (to, from, next) {
  const answer = window.confirm('Do you really want to leave? you have unsaved changes!')
  if (answer) {
    next()
  } else {
    next(false)
  }
}
```

## The full navigation resolution flow

1. Navigation triggered.
2. Call `beforeRouteLeave` guards in deactivated components.
3. Call global `beforeEach` guards.
4. Call `beforeRouteUpdate` guards in reused components.
5. Call `beforeEnter` in route configs.
6. Resolve async route components.
7. Call `beforeRouteEnter` in activated components.
8. Call global `beforeResolve` guards.
9. Navigation confirmed.
10. Call global `afterEach` hooks.
11. DOM updates triggered.
12. Call callbacks passed to `next` in `beforeRouteEnter` guards with instantiated instances.

## References

https://router.vuejs.org/guide/advanced/navigation-guards.html#navigation-guards (Navigation Guards)

https://adeuran.tistory.com/14 (Vue Router의 LifeCycle 이해하기)