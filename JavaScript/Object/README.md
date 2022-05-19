# `Object`

You access the data in `objects` through what are called `properties`. You can also use numbers as properties in addition to strings. You can even omit the quotes for single-word string properties.

```js
var anotherObject = {
  make: "Ford",
  5: "five",
  "model": "focus"
};
```



## Properties

### How to use

#### Accessing

You can use **1. dot notation** or **2. bracket notation** to access object properties.

```js
var myObj = {
  "Space Name": "Kirk",
  "More Space": "Spock",
  "NoSpace": "USS Enterprise"
};
myObj.NoSpace;  // "USS Enterprise"
myObj["Space Name"];  // "Kirk"
```

#### Deleting

```js
delete object.property;
delete object["property"];
```

#### Testing

We could check for its presence in either of the following ways:

```js
var myObj = {
  top: "hat",
  bottom: "pants"
};
myObj.hasOwnProperty("top");  // true
myObj.hasOwnProperty("middle");  // false

"top" in myObj;  // true
"middle" in myObj;  // false
```

----

### Computed property

ES6 allows you to use an expression in brackets `[]`. It’ll then use the result of the expression as the property name of an object.

```js
let propName = 'c';

const rank = {
  a: 1,
  b: 2,
  [propName]: 3,
};

console.log(rank.c); // 3
```

[JavaScript Computed Property](https://www.javascripttutorial.net/es6/javascript-computed-property)



## `.keys()`

We can also generate an array which contains all the keys stored in an object using the `Object.keys()` method and passing in an object as the argument. This will return an array with strings representing each property in the object.

```js
let users = {
  Alan: {
    age: 27,
    online: false
  },
  Jeff: {
    age: 32,
    online: true
  }
};

console.log(Object.keys(users));  // ['Alan', 'Jeff']
```

### Iterating through the keys of an object

```js
var users = {
  Alan: {
    online: false
  },
  Jeff: {
    online: true
  },
  Sarah: {
    online: false
  }
}

for (let user in users) {
  console.log(user);  // 'Alan', 'Jeff', 'Sarah'
}
```



## Constructor

Constructors are functions that create new objects. They define properties(called **own properties**) and behaviors that will belong to the new object.

```js
function Bird(name) {
  this.name = name;
  this.color = 'blue';
  this.numLegs = 2;
}

let blueBird = new Bird('Albert');
```

Constructors follow a few conventions:

- Constructors are defined with a capitalized name to distinguish them from other functions that are not constructors.
- They use `this` keyword that refers to the new object it will create.
- Constructors define properties and behaviors instead of returning a value as other functions might.

### `new`

The `new` keyword does the following things:

1. Creates a blank, plain JS object, inheriting `Bird.prototype` (By adding a property `__proto__`)
2. Binds the newly created object instance as the `this` context (i.e. all references to `this` in the constructor function now refer to the object created in the first step).
3. `return` 값이 없거나, primitive 값을 `return` 하면 위의 `this`가 반환되고,
   object를 `return`하면 해당 object가 반환된다.

#### References

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new

https://ko.javascript.info/constructor-new

----

### `instanceof`

`instanceof` allows you to compare an object to a constructor, return boolean value based on whether or not that object was created with the constructor.

```js
let Bird = function(name, color) {
  this.name = name;
  this.color = color;
  this.numLegs = 2;
}

let crow = new Bird("Alexis", "black");

crow instanceof Bird;  // true
```

### `.constructor`

It's a reference to the constructor function that created the instance.

```js
let duck = new Bird();
let beagle = new Dog();

console.log(duck.constructor === Bird);  // true
console.log(beagle.constructor === Dog);  // true
```



## Mixin

Object behavior can be shared through inheritance. However, there are cases when inheritance is not the best solution. Inheritance does not work well for unrelated objects like `Bird` and `Airplane`. They can both fly, but a `Bird` is not a type of `Airplane` and vice versa.

For unrelated objects, it's better to use mixins. A mixin allows other objects to use a collection of functions.

```js
let flyMixin = function(obj) {
  obj.fly = function() {
    console.log("Flying, wooosh!");
  }
};
```

```js
let bird = {
  name: "Donald",
};

let plane = {
  model: "777",
};

flyMixin(bird);
flyMixin(plane);

bird.fly();  // Flying, wooosh!
plane.fly();  // Flying, wooosh!
```

