# JavaScript

## 8 data types

1. `undefined`

2. `null`

3. `boolean`

4. `string`

5. `symbol`

6. `bigint`

   `BigInt`는 정수 리터럴의 뒤에 n을 붙이거나 function `BigInt()`를 호출해 생성할 수 있다.

   ```js
   const theBiggestInt = 9007199254740991n;
   const alsoHuge = BigInt(9007199254740991);
   ```

   `BigInt`와 `Number`는 어떤 면에서 비슷하지만 중요한 차이점이 있다. 예컨대 `BigInt`는 내장 `Math` 객체의 메서드와 함께 사용할 수 없고, 연산에서 `Number`와 혼합해 사용할 수 없다. 따라서 먼저 같은 자료형으로 변환해야 한다. 그러나, `BigInt`가 `Number`로 바뀌면 정확성을 잃을 수 있으니 주의해야 한다.

7. `number`

8. `object`

### References

[BigInt](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/BigInt)



## String

### Escape sequences

| Code | Output          |
| ---- | --------------- |
| `\'` | single quote    |
| `\"` | double quote    |
| `\\` | backslash       |
| `\n` | newline         |
| `\r` | carriage return |
| `\t` | tab             |
| `\b` | word boundary   |
| `\f` | form feed       |

### Index

Bracket notation을 사용한다.

```js
var firstName = 'Charles';
console.log(firstName[0]); // C
```

### Immutability

```js
var myStr = "Bob";
myStr[0] = "J";
// Job으로 바뀌지 않는다.
```

### Convert to Integer

Use `parseInt()`

```js
var a = parseInt("007");  // 7
```

`parseInt()` function takes a second argument for the radix, which specifies the base of the number in the string. The radix can be an integer between 2 and 36.

```js
var a = parseInt("11", 2);
```

The radix variable says that `11` is in the binary system, or base 2. This example converts the string `11` to an integer `3`.

### Methods

#### `split()`

Splits a string into an array of strings. It takes an argument for the delimiter, which can be a character to use to break up the string or a regular expression.

```js
var str = "Hello World";
var bySpace = str.split(" ");  // ["Hello", "World"]

var otherString = "How9are7you2today";
var byDigits = otherString.split(/\d/);  // ["How", "are", "you", "today"]
```

#### `replace()`

The **`replace()`** method returns a new string with some or all matches of a `pattern` replaced by a `replacement`. The `pattern` can be a string or a `Regexp`, and the `replacement` can be a string or a function to be called for each match. If `pattern` is a string, only the first occurrence will be replaced.

```js
replace(regexp, newSubstr)
replace(regexp, replacerFunction)

replace(substr, newSubstr)
replace(substr, replacerFunction)
```



## Array

### Index

Bracket notation을 사용한다.

```js
var array = [50,60,70];
console.log(array[0]); // 50
```

### Mutability

String과는 달리 mutable하다.

```js
var ourArray = [50,40,30];
ourArray[0] = 15;
console.log(ourArray); // [15, 40, 30]
```

### Methods

#### `indexOf()`

Takes an element as a parameter, and when called, it returns the position, or index, of that element, or `-1` if the element does not exist on the array.

```js
let fruits = ['apples', 'pears', 'oranges', 'peaches', 'pears'];

fruits.indexOf('dates');  // -1
fruits.indexOf('oranges');  // 2
fruits.indexOf('pears');  // 1(the first index at which each element exists)
```

#### Manipulating arrays

##### `push()`

array의 맨 끝에 데이터를 추가한다.

```js
var arr1 = [1,2,3];
arr1.push(4);
console.log(arr1); // [1, 2, 3, 4]
```

##### `pop()`

Pops a value off of the end of an array.

```js
var threeArr = [1, 4, 6];
var oneDown = threeArr.pop();
console.log(oneDown); // 6
```

##### `shift()`

Removes the first element of an array.

```js
var ourArray = ["Stimpson", "J", ["cat"]];
var removedFromOurArray = ourArray.shift();
console.log(removedFromOurArray); // "Stimpson"
```

