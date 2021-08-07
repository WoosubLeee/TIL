# watch

## handler

`handler`는 `watch`된 속성이 변경될 때 호출될 함수를 지정한다.

다만, `deep`, `immediate` option이 없을 경우에는 생략할 수 있다.

## options

### `{boolean} deep`

It's used to detect nested value changes inside Objects.

```js
vm.$watch('someObject', callback, {
  deep: true,
  handler() {
    // ...
  }
  // handler는 다른 option이 없을 때만 생략되는 것이다.
  // 따라서 위와 같이 deep: true가 추가된 경우, handler를 작성해주어야 한다.
})
vm.someObject.nestedValue = 123
// callback is fired
// deep: true를 주지 않으면 Object 속성이 변경이 되어도 watch가 실행되지 않는다
```

### `{boolean} immediate`

When `immediate: true` is passed, callback will be immediately triggered even though the target hasn't changed yet.

## References

https://vuejs.org/v2/api/#watch

https://vuejs.org/v2/api/#vm-watch

https://ui.toast.com/weekly-pick/ko_20190307 (Vue에서 중첩 데이터를 감시하는 법)