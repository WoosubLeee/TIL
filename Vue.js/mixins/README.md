# mixins

## What is mixins?

Mixins는 Vue components에 reusable한 기능들을 배부하는 방법이다.

Mixin에는 Vue component에 들어가는 어떤 option도 들어갈 수 있다.

```js
// define a mixin object
var myMixin = {
  created: function () {
    this.hello()
  },
  methods: {
    hello: function () {
      console.log('hello from mixin!')
    }
  }
}

// define a component that uses this mixin
var Component = Vue.extend({
  mixins: [myMixin]
})

var component = new Component() // => "hello from mixin!"
```

## Option Merging

Mixin과 component가 중복 option을 갖고 있을 시, 상황에 따라 다른 방식으로 merge된다.

**`data`** : component > mixin

**lifecycle hooks** : component < mixin - mixin의 hook이 먼저 실행되고, 그 후 component의 hook이 실행된다.

**Options that expect object values(ex-`methods`, `components`, `directives`)** : component > mixin

