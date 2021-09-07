# Modules

## What is module?

ES6 introduced an easy way of sharing. This involves exporting parts of a file for use in one or more other files, and importing the parts you need, where you need them.

## Exporting

The first thing you do to get access to module features is export them. This is done using the `export` statement.

```js
export const name = 'square';

export function test(a, b) {
  return {
    a: a,
    b: b
  };
}
```

or

```js
export { name, test };
```

You can export functions, `var`, `let`, `const`, and classes. They need to be top-level items, you can't `export` inside a function, for example.



## Importing

```js
import { name, test } from './modules.js';
```

Once you've imported the features into your script, you can use them just like they were defined inside the same file.



## Applying the module to HTML

First of all, you need to include `type="module"` in the `<script>` element.

```html
<script type="module" src="modules.js"></script>
```



## `.mjs` vs. `.js`

The reason of using `mjs` are:

- good for clarity, i.e. makes it clear which files are modules, and which are regular JS.
- ensures that your modules are parsed as a module by runtimes.

하지만 꼭 `.mjs`를 사용해야만 하는 것은 아니다. 오히려 `.mjs`가 오류를 일으킬 수도 있으니 `.js`를 사용하는 것이 더 나을 수도 있다.



