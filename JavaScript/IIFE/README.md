# IIFE(Immediately Invoked Function Expression)

A common pattern in JavaScript is to execute a function as soon as it is declared:

```js
(function () {
  console.log("Chirp, chirp!");
})();  // Chirp, chirp!
```

Note that the function has no name and is not stored in a variable. The two parentheses `()` at the end of the function expression cause it to be immediately executed or invoked.

## module

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

