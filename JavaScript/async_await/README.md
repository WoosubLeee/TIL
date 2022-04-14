# async/await

## The async keyword

You put it in front of a function declaration to turn it into an **async fucntion**. An async function is a function that knows how to expect the possibility of the `await` keyword being used to invoke asynchronous code.

```js
async function hello() { return "Hello" };
let hello = async function() { return "Hello" };
let hello = async () => { return "Hello" };
```

Invoking the function returns a promise. Async functions' return values are guaranteed to be converted to promises.

Since it's returning a promise, we could use a `.then()` block.

```js
hello().then((value) => console.log(value))
hello().then(console.log)
```

## The await keyword

`await` only works inside async functions within regular JS code, however it can be used on its own with JS modules. `await` can be put in front of any async promise-based function to pause your code on that line until the promise fulfills, then return the resulting value.

```js
async function hello() {
  return greeting = await Promise.resolve("Hello");
};

hello().then(alert);
```

