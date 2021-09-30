# `Object`

You access the data in `objects` through what are called `properties`. You can also use numbers as properties in addition to strings. You can even omit the quotes for single-word string properties.

```js
var anotherObject = {
  make: "Ford",
  5: "five",
  "model": "focus"
};
```



## Accessing `object` properties

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

### `this`

`this` refers to the object itself.

```js
let duck = {
  name: "Aflac",
  numLegs: 2,
  sayName: function() {
    return this.name;
  }
};

console.log(duck.sayName());  // 'Aflac'
```



## Deleting properties

```js
delete object.property;
delete object["property"];
```



## Testing `objects` for properties

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



## Iterating through the keys of an object

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



## Constructor

Constructors are functions that create new objects. They define properties and behaviors that will belong to the new object.

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



## `instanceof`

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



## `.prototype`

Properties in the `prototype` are shared among ALL instances of an object.

```js
Bird.prototype.numLegs = 2;

console.log(duck.numLegs);  // 2
console.log(canary.numLegs);  // 2
```

