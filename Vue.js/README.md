# Vue.js

## project management

### Architecture

#### how to make architecture tree

터미널에서 `$ tree > 파일명.txt` 를 입력한다.

#### example

##### 1)

```
.
├─ README.md
├─ index.html
├─ webpack.config.js
├─ package.json
└─ src
   ├─ main.js
   ├─ App.vue
   ├─ components        컴포넌트
   │  ├─ common
   │  └─ ...
   ├─ routes            라우터
   │  ├─ index.js
   │  └─ routes.js
   ├─ views             라우터 페이지
   │  ├─ MainView.vue
   │  └─ ...
   ├─ store             상태 관리
   │  ├─ auth
   │  ├─ index.js
   │  └─ ...
   ├─ api               api 함수
   │  ├─ index.js
   │  ├─ users.js
   │  └─ ...
   ├─ utils             필터 등의 유틸리티 함수
   │  ├─ filters.js
   │  ├─ bus.js
   │  └─ ...
   ├─ mixins            믹스인
   │  ├─ index.js
   │  └─ ...
   ├─ plugins           플러그인
   │  ├─ ChartPlugin.js
   │  └─ ...
   ├─ translations      다국어
   │  ├─ index.js
   │  ├─ en.json
   │  └─ ...
   ├─ images            이미지
   ├─ fonts             폰트
   └─ assets            기타 자원
```



## watch

### handler

`handler`는 `watch`된 속성이 변경될 때 호출될 함수를 지정한다.

다만, `deep`, `immediate` option이 없을 경우에는 생략할 수 있다.

### options

#### `{boolean} deep`

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

#### `{boolean} immediate`

When `immediate: true` is passed, callback will be immediately triggered even though the target hasn't changed yet.



## Slots

### What is slot?

slot은 컴포넌트의 재사용성을 높여주는 기능입니다. 특정 컴포넌트에 등록된 하위 컴포넌트의 마크업을 확장하거나 재정의할 수 있습니다.

### How to use

slot을 삽입한 자식 컴포넌트를 생성 후,

```html
<!-- NavigationLink.vue -->

<a
  v-bind:href="url"
  class="nav-link"
>
  <slot></slot>
</a>
```

부모 컴포넌트에서 자식 컴포넌트의 opening tag와 closing tag 사이에 코드를 작성하게 되면, `<slot></slot>`이 해당 코드로 대체되게 된다.

```html
<navigation-link url="/profile">
  <i class="fa fa-user"></i>
  My Profile
</navigation-link>
```

It's also possible to insert other components.

```html
<navigation-link url="/profile">
  <!-- Use a component to add an icon -->
  <font-awesome-icon name="user"></font-awesome-icon>
  My Profile
</navigation-link>
```

#### Compilation scope

Slot has access to the same instance properties (i.e. the same "scope") as the rest of the template. The slot doesn't have access to the child component's scope.

```html
<navigation-link url="/profile">
  Clicking here will send you to: {{ url }}
  <!--
  The `url` will be undefined, because this content is passed
  _to_ <navigation-link>, rather than defined _inside_ the
  <navigation-link> component.
  -->
</navigation-link>
```

#### Fallback content

You can specify fallback (i.e. default) content for a slot, to be rendered only when no content is provided.

To make “Submit” the fallback content, we can place it in between the `<slot>` tags.

```html
<!-- SubmitButton.vue -->

<button type="submit">
  <slot>Submit</slot>
</button>
```

Now when we use `<submit-button>` in a parent component, providing no content for the slot

```html
<submit-button></submit-button>
```

will render the fallback content, "Submit".

But if we provide content,

```html
<submit-button>
  Save
</submit-button>
```

Then the provided content will be rendered instead.

#### Named slots

You can use multiple slots. For these cases, the `<slot>` element has a special attribute, `name`, which can be used to define additional slots.

```html
<!-- BaseLayout.vue -->

<div class="container">
  <header>
    <slot name="header"></slot>
  </header>
  <main>
    <slot></slot>
  </main>
  <footer>
    <slot name="footer"></slot>
  </footer>
</div>
```

A `<slot>` outlet without `name` implicitly has the name “default”.

To provide content to named slots, we can use the `v-slot` directive on a `<template>`, providing the name of the slot as `v-slot`‘s argument.

```html
<base-layout>
  <template v-slot:header>
    <h1>Here might be a page title</h1>
  </template>

  <p>A paragraph for the main content.</p>
  <p>And another one.</p>

  <template v-slot:footer>
    <p>Here's some contact info</p>
  </template>
</base-layout>
```

Any content not wrapped in a `<template>` using `v-slot` is assumed to be for the default slot. However, you can still wrap default slot content in a `<template>` if you wish to be explicit.

```html
<template v-slot:default>
  <p>A paragraph for the main content.</p>
  <p>And another one.</p>
</template>
```

Note that **`v-slot` can only be added to a `<template>`**.



## mixins

### What is mixins?

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

### Option Merging

Mixin과 component가 중복 option을 갖고 있을 시, 상황에 따라 다른 방식으로 merge된다.

**`data`** : component > mixin

**lifecycle hooks** : component < mixin - mixin의 hook이 먼저 실행되고, 그 후 component의 hook이 실행된다.

**Options that expect object values(ex-`methods`, `components`, `directives`)** : component > mixin



## References

https://velog.io/@cindy-choi/VUE-%EC%9A%B0%EC%95%84%ED%95%9C-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EA%B5%AC%EC%A1%B0-%EC%A7%9C%EA%B8%B0 ([VUE] 🌱우아한 프로젝트 구조 짜기)

https://joshua1988.github.io/web-development/vuejs/vue-structure/ (실무에서 사용하는 Vue.js 프로젝트 구조)

https://vuejs.org/v2/guide/components-slots.html

https://joshua1988.github.io/web-development/vuejs/slots/ (Vue.js 컴포넌트 재사용하기 - slot 편)

https://vuejs.org/v2/api/#watch

https://vuejs.org/v2/api/#vm-watch

https://ui.toast.com/weekly-pick/ko_20190307 (Vue에서 중첩 데이터를 감시하는 법)