##### `unshift()`

Add an element at the beginning of an array.

```js
var ourArray = ["J", "cat"];
ourArray.unshift("Happy");
console.log(ourArray); // ["Happy", "J", "cat"]
```

##### `splice()`

Remove any number of consecutive elements from anywhere in an array. The first parameter represents the index on the array from which to begin removing elements, while the second parameter indicates the number of elements to delete.

```js
let array = ['I', 'am', 'feeling', 'really', 'happy'];
let newArray = array.splice(3, 2);
console.log(array);  // ['I', 'am', 'feeling'];
console.log(newArray);  // ['really', 'happy'];
```

You can use the third parameter, comprised of one or more elements, to add to the array.

```js
const numbers = [10, 11, 12, 12, 15];
const startIndex = 3;
const amountToDelete = 1;

numbers.splice(startIndex, amountToDelete, 13, 14);
console.log(numbers);  // [10, 11, 12, 13, 14, 15]
```

##### `slice()`

Copies or extracts a given number of elements to a new array, leaving the array it is called upon untouched. `slice()` takes only 2 parameters — the first is the index at which to begin extraction, and the second is the index at which to stop extraction (extraction will occur up to, but not including the element at this index).

```js
let weatherConditions = ['rain', 'snow', 'sleet', 'hail', 'clear'];
let todaysWeather = weatherConditions.slice(1, 3);
console.log(weatherConditions)  // ['rain', 'snow', 'sleet', 'hail', 'clear']
console.log(todaysWeather)  // ['snow', 'sleet']
```

##### `concat()`

For arrays, the method is called on one, then another array is provided as the argument to `concat`, which is added to the end of the first array. It returns a new array and does not mutate either of the original arrays.

```js
[1, 2, 3].concat([4, 5, 6]);  // [1, 2, 3, 4, 5, 6]
```

##### `map()`

The `map` method iterates over each item in an array and returns a new array containing the results of calling the callback function on each element. It does this without mutating the original array.

```js
arr.map(callback(currentValue[, index[, array]])[, thisArg])
```

When the callback is used, it is passed three arguments. The first argument is the current element being processed. The second is the index of that element and the third is the array upon which the `map` method was called.

```js
const users = [
  { name: 'John', age: 34 },
  { name: 'Amy', age: 20 },
  { name: 'camperCat', age: 10 }
];

const names = users.map(user => user.name);
console.log(names);  // ['John', 'Amy', 'camperCat']
```

##### `filter()`

`filter` calls a function on each element of an array and returns a new array containing only the elements for which that function returns `true`. Like `map()`, it does this without needing to modify the original array.

```js
arr.filter(callback(element[, index[, array]])[, thisArg])
```

The callback function accepts three arguments. The first argument is the current element being processed. The second is the index of that element and the third is the array upon which the `filter` method was called.

```js
const users = [
  { name: 'John', age: 34 },
  { name: 'Amy', age: 20 },
  { name: 'camperCat', age: 10 }
];

const usersUnder30 = users.filter(user => user.age < 30);
console.log(usersUnder30);
// [{name: 'Amy', age: 20}, {name: 'camperCat', age: 10}]
```

##### `reduce()`

The `reduce` method iterates over each item in an array and returns a single value (i.e. string, number, object, array). This is achieved via a callback function that is called on each iteration. It's possible to show that both `filter` and `map` can be derived as special applications of `reduce`.

```js
arr.reduce(callback(previousValue, currentValue, currentIndex, array) { ... }, initialValue)
```

- `callback` : takes four arguments:
  - *previousValue* (the value resulting from the previous call to `callbackfn`)
  - *currentValue* (the value of the current element)
  - *currentIndex* Optional
  - *array* (the array to traverse) Optional
- `initialValue` : A value to which *previousValue* is initialized the first time the callback is called. If `initialValue` is *not* specified, *previousValue* is initialized to the first value in the array, and *currentValue* is initialized to the second value in the array.

