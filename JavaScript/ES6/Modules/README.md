# Modules

## What is module?

ES6 introduced an easy way of sharing. This involves exporting parts of a file for use in one or more other files, and importing the parts you need, where you need them.



## Export

The first thing you do to get access to module features is export them. This is done using the `export` statement. \ They need to be top-level items, you can't `export` inside a function, for example.

### Named export

Zero or more exports per module.

```js
// export features declared earlier
export { myFunction, myVariable };

// export individual features (can export var, let,
// const, function, class)
export let myVariable = Math.sqrt(2);
export function myFunction() { ... };
```

You can export functions, `var`, `let`, `const`, and classes. 

During the import, it is mandatory to use the same name of the corresponding object.

### Default export

One export per module.

```js
// export feature declared earlier as default
export { myFunction as default };

// export individual features as default
export default function () { ... }
export default class { .. }

// each export overwrites the previous one
```

`var`, `let`, `const`는 바로 `export default` 할 수 없다.

```js
export default const variable = "variable";  // error
```

A default export can be imported with any name.



## Import

```js
import { name, test } from './modules.js';
```

Once you've imported the features into your script, you can use them just like they were defined inside the same file.

### Import default export

```js
import myDefault from './modules.js';
```

The imported value is not surrounded by curly braces.

### Import an entire module's contents

```js
import * as myModule from './modules.js';
```





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



