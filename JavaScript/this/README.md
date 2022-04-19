# JavaScript `this`

A property of an execution context (global, function or eval) that, in non–strict mode, is always a reference to an object and in strict mode can be any value. The `this` keyword refers to different objects depending on how it is used:

- in an object method : the object

  ```js
  const person = {
    firstName: "John",
    lastName : "Doe",
    id       : 5566,
    fullName : function() {
      return this.firstName + " " + this.lastName;  // this refers to the 'person' object
    }
  };
  ```

- alone : global object. In a browser window the global object is `[object Window]`

  ```js
  let x = this;  // this refers to the global object
  ```

- in a function

  - not strict mode : global object

    ```js
    function myFunction() {
      return this;  // this refers to the global object
    }
    ```

  - strict mode : undefined

    ```js
    "use strict";
    function myFunction() {
      return this;  // this refers to undefined
    }
    ```

- in an event : element that received the event.

  ```html
  <button onclick="this.style.display='none'">
    Click to Remove Me!
  </button>
  ```

- `call()`, `apply()`, `bind()` : any object

  ```js
  const person1 = {
    fullName: function() {
      return this.firstName + " " + this.lastName;
    }
  }
  
  const person2 = {
    firstName:"John",
    lastName: "Doe",
  }
  
  // Return "John Doe":
  person1.fullName.call(person2);  // this refers to 'person2' object
  ```



## `this` precedence

To determine which object `this` refers to; Use the following precedence of order.

1. `bind()`
2. `apply()`, `call()`
3. Object method
4. global scope



## References

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this

https://www.w3schools.com/js/js_this.asp