```js
const users = [
  { name: 'John', age: 34 },
  { name: 'Amy', age: 20 },
  { name: 'camperCat', age: 10 }
];

const sumOfAges = users.reduce((sum, user) => sum + user.age, 0);
console.log(sumOfAges);  // 64
```

```js
const users = [
  { name: 'John', age: 34 },
  { name: 'Amy', age: 20 },
  { name: 'camperCat', age: 10 }
];

const usersObj = users.reduce((obj, user) => {
  obj[user.name] = user.age;
  return obj;
}, {});
console.log(usersObj);  // {John: 34, Amy: 20, camperCat: 10}
```

##### `sort()`

Sorts the elements of an array according to the callback function.

When such a callback function, normally called `compareFunction`, is supplied, the array elements are sorted according to the return value of the `compareFunction`: If `compareFunction(a,b)` returns a value less than 0 for two elements `a` and `b`, then `a` will come before `b`. If `compareFunction(a,b)` returns a value greater than 0 for two elements `a` and `b`, then `b` will come before `a`. If `compareFunction(a,b)` returns a value equal to 0 for two elements `a` and `b`, then `a` and `b` will remain unchanged.

```js
function ascendingOrder(arr) {
  return arr.sort(function(a, b) {
    return a - b;
  });
}
ascendingOrder([1, 5, 2, 3, 4]);  // [1, 2, 3, 4, 5]
```

##### `join()`

The `join` method is used to join the elements of an array together to create a string. It takes an argument for the delimiter that is used to separate the array elements in the string.

```js
var arr = ["Hello", "World"];
var str = arr.join(" ");  // 'Hello World'
```

##### `every()`

The `every` method works with arrays to check if *every* element passes a particular test. It returns a Boolean value - `true` if all values meet the criteria, `false` if not.

```js
var numbers = [1, 5, 8, 0, 10, 11];
numbers.every(function(currentValue) {
  return currentValue < 10;
});  // false
```

##### `some()`

The `some` method works with arrays to check if *any* element passes a particular test. It returns a Boolean value - `true` if any of the values meet the criteria, `false` if not.

```js
var numbers = [10, 50, 8, 220, 110, 11];
numbers.some(function(currentValue) {
  return currentValue < 10;
});  // true
```



## Scopes

### Block scope

Variables declared inside a `{ }` block with `let` and `const` keywords cannot be accessed from outside the block.

```js
{
  let x = 2;
}
// x can NOT be used here
```

\* Variables declared with the `var` keyword can't have block scope.

```js
{
  var x = 2;
}
// x CAN be used here
```

### Function scope

Variables declared within a JavaScript function, become local to the function.

```js
// code here can NOT use carName

function myFunction() {
  let carName = "Volvo"; // [var, let, const] All of them can be used.
  // code here CAN use carName
}

// code here can NOT use carName
```

### Global

- Variables defined outside of a function block

```js
let carName = "Volvo";
// code here can use carName

function myFunction() {
// code here can also use carName
}
```

- Variables declared without the `var` keyword

```js
myFunction();

// code here can use carName

function myFunction() {
  carName = "Volvo";
}
```

### \* Global vs. Function

When you have both global and local variables with the same name, the local variable takes precedence over the global variable.

```js
var someVar = "Hat";

function myFun() {
  var someVar = "Head";
  return someVar; // "Head"
}
```



## Operators

### `==` vs. `===`

`==` operator checks equality only after converting both the values to a common type.

```js
console.log(21 == 21);
console.log(21 == '21');
console.log('food is love'=='food is love');
console.log(true == 1);
console.log(false == 0);
console.log(null == undefined);
// all outputs are true.
```

`===` operator, also known as strict equality operator, it compares both the value and the type.

```js
console.log(true === 1);
console.log(true === 'true');
console.log(5 === '5');
// all outputs are false.
```

### `!=` vs. `!==`

`!=` operator checks equality only after converting both the values to a common type.

```js
1 != 2 // true
1 != "1" // false
1 != '1' // false
1 != true // false
0 != false // false
```

`!==` operator, it compares both the value and the type.

```js
3 !== 3 // false
3 !== '3' // true
4 !== 3 // true
```

