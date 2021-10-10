# Inheritance

## How to inherit from a `supertype`

To make an instance of the `supertype` (or parent). You already know one way to create an instance of `Animal` using the `new` operator:

```js
let animal = new Animal();
```

There are some disadvantages when using this syntax for inheritance, which are too complex. Instead, here's an alternative approach without those disadvantages:

```js
let animal = Object.create(Animal.prototype);
```

`Object.create(obj)` creates a new object, and sets `obj` as the new object's `prototype`. Recall that the `prototype` is like the "recipe" for creating an object. By setting the `prototype` of `animal` to be the `prototype` of `Animal`, you are effectively giving the `animal` instance the same "recipe" as any other instance of `Animal`.

```js
animal instanceof Animal;
```

The `instanceof` method here would return `true`.

### Set the child's `prototype` to an instance of the parent

```js
Bird.prototype = Object.create(Animal.prototype);
Bird.prototype.constructor = Bird;
```

All instances of `Bird` should show that they were constructed by `Bird` and not `Animal`. To do so, you should manually set the constructor property of `Bird` to the `Bird` object.

#### Override inherited method

It's done by adding a method to child object's `prototype` using the same method name.

```js
function Animal() { }
Animal.prototype.eat = function() {
  return "nom nom nom";
};
function Bird() { }

Bird.prototype = Object.create(Animal.prototype);

Bird.prototype.eat = function() {
  return "peck peck peck";
};
```

JS looks for the method on the `prototype` chain:

1. `duck` => Is `eat()` defined here? No.
2. `Bird` => Is `eat()` defined here? => Yes. Execute it and stop searching.
3. `Animal` => `eat()` is also defined, but JavaScript stopped searching before reaching this level.
4. Object => JavaScript stopped searching before reaching this level.