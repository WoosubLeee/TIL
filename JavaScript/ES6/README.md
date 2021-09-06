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

This is traditional function.

```js
const myFunc = function (a) {
  return a + 100;
}
```

1. Remove the word `function` and place arrow.

```js
const myFunc = (a) => {
  return a + 100;
}
```

2. (If you have only one line statement) Remove the body braces and `return`.

```js
const myFunc = (a) => a + 100;
```

3. (If you have only one argument) Remove the argument parentheses.

```js
const myFunc = a => a + 100;
```



### Default parameters

You can set default parameters for functions.

```js
const greeting = (name = "Anonymous") => "Hello " + name;

console.log(greeting("John"));  // Hello John
console.log(greeting());  // Hello Anonymous
```



### Rest parameter

With the rest parameter, you can create functions that take a variable number of arguments.

```js
function howMany(...args) {
  return "You have passed " + args.length + " arguments.";
}
console.log(howMany(0, 1, 2));  // You have passed 3 arguments.
console.log(howMany("string", null, [1, 2, 3], { }));  // You have passed 4 arguments.
```



### Spread operator

ES6 introduces the spread operator, which allows us to expand arrays and other expressions in places where multiple parameters or elements are expected.

```js
var arr = [6, 89, 3, 45];
var maximus = Math.max.apply(null, arr);  // until ES5
const maximus = Math.max(...arr);  // ES6
```

However, the spread operator only works in-place, like in an argument to a function or in an array literal. The following code will not work.

```js
const spreaded = ...arr;
```



### Destructuring assignment

It makes it possible to unpack values from arrays, or properties from objects, into distinct variables.

#### Array destructuring

```js
let a, b, rest;
[a, b] = [10, 20, 30];
console.log(a); // 10
console.log(b); // 20

[a, b, ...rest] = [10, 20, 30, 40, 50];
console.log(a); // 10
console.log(b); // 20
console.log(rest); // [30, 40, 50]
```

If the number of variables specified on the left-hand side of the assignment is greater than N, only the first N variables are assigned values. The values of the remaining variables will be undefined.

```js
const foo = ['one', 'two'];

const [red, yellow, green, blue] = foo;
console.log(red); // "one"
console.log(yellow); // "two"
console.log(green); // undefined
console.log(blue);  //undefined
```

##### Swapping variables

```js
let a = 1;
let b = 3;

[a, b] = [b, a];
console.log(a); // 3
console.log(b); // 1

const arr = [1,2,3];
[arr[2], arr[1]] = [arr[1], arr[2]];
console.log(arr); // [1,3,2]
```

##### Ignoring some returned values

```js
const [a, , b] = [1, 0, 3];
console.log(a); // 1
console.log(b); // 3
```

#### Object destructuring

```js
({ a, b } = { a: 10, b: 20, c: 30 });
console.log(a); // 10
console.log(b); // 20

({a, b, ...rest} = {a: 10, b: 20, c: 30, d: 40});
console.log(a); // 10
console.log(b); // 20
console.log(rest); // {c: 30, d: 40}
```

##### Assigning to new variable names

A property can be unpacked from an object and assigned to a variable with a different name than the object property.

```js
const o = {p: 42, q: true};
const {p: foo, q: bar} = o;

console.log(foo); // 42
console.log(bar); // true
```

#### Default values

A variable can be assigned a default, in the case that the value unpacked from the object/array is `undefined`.

```js
const [a=5, b=7] = [1];

console.log(a); // 1
console.log(b); // 7
```

```js
const {a = 10, b = 5} = {a: 3};

console.log(a); // 3
console.log(b); // 5
```



### Template literals

*Untagged* template literals result in strings, which makes them useful for string interpolation (and multiline strings, since unescaped newlines are allowed).

Template literals are enclosed by the backtick. Template literals can contain placeholders. These are indicated by the dollar sign and curly braces (`${expression}`).

```js
const person = {
  name: "Zodiac Hasbro",
  age: 56
};

const greeting = `Hello, my name is ${person.name}!
I am ${person.age} years old.`;

console.log(greeting);
// Hello, my name is Zodiac Hasbro!
// I am 56 years old..
```

Using template literals, you don't have to use `\n`. Both examples below are the same.

```js
console.log('string text line 1\n' +
'string text line 2');
console.log(`string text line 1
string text line 2`);
```

In order to embed expressions, you would use the following syntax.

```js
let a = 5;
let b = 10;
console.log(`Fifteen is ${a + b}.`) // "Fifteen is 15.
```

#### Nesting templates

Within a backticked template, it is simple to allow inner backticks by using them inside a placeholder `${ }` within the template.

```js
const classes = `header ${ isLargeScreen() ? '' :
  `icon-${item.isCollapsed ? 'expander' : 'collapser'}` }`;
```



### Object property shorthand

```js
const getMousePosition = (x, y) => ({
  x: x,
  y: y
});
```

You can shorten this code.

```js
const getMousePosition = (x, y) => ({ x, y });
```

