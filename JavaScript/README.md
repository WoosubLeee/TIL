# JavaScript

##### 8 data types

1. `undefined`
2. `null`
3. `boolean`
4. `string`
5. `symbol`
6. `bigint`
7. `number`
8. `object`

##### Declare variables

```js
var variableA;
const variableB;
```

##### Assignment

```js
variableA = 10;
var variableB = 10;
```

#### String

##### Escape sequences

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

##### Index

Bracket notation을 사용한다.

```js
var firstName = 'Charles';
console.log(firstName[0]) // C
```

##### Immutability

```js
var myStr = "Bob";
myStr[0] = "J";
// Job으로 바뀌지 않는다.
```

