# Function

## `arguments`

**`arguments`** is an `Array`-like object accessible inside functions that contains the values of the arguments passed to that function. The `arguments` object is a local variable available within all non-arrow functions.

```js
function func1(a, b, c) {
  console.log(arguments[0]);
  console.log(arguments[1]);
  console.log(arguments[2]);
}

func1(1, 2, 3);
// 1
// 2
// 3
```

The `arguments` object is not an `Array`. It is similar, but lacks all `Array` properties except `length`.

To convert to a real `Array`:

```js
let args = [...arguments];
```



## References

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments

