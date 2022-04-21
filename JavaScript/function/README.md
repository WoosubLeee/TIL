# Function

## Properties

### `arguments`

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

#### References

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments



## Methods

### `call()`, `apply()`, `bind()`

In JavaScript all functions are object methods. If a function is not a method of a JavaScript object, it is a function of the global object. With these methods, you can write a method that can be used on different objects.

#### `call()`

With `call()`, an object can use a method belonging to another object.

```js
const person = {
  fullName: function() {
    return this.firstName + " " + this.lastName;
  }
}
const person1 = {
  firstName:"John",
  lastName: "Doe"
}

// This will return "John Doe":
person.fullName.call(person1);
```

The `call()` method can accept arguments:

```js
const person = {
  fullName: function(city, country) {
    return this.firstName + " " + this.lastName + "," + city + "," + country;
  }
}

const person1 = {
  firstName:"John",
  lastName: "Doe"
}

person.fullName.call(person1, "Oslo", "Norway");
```

#### `apply()`

The `apply()` method is similar to the `call()` method.

```js
const person = {
  fullName: function() {
    return this.firstName + " " + this.lastName;
  }
}

const person1 = {
  firstName: "Mary",
  lastName: "Doe"
}

// This will return "Mary Doe":
person.fullName.apply(person1);
```

##### vs `call()`

The difference is:

The `call()` method takes arguments **separately**.
The `apply()` method takes arguments as an **array**.

```js
const person = {
  fullName: function(city, country) {
    return this.firstName + " " + this.lastName + "," + city + "," + country;
  }
}

const person1 = {
  firstName:"John",
  lastName: "Doe"
}

person.fullName.apply(person1, ["Oslo", "Norway"]);
```

***

#### `bind()`

With the `bind()` method, an object can borrow a method from another object. It creates a new function that has its `this` keyword set to the provided value, with a given sequence of arguments preceding any provided when the new function is called.

```js
const person = {
  firstName:"John",
  lastName: "Doe",
  fullName: function () {
    return this.firstName + " " + this.lastName;
  }
}

const member = {
  firstName:"Hege",
  lastName: "Nilsen",
}

let fullName = person.fullName.bind(member);
```

##### Preserving `this`

Sometimes the `bind()` method has to be used to prevent loosing **this**. This example will try to display the person name after 3 seconds, but it will display **undefined** instead:

```js
const person = {
  firstName:"John",
  lastName: "Doe",
  display: function () {
    let x = document.getElementById("demo");
    x.innerHTML = this.firstName + " " + this.lastName;
  }
}

setTimeout(person.display, 3000);
```

In the following example, the `bind()` method is used to bind person.display to person. This example will display the person name after 3 seconds:

```js
const person = {
  firstName:"John",
  lastName: "Doe",
  display: function () {
    let x = document.getElementById("demo");
    x.innerHTML = this.firstName + " " + this.lastName;
  }
}

let display = person.display.bind(person);
setTimeout(display, 3000);
```

***

#### `call()` vs `apply()` vs `bind()`

- *Call* invokes the function and allows you to pass in arguments one by one.
- *Apply* invokes the function and allows you to pass in arguments as an array.
- *Bind* returns a new function, allowing you to pass in a this array and any number of arguments.

#### References

https://www.w3schools.com/js/js_function_bind.asp

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_objects/Function/bind

https://stackoverflow.com/questions/15455009/javascript-call-apply-vs-bind



## Closure

A **closure** is the combination of a function bundled together (enclosed) with references to its surrounding state (the **lexical environment**). In other words, a closure gives you access to an outer function's scope from an inner function.

### Lexical scoping

**Lexical Scoping** defines how variable names are resolved in nested functions.

```js
function outerFunc() {
  var x = 10;
  var innerFunc = function () { console.log(x); };
  innerFunc();
}

outerFunc(); // 10
```

위 함수를 살펴보자. 함수 `outerFunc` 내에서 내부함수 `innerFunc`가 선언되고 호출되었다. 이때 내부함수 `innerFunc`는 자신을 포함하고 있는 외부함수 `outerFunc`의 변수 x에 접근할 수 있다. 이는 함수 `innerFunc`가 함수 `outerFunc`의 내부에 선언되었기 때문이다. 또, `innerFunc`는 `outerFunc` 바깥에 선언된 변수(global 변수 포함)에도 접근할 수 있다.

여기서 global scope, `outerFunc`'s scope, 자신의 스코프 모두가 lexical scope 가 된다. lexical scope는 함수를 호출할 때가 아니라 선언할 때 결정된다. 

### Then what is closure?

Lexical scoping 의 정의에서 한 문장이 추가된다. 추가된 문장이 closure의 핵심이다.

**Lexical Scoping** defines how variable names are resolved in nested functions: **inner functions contain the scope of parent functions even if the parent function has returned**.

closure가 무엇인지 더 명확하게 알기 위해 이번에는 내부함수 `innerFunc`를 함수 `outerFunc` 내에서 호출하는 것이 아니라 반환하도록 변경해 보자.

```js
function outerFunc() {
  var x = 10;
  var innerFunc = function () { console.log(x); };
  return innerFunc;
}

/**
 *  함수 outerFunc를 호출하면 내부 함수 innerFunc가 반환된다.
 *  그리고 함수 outerFunc의 실행 컨텍스트는 소멸한다.
 */
var inner = outerFunc();
inner(); // 10
```

함수 `outerFunc`는 내부함수 `innerFunc`를 반환하고 생을 마감했다. 하지만 변수 `inner`는 여전히 변수 `x`의 값에 접근을 할 수 있다. 그것은 내부함수 `innerFunc`가 함수가 선언될 때의 lexical environment를 기억하여 변수도 기억하고 있기 때문이다.

즉, **클로저는 반환된 내부함수가 자신이 선언됐을 때의 환경(lexical environment)인 스코프를 기억하여 자신이 선언됐을 때의 환경(스코프) 밖에서 호출되어도 그 환경(스코프)에 접근할 수 있는 함수**를 말한다. 이를 조금 더 간단히 말하면 **클로저는 자신이 생성될 때의 환경(lexical environment)을 기억하는 함수다**라고 말할 수 있겠다.

#### References

[What is lexical scope?](https://stackoverflow.com/questions/1047454/what-is-lexical-scope)

### Usages

클로저는 자신이 생성될 때의 환경(lexical environment)을 기억해야 하므로 메모리 차원에서 손해를 볼 수 있다. 하지만 클로저는 자바스크립트의 강력한 기능으로 이를 적극적으로 사용해야 한다.

#### 상태 유지

클로저가 가장 유용하게 사용되는 상황은 **현재 상태를 기억하고 변경된 최신 상태를 유지**하는 것이다.

```js
var toggle = (function () {
  var isShow = false;

  // ① 클로저를 반환
  return function () {
    box.style.display = isShow ? 'block' : 'none';
    // ③ 상태 변경
    isShow = !isShow;
  };
})();

document.querySelector('.toggleBtn').onclick = toggle;
```

변수 `toggle`의 IIFE는 함수를 반환하고 즉시 소멸한다. IIFE의 변수 `isShow`도 같이 소멸됐지만 반환된 함수(closure)는 이 변수를 기억하고 있다. 따라서 이 closure를 제거하지 않는 한 변수 `isShow`는 소멸되지 않고 계속 상태가 유지된다.

#### 전역 변수의 사용 억제

```js
var counter = 0;

function increase() {
  return ++counter;
}

incleaseBtn.onclick = function () {
  count.innerHTML = increase();
};
```

여기서 변수 `counter`는 함수 `increase`를 통해서만 조작되는 것을 의도했겠으나, 전역 변수이기 때문에 언제든지 누구나 접근할 수 있고 변경할 수 있다. closure를 통해 의도치 않은 상태 변경을 방지할 수 있다.

```js
var increase = (function () {
  // 카운트 상태를 유지하기 위한 자유 변수
  var counter = 0;
  // 클로저를 반환
  return function () {
    return ++counter;
  };
}());
```

#### 정보의 은닉

```js
function Counter() {
  // 카운트를 유지하기 위한 자유 변수
  var counter = 0;

  // 클로저
  this.increase = function () {
    return ++counter;
  };

  // 클로저
  this.decrease = function () {
    return --counter;
  };
}

const counter = new Counter();
```

변수 `counter`는 생성자 함수 `Counter` 외부에서 접근할 수 없다. 이러한 closure의 특징을 사용해 클래스 기반 언어의 `private` 키워드를 흉내낼 수 있다.

### References

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures

[클로저](https://poiemaweb.com/js-closure)



## Generator

The `Generator` object is returned by a [generator function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*) and it conforms to both the iterable protocol and the iterator protocol. A generator function is the **`function*`** declaration (`function` keyword followed by an asterisk).

```js
function* generator() {
  yield 1;
  yield 2;
  yield 3;
}

const gen = generator(); // "Generator { }"

console.log(gen.next().value); // 1
console.log(gen.next().value); // 2
console.log(gen.next().value); // 3
```

### `yield`

The `yield` keyword pauses generator function execution and the value of the expression following the `yield` keyword is returned to the generator's caller. It can be thought of as a generator-based version of the `return` keyword.

The `yield` keyword causes the call to the generator's `next()` method to return an `IteratorResult` object

#### Syntax

```js
[rv] = yield [expression]
```

- `expression` : Defines the value to return from the generator function via the iterator protocol. If omitted, `undefined` is returned instead.
- `rv` : Retrieves the optional value passed to the generator's `next()` method to resume its execution.

***

### References

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator
