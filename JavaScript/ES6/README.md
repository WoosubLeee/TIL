# ES6

### `var` vs `let` vs `const`

|             | var                                 | let   | const |
| ----------- | ----------------------------------- | ----- | ----- |
| 변수 재선언 | O                                   | X     | X     |
| 변수 재할당 | O                                   | O     | X     |
| Hoisting    | O                                   | X     | X     |
| Scope       | Global<br />Function(in a function) | Block | Block |

#### `const` mutation

재선언, 재할당은 불가능하지만 `const` array의 경우 mutate는 가능하다.

```js
const s = [5, 6, 7];
s = [1, 2, 3];  // error
s[2] = 45;  // [5, 6, 45]
```



### Hoisting

A variable can be declared after it has been used.

```js
x = 5; // Assign 5 to x

console.log(x) // 5

var x; // Declare x
```

#### Declarations vs Initializations

JS only hoists **declarations**, not initializations.

```js
// Example 1

var x = 5;
var y = 7;

console.log(x + ' ' + y);  // 5 7
```

```js
// Example 2

var x = 5;

console.log(x + ' ' + y);  // 5 undefined

var y = 7;
```

The difference between two examples happened because only the declaration(`var y`), not the initialization(`=7`)  is hoisted to the top.

#### `let`, `const`

`let`과 `const`는 호이스팅이 적용되지 않는다.(엄밀히 말하자면 적용되지만, 적용되지 않는다고 생각해도 무관하다.)

#### Conventions

Hosting is not recommended because it can cause bugs. So always declare all variables at the beginning of every scope.



### Arrow functions

ES6 allows us to shorten anonymous functions.

This is original code.

```js
const myFunc = function() {
  const myVar = "value";
  return myVar;
}
```

You can omit `function` and put an arrow.

```js
const myFunc = () => {
  const myVar = "value";
  return myVar;
}
```

And when there is no function body, and only return a value, arrow function syntax allows you to omit the brackets and `return`.

```js
const myFunc = () => "value";
```

