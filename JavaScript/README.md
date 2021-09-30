# JavaScript

### 8 data types

1. `undefined`
2. `null`
3. `boolean`
4. `string`
5. `symbol`
6. `bigint`
7. `number`
8. `object`



### Declare variables

```js
var variableA;
const variableB;
```



### Assignment

```js
variableA = 10;
var variableB = 10;
```



### String

#### Escape sequences

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

#### Index

Bracket notation을 사용한다.

```js
var firstName = 'Charles';
console.log(firstName[0]); // C
```

##### Immutability

```js
var myStr = "Bob";
myStr[0] = "J";
// Job으로 바뀌지 않는다.
```

#### Convert to Integer

Use `parseInt()`

```js
var a = parseInt("007");  // 7
```

`parseInt()` function takes a second argument for the radix, which specifies the base of the number in the string. The radix can be an integer between 2 and 36.

```js
var a = parseInt("11", 2);
```

The radix variable says that `11` is in the binary system, or base 2. This example converts the string `11` to an integer `3`.



### Array

#### Index

Bracket notation을 사용한다.

```js
var array = [50,60,70];
console.log(array[0]); // 50
```

##### Mutability

String과는 달리 mutable하다.

```js
var ourArray = [50,40,30];
ourArray[0] = 15;
console.log(ourArray); // [15, 40, 30]
```

##### `indexOf()`

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



### Scopes

#### Block scope

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

#### Function scope

Variables declared within a JavaScript function, become local to the function.

```js
// code here can NOT use carName

function myFunction() {
  let carName = "Volvo"; // [var, let, const] All of them can be used.
  // code here CAN use carName
}

// code here can NOT use carName
```

#### Global

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

#### \* Global vs. Function

When you have both global and local variables with the same name, the local variable takes precedence over the global variable.

```js
var someVar = "Hat";

function myFun() {
  var someVar = "Head";
  return someVar; // "Head"
}
```



### Operators

#### `==` vs. `===`

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

#### `!=` vs. `!==`

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

#### `>`, `>=`

Like the `==` operator, these operators will convert data types of values while comparing.

```js
5 > '3' // true
7 >= '3' // true
```



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



### JSON

JavaScript Object Notation



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