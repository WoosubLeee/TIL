# Slots

## What is slot?

slot은 컴포넌트의 재사용성을 높여주는 기능입니다. 특정 컴포넌트에 등록된 하위 컴포넌트의 마크업을 확장하거나 재정의할 수 있습니다.

## How to use

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

### Compilation scope

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

### Fallback content

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

### Named slots

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

## References

https://vuejs.org/v2/guide/components-slots.html

https://joshua1988.github.io/web-development/vuejs/slots/ (Vue.js 컴포넌트 재사용하기 - slot 편)