### `>`, `>=`

Like the `==` operator, these operators will convert data types of values while comparing.

```js
5 > '3' // true
7 >= '3' // true
```



## 조건문

### `switch` statements

A `switch` statement tests a value and can have many `case` statements which define various possible values. Statements are executed from the first matched `case` value until a `break` is encountered.

`case` values are tested with strict equality(`===`).

```js
switch (lowercaseLetter) {
  case "a":
    console.log("A");
    break;
  case "b":
    console.log("B");
    break;
}
```

`break` 문을 쓰지 않는다면 한 번 case test를 통과하면 그 뒤에 있는 코드는 `break`가 나올때 까지 case test 결과와 상관없이 모두 실행된다.

```js
function test(lowercaseLetter) {
  switch (lowercaseLetter) {
    case "a":
      console.log("A");
    case "b":
      console.log("B");
      break;
    case "c":
      console.log("C");
      break;
  }
}

test("a")
// A
// B
```

아래와 같이 활용도 가능하다.

```js
var result = "";
switch(val) {
  case 1:
  case 2:
  case 3:
    result = "1, 2, or 3";
    break;
  case 4:
    result = "4 alone";
}
```

#### `default`

You can add the `default` statement which will be executed if no matching `case` statements are found. Think of it like the final `else` statement in an `if/else` chain.

```js
switch (num) {
  case value1:
    statement1;
    break;
  case value2:
    statement2;
    break;
...
  default:
    defaultStatement;
    break;
}
```

###  Ternary operator

It can be used as a one line if-else expression. The syntax is `a ? b : c`, where `a ` is the condition, `b` is the code to run when the condition returns `true`, and `c` is the code to run when the condition returns `false`.

```js
function findGreater(a, b) {
  return a > b ? "a is greater" : "b is greater or equal";
}
```

You can also chain them together to check for multiple conditions.

```js
function findGreaterOrEqual(a, b) {
  return (a === b) ? "a and b are equal" 
    : (a > b) ? "a is greater" 
    : "b is greater";
}
```

It's considered best practice to format multiple conditional operators such that each condition is on a separtae line, as shown above.



## 반복문

### Loops

#### `while`

```js
var ourArray = [];
var i = 0;
while(i < 5) {
  ourArray.push(i);
  i++;
}
```

#### `do...while`

It will first `do` one pass of the code inside the loop no matter what, and then continue to run the loop `while` the specified condition evaluates to `true`.

```js
var ourArray = [];
var i = 7;
do {
  ourArray.push(i);
  i++;
} while (i < 5);

console.log(ourArray)  // [7]
```

#### `for`

`for` loops are declared with three optional expressions separated by semicolons. `for (a; b; c)`, where `a` is the initialization statement, `b` is the condition statement, and `c` is the final expression.

```js
var ourArray = [];
for (var i = 0; i < 5; i++) {
  ourArray.push(i);
}
// [0, 1, 2, 3, 4]
```



## Strict mode

JavaScript's strict mode, introduced in ES5, is a way to *opt in* to a restricted variant of JavaScript, thereby implicitly opting-out of "sloppy mode". Strict mode makes several changes to normal JavaScript semantics:

1. Eliminates some JavaScript silent errors by changing them to throw errors.
2. Fixes mistakes that make it difficult for JavaScript engines to perform optimizations: strict mode code can sometimes be made to run faster than identical code that's not strict mode.
3. Prohibits some syntax likely to be defined in future versions of ECMAScript.

### Invoking strict mode

Put the exact statement `'use strict'` or `"use strict"` before any other statements.

1. entire scripts

   ```js
   // Whole-script strict mode syntax
   'use strict';
   var v = "Hi! I'm a strict mode script!";
   ```

2. individual functions

   ```js
   function strict() {
     // Function-level strict mode syntax
     'use strict';
     function nested() { return 'And so am I!'; }
     return "Hi!  I'm a strict mode function!  " + nested();
   }
   function notStrict() { return "I'm not strict."; }
   ```

3. modules, classes

   All of modules and classes are strict mode code.

### References

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode