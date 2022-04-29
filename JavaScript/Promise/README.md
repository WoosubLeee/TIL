# Promise

## Promise란?

Promise는 비동기 작업의 최종 완료 또는 실패를 나타내는 객체이다. It allows you to associate handlers with an asynchronous action's eventual success value or failure reason. This lets asynchronous methods return values like synchronous methods.

Promise has 3 states.

1. pending : initial state, neither fulfilled nor rejected.
2. fulfilled : meaning that the operation was completed successfully.
3. rejected : meaning that the operation failed.

![image-20210910014250085](README.assets/image-20210910014250085.png)

Using Promise comes with some guarantees:

- Callbacks added with `then()` will never be invoked before the completion of the current run of the JavaScript event loop.

- Multiple callbacks may be added by calling `then()` several times. They will be invoked one after another, in the order in which they were inserted.

### Using Promises

`Promise` is a constructor function, so you need to use the `new` keyword to create one. It takes a function, as its argument, with two parameters - `resolve` and `reject`. These are methods used to determine the outcome of the promise. The syntax looks like this:

```js
const myPromise = new Promise((resolve, reject) => {
  if (작업이 완료) {
    resolve("fulfilled");
  } else if (작업이 실패) {
    reject("rejected");
  }
});
```

The methods `promise.then()`, `promise.catch()`, and `promise.finally()` are used to associate further action with a promise that becomes settled.

The `.then()` method takes up to two arguments:

1. the first argument is a callback function for the resolved case of the promise
2. the second argument is a callback function for the rejected case.

Each `.then()` returns a newly generated promise object, which can optionally be used for chaining.

```js
myPromise
  .then((successMsg) => {  // successMsg == resolve의 parameter로 전달된 'fulfilled'
    console.log(successMsg);
  }, (rejectMsg) => {  // rejectMsg == reject의 parameter로 전달된 'rejected'
    console.log(rejectMsg);
  });

// 'fulfilled' if (value == true)
// 'rejected' if (value == false)
```

위의 경우는 `.then()`에서 rejected promise를 처리하도록 했지만, rejected promise를 처리하는 방법은 한 가지가 더 있다. `.then()`에는 resolved promise를 처리하는 함수만 두고 맨 마지막 `.catch()`에 error handling (rejected promise도 처리할 수 있는) 함수를 두는 것이다. 아래 코드는 위 코드와 같은 동작을 한다.

```js
myPromise
  .then((successMsg) => {
    console.log(successMsg);
  });
  .catch((rejectMsg) => {
    console.log(rejectMsg);
  });
```

가급적이면 아래의 `.catch()`를 사용하는 편이 더 좋은데, `.then()`에서 rejected promise를 처리하는 경우 `.catch()`문을 따로 두지 않는다면 `.then()` 안에서 일어나는 error는 처리할 수 없다는 단점이 있다. `.catch()`에서 rejected promise를 처리하는 경우 rejected promise와 error 둘 다 `.catch()`에서 처리할 수 있을 것이다. 

#### Chaining

기존의 callback을 활용한다면 다음과 같이 코드가 짜여질 것이다.

```js
doSomething(function(result) {
  doSomethingElse(result, function(newResult) {
    doThirdThing(newResult, function(finalResult) {
      console.log('Got the final result: ' + finalResult);
    }, failureCallback);
  }, failureCallback);
}, failureCallback);
```

promise chaing을 활용한다면 다음과 같이 바꿀 수 있다.

```js
doSomething()
.then(function(result) {
  return doSomethingElse(result);
})
.then(function(newResult) {
  return doThirdThing(newResult);
})
.then(function(finalResult) {
  console.log('Got the final result: ' + finalResult);
})
.catch(failureCallback);
```

`.then` chain에서는 Promise 객체가 없더라도 계속 이어서 다음 link로 이어서 실행한다. 중간에 reject 되는 경우 바로 `.catch`문으로 이동한다.

***

### References

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises

[자바스크립트 Promise 쉽게 이해하기](https://joshua1988.github.io/web-development/javascript/promise-for-beginners/)



## Methods

### `Promise.race()`

Returns a promise that fulfills or rejects as soon as one of the promises in an iterable fulfills or rejects, with the value or reason from that promise.

```js
const promise1 = new Promise((resolve, reject) => {
  setTimeout(resolve, 500, 'one');
});

const promise2 = new Promise((resolve, reject) => {
  setTimeout(resolve, 100, 'two');
});

Promise.race([promise1, promise2]).then((value) => {
  console.log(value);
  // Both resolve, but promise2 is faster
});
// expected output: "two"
```

### References

[Promise.race()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/race)

