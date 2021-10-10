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

### Accessing

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

#### `this`

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

### Deleting

```js
delete object.property;
delete object["property"];
```

### Testing

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



## Closure

The simplest way to make property private is by creating a variable within the constructor function. This changes the scope of that variable to be within the constructor function versus available globally. This way, the variable can only be accessed and changed by methods also within the constructor function.

```js
function Bird() {
  let hatchedEgg = 10;  // 'let'!! not `this`!!

  this.getHatchedEggCount = function() { 
    return hatchedEgg;
  };
}
let ducky = new Bird();
ducky.getHatchedEggCount();
```

The private variable `hatchedEgg` can only be accessed by `getHatchedEggCount`.



## Immediately Invoked Function Expression(IIFE)

A common pattern in JavaScript is to execute a function as soon as it is declared:

```js
(function () {
  console.log("Chirp, chirp!");
})();  // Chirp, chirp!
```

Note that the function has no name and is not stored in a variable. The two parentheses `()` at the end of the function expression cause it to be immediately executed or invoked.

### module

IIFE is often used to group related functionality into a single object or module. We can group mixins into a module as follows:

```js
function glideMixin(obj) {
  obj.glide = function() {
    console.log("Gliding on the water");
  };
}
function flyMixin(obj) {
  obj.fly = function() {
    console.log("Flying, wooosh!");
  };
}

let motionModule = (function () {
  return {
    glideMixin: function(obj) {
      obj.glide = function() {
        console.log("Gliding on the water");
      };
    },
    flyMixin: function(obj) {
      obj.fly = function() {
        console.log("Flying, wooosh!");
      };
    }
  }
})();
```

Note that you have an immediately invoked function expression (IIFE) that returns an object `motionModule`. This returned object contains all of the mixin behaviors as properties of the object.

```js
motionModule.glideMixin(duck);
duck.glide();  // Gliding on the water
```

