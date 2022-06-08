# TypeScript

## Why use TypeScript?

### Static type-checking

A static type-checker like TypeScript helps us find bugs before our code runs. It uses static type systems that describe the shapes and behaviors of what our values will be when we run our programs and tells us when things might be going off the rails.

```js
const message = "hello!";
 
message();
// This expression is not callable.
// Type 'String' has no call signatures.
```

### Non-exception failures

You could imagine that accessing a property that doesn’t exist on an object should throw an error too. Instead, JavaScript gives us different behavior and returns the value `undefined`:

```js
const user = {
  name: "Daniel",
  age: 26,
};

user.location; // returns undefined
```

In TypeScript, the code produces an error about `location` not being defined.

TypeScript catches a lot of legitimate bugs:

typos,

```js
const announcement = "Hello World!";
 
// How quickly can you spot the typos?
announcement.toLocaleLowercase();
announcement.toLocalLowerCase();
 
// We probably meant to write this...
announcement.toLocaleLowerCase();
```

uncalled functions,

```js
function flipCoin() {
  // Meant to be Math.random()
  return Math.random < 0.5;
Operator '<' cannot be applied to types '() => number' and 'number'.
}
```

Basic logic errors,

```js
const value = Math.random() < 0.5 ? "a" : "b";
if (value !== "a") {
  // ...
} else if (value === "b") {
This condition will always return 'false' since the types '"a"' and '"b"' have no overlap.
  // Oops, unreachable
}
```



## Types

### Arrays

`type[]` 형식으로 작성하면 된다(e.g. `number[]`, `string[]`).

`Array<type>` 형식도 가능하다.

### `any`

When a value is of type `any`, type checking error doesn't occur in any circumstances.

```typescript
let obj: any = { x: 0 };
// None of the following lines of code will throw compiler errors.
// Using `any` disables all further type checking, and it is assumed 
// you know the environment better than TypeScript.
obj.foo();
obj();
obj.bar = 100;
obj = "hello";
const n: number = obj;
```

### Functions

#### Parameters

```typescript
function greet(name: string) {
  console.log("Hello, " + name.toUpperCase() + "!!");
}

greet(42);
// Argument of type 'number' is not assignable to parameter of type 'string'.
```

#### Return value

```typescript
function getFavoriteNumber(): number {
  return 26;
}
```

#### Anonymous functions

When a function appears in a place where TypeScript can determine how it’s going to be called, the parameters of that function are automatically given types:

```typescript
// No type annotations here, but TypeScript can spot the bug
const names = ["Alice", "Bob", "Eve"];
 
// Contextual typing for function
names.forEach(function (s) {
  console.log(s.toUppercase());
});
// Property 'toUppercase' does not exist on type 'string'. Did you mean 'toUpperCase'?
```

This process is called *contextual typing* because the *context* that the function occurred within informs what type it should have.

----

### Objects

To define an object type, we simply list its properties and their types. You can use `,` or `;` to separate the properties, and the last separator is optional either way. The type part of each property is also optional. If you don’t specify a type, it will be assumed to be `any`.

```typescript
// The parameter's type annotation is an object type
function printCoord(pt: { x: number; y: number }) {
  console.log("The coordinate's x value is " + pt.x);
  console.log("The coordinate's y value is " + pt.y);
}

printCoord({ x: 3, y: 7 });
```

#### Optional properties

Object types can also specify that some or all of their properties are *optional*. To do this, add a `?` after the property name:

```typescript
function printName(obj: { first: string; last?: string }) {
  // ...
}
// Both OK
printName({ first: "Bob" });
printName({ first: "Alice", last: "Alisson" });
```

When you *read* from an optional property, you’ll have to check for `undefined` before using it.

```typescript
function printName(obj: { first: string; last?: string }) {
  if (obj.last !== undefined) {
    // OK
    console.log(obj.last.toUpperCase());
  }
 
  // A safe alternative using modern JavaScript syntax:
  console.log(obj.last?.toUpperCase());
}
```

----

### `null` and `undefined`

TypeScript has two corresponding *types* by the same names. How these types behave depends on whether you have the `strictNullChecks` option on.

#### `strictNullChecks` on

You will need to test for those values before using methods or properties on that value. Just like checking for `undefined` before using an optional property, we can use *narrowing* to check for values that might be `null`:

```typescript
function doSomething(x: string | null) {
  if (x === null) {
    // do nothing
  } else {
    console.log("Hello, " + x.toUpperCase());
  }
}
```

#### Non-null Assertion Operator (Postfix`!`)

Writing `!` after any expression is effectively a type assertion that the value isn’t `null` or `undefined`:

```typescript
function liveDangerously(x?: number | null) {
  // No error
  console.log(x!.toFixed());
}
```



## How to use

### `tsc`, the TypeScript compiler

To install:

```bash
npm install -g typescript
```

By running the command `tsc`, you can type-check the `ts` file and convert it to `js` file:

```bash
tsc foo.ts
```

#### Erased types

When we compile the above function `greet` with `tsc`, the output is:

```js
"use strict";
function greet(person, date) {
    console.log("Hello ".concat(person, ", today is ").concat(date.toDateString(), "!"));
}
greet("Maddison", new Date());
```

Type annotations aren’t part of JavaScript (or ECMAScript to be pedantic), so there really aren’t any browsers or other runtimes that can just run TypeScript unmodified. Most TypeScript-specific code gets erased away, and likewise, here our type annotations were completely erased.


#### Downleveling

One other difference from the above was that our template string was rewritten from

```tsx
`Hello ${person}, today is ${date.toDateString()}!`;
```

to

```js
"Hello " + person + ", today is " + date.toDateString() + "!";
```

Template strings are a feature from a version of ECMAScript called ECMAScript 2015 (a.k.a. ECMAScript 6, ES2015, ES6, etc. - *don’t ask*). TypeScript has the ability to rewrite code from newer versions of ECMAScript to older ones such as ECMAScript 3 or ECMAScript 5 (a.k.a. ES3 and ES5). This process of moving from a newer or “higher” version of ECMAScript down to an older or “lower” one is sometimes called *downleveling*.

Default target is ES3. You can specify a version by `--target` option.

#### Options
##### `noEmitOnError`

`tsc`로 컴파일 시, 아무 옵션을 주지 않을 경우, type error가 발생해도 `js`파일을 생성해낸다. 에러가 있을 경우 `js`파일을 생성하지 않도록 하기 위해선 `noEmitOnError` 옵션을 주면 된다.

```bash
tsc --noEmitOnError foo.ts
```

##### Strictness

TypeScript has several type-checking strictness flags that can be turned on or off. The strict flag in the CLI, or `"strict": true` in `tsconfig.json` toggles them all on simultaneously, but we can opt out of them individually.

###### `noImplicitAny`

Turning on this flag will issue an error on any variables whose type is implicitly inferred as `any`.

###### `strictNullChecks`

Forgetting to handle `null` and `undefined` is the cause of countless bugs in the world. This flag makes handling `null` and `undefined` more explicit, and *spares* us from worrying about whether we *forgot* to handle `null` and `undefined`.

----

### Explicit types

TS를 사용해 변수의 타입을 명시적으로 지정할 수 있다.

```tsx
function greet(person: string, date: Date) {
  console.log(`Hello ${person}, today is ${date.toDateString()}!`);
}

let myName: string = "Alice";
```

We don’t always have to write explicit type annotations. In many cases, TypeScript can even just *infer* (or “figure out”) the types for us even if we omit them.

```tsx
let msg = "hello there!";
// let msg: string 으로 자동으로 인식한다.
```

Even though we didn’t tell TypeScript that `msg` had the type `string` it was able to figure that out. That’s a feature, and it’s best not to add annotations when the type system would end up inferring the same type anyway.

### Union types

TypeScript’s type system allows you to build new types out of existing ones using a large variety of operators.

```typescript
function printId(id: number | string) {
  console.log("Your ID is: " + id);
}
// OK
printId(101);
// OK
printId("202");
// Argument of type '{ myID: number; }' is not assignable to parameter of type 'string | number'.
printId({ myID: 22342 });
```

TypeScript will only allow an operation if it is valid for *every* member of the union. For example, if you have the union `string | number`, you can’t use methods that are only available on `string`:

```typescript
function printId(id: number | string) {
  console.log(id.toUpperCase());
  // Property 'toUpperCase' does not exist on type 'string | number'.
  //   Property 'toUpperCase' does not exist on type 'number'.
}
```

The solution is to *narrow* the union with code. For example, TypeScript knows that only a `string` value will have a `typeof` value `"string"`:

```typescript
function printId(id: number | string) {
  if (typeof id === "string") {
    // In this branch, id is of type 'string'
    console.log(id.toUpperCase());
  } else {
    // Here, id is of type 'number'
    console.log(id);
  }
}
```

Notice that in the `else` branch, we don’t need to do anything special - if `id` wasn’t a `string`, then it must have been a `number`.

If every member in a union has a property in common, you can use that property without narrowing:

```typescript
// Return type is inferred as number[] | string
function getFirstThree(x: number[] | string) {
  return x.slice(0, 3);
}
```

### Type aliases

You can reuse types by a type alias. A *type alias* is a *name* for any *type*.

```typescript
type Point = {
  x: number;
  y: number;
};
 
// Exactly the same as the earlier example
function printCoord(pt: Point) {
  console.log("The coordinate's x value is " + pt.x);
  console.log("The coordinate's y value is " + pt.y);
}
 
printCoord({ x: 100, y: 100 });
```

You can actually use a type alias to give a name to any type at all, not just an object type.

```typescript
type ID = number | string;
```

### Interfaces

An *interface declaration* is another way to name an object type:

```typescript
interface Point {
  x: number;
  y: number;
}
 
function printCoord(pt: Point) {
  console.log("The coordinate's x value is " + pt.x);
  console.log("The coordinate's y value is " + pt.y);
}
 
printCoord({ x: 100, y: 100 });
```

#### Type aliases vs Interfaces

Almost all features of an `interface` are available in `type`, the key distinction is that a type cannot be re-opened to add new properties vs an interface which is always extendable.

If you would like a heuristic, use `interface` until you need to use features from `type`.

##### Extend

Both can be extended, but the syntax differs.

```typescript
type BirdType = {
  wings: 2;
};

interface BirdInterface {
  wings: 2;
}

// Extend

type Owl = { nocturnal: true } & BirdType;
type Robin = { nocturnal: false } & BirdInterface;

interface Peacock extends BirdType {
  colourful: true;
  flies: false;
}
interface Chicken extends BirdInterface {
  colourful: false;
  flies: false;
}
```

##### Declaration merging

You can extend an interface by declaring it a second time, but can't with type alias.

```typescript
interface Kitten {
  purrs: boolean;
}

interface Kitten {
  colour: string;
}

type Puppy = {
  color: string;
};

type Puppy = {
  toys: number;
};
// Error: Duplicate identifier 'Puppy'.
```

##### Other types

Unlike an interface, the type alias can also be used for other types such as primitives, unions, and tuples.

```typescript
// primitive
type Name = string;

// object
type PartialPointX = { x: number; };
type PartialPointY = { y: number; };

// union
type PartialPoint = PartialPointX | PartialPointY;

// tuple
type Data = [number, string];
```

##### References

[TypeScript 공식문서](https://www.typescriptlang.org/play?#code/PTAEBUAsFMCdtAQ3qALgdwPagLaIJYB2ammANgM4mgAm0AxmcgqjKBZIgA4KYBmSQgFgAUCFCYARgCsGqAFygiqOH0T1oVRIRpoAnjyRl8iCpoB0okFbBRoepCgBucBxXw58TWABpBuvkxYNDYcTApUUHpMHDDielNNGyR6SNYECkQcaEsRUVQDBAAhfFgacELQAF5QAG9RUFB0IgBzCkUAJgBuUQBfHryRZVV1YtKaAElCFVg1DTqGptb20G6+0VFowgjQSXGARkUSsorDGtqlwjbO0H7NzG3IvbKOo-GpmbmEc8vr1duBskigxEABXMwQQoAZXosHwXEi+C07FQsFBqVBsEQZH0hgoegi0BwPmS+FQAHIqFxwu5JGQWNhhrBPAAPELQUqgcEMzC5e6PXbjADMbzKHxG8xqzxo+0BYlsMAckkwrHYoK41NgkWgLJUOlaEnSwSZXy0OlxFmSpwQ2JMZioNGwrCRoCcJiU0zgZlS+AeFoofnQkC80FJntmoyonBcSFAAGt7FgynyRAVDAB5dA4n6ETAY2CEbGKVGghC9UAAMlAx3KhQGaYQACUpERqnVQLn84WyIo1JQy5Xq+9w185SbRqAAArQdR5uOgHV6mhUGvWhYiRrRMiYTF8UE9tBo6ADRp8YyaXvYswDXqicfzADCwfoCeIi+gOhXw8+E-qG6i5A7rM+6Xv2J6gGe+AXhBV7Husgz0pEmBZoombZu2zRXCsHR+J2qCYt2xZHgCoiIVEz6vooT74C+H5thcmF-DhAHbruIEwf2fiQdBfYQncgziFAiCRJk+A0IGCDwNEsQfroeg7lyEL3poEguMEDbJLaiQUOYoBQjw9D4HwNHYmQeh+JIILcqA8mgksZA4i00BPM5MwLrAsBBMk2QUJkTk6aAEwCLZoCQJgamqXA7IQeQ26Me5nmwAGNkKQkwjyuw0AIGF6CQjwMJwgiUTaKAXCeW6dBoF6UXaLoYQoIE9DcjQ3maH5KlBnRSZxgazSqspVDGAmoDUbRhApsh6H0BRH4DNNNGvm2k1yuI6aEAgeDSEEtBGXwcAfvMlkYFlxANkYdoqU4VADZpKCsMJHo-hoWgoJgPDELVFrndpjgIIw4TQDQuSCcGVDZNoVAhWlC66rJgiPRKCCSA4dCMMgBpkppmVbLoqAeDkGxDCOE4ANJknq66NFwmJJYoyrkDOhA3oTymgGTqAU3+m6AZiigRHCVzMwJYBTNFKowMECQQogX1pbmLnkdoTm6DuqDuJV-CkmrtAMN4wm+uNhNnZO6pcA45yLFuQR86irQ3nKxum+blMkASiiEKCOCWbA9uE+IAAi0DvTQBp+rZwQtJgV5+M6Dq7fthDzNE+66JZSDJNS7h4zG20y+tLT6y4ukABLIdAEWBME1N0jRZkw5ngPJA2yVkpSsZHW5CQOdQeDDekODw8pKaretEgCOkuyaJE8AUEBz0xcEZgclcRg4vw0WA05yRSypyA7uazeutdxPPTHoMouo87haocVN5A8CILoLoy5HmC6FwTDzKg2ARMgCh+2ASAHMuDtBAL-F819ZhxXMNJYAABHUsEQDYUGAEKAA7B0IU6ChQAFZgDN1hPCVAABaAaxCrrEObsAHBHQABsAAODoTCAAMABiGhDCmEdGYaIIAA)

[Interfaces vs Types in TypeScript](https://stackoverflow.com/questions/37233735/interfaces-vs-types-in-typescript)

----

### Type assertions

Sometimes you will have information about the type of a value that TypeScript can’t know about. In this situation, you can use a *type assertion* to specify a more specific type:

```typescript
const myCanvas = document.getElementById("main_canvas") as HTMLCanvasElement;
```

This rule prevents “impossible” coercions like:

```typescript
const x = "hello" as number;
// Conversion of type 'string' to type 'number' may be a mistake because neither type sufficiently overlaps with the other. If this was inte
```

### Literal types

```typescript
let x: "hello" = "hello";
// OK
x = "hello";
// Type '"howdy"' is not assignable to type '"hello"'.
x = "howdy";
```

It’s not much use to have a variable that can only have one value!

But by *combining* literals into unions, you can express a much more useful concept - for example, functions that only accept a certain set of known values:

```typescript
function printText(s: string, alignment: "left" | "right" | "center") {
  // ...
}
printText("Hello, world", "left");
printText("G'day, mate", "centre");
// Argument of type '"centre"' is not assignable to parameter of type '"left" | "right" | "center"'.
```

```typescript
function compare(a: string, b: string): -1 | 0 | 1 {
  return a === b ? 0 : a > b ? 1 : -1;
}
```

You can combine these with non-literal types:

```typescript
interface Options {
  width: number;
}
function configure(x: Options | "auto") {
  // ...
}
configure({ width: 100 });
configure("auto");
configure("automatic");
// Argument of type '"automatic"' is not assignable to parameter of type 'Options | "auto"'.
```

#### Literal interface

```typescript
const req = { url: "https://example.com", method: "GET" };
handleRequest(req.url, req.method);
// Argument of type 'string' is not assignable to parameter of type '"GET" | "POST"'.
```

In the above example `req.method` is inferred to be `string`, not `"GET"`. Because code can be evaluated between the creation of `req` and the call of `handleRequest` which could assign a new string like `"GUESS"` to `req.method`, TypeScript considers this code to have an error.

There are two ways to work around this.

1. You can change the inference by adding a type assertion in either location:

   ```typescript
   // Change 1:
   const req = { url: "https://example.com", method: "GET" as "GET" };
   // Change 2
   handleRequest(req.url, req.method as "GET");
   ```

2. You can use `as const` to convert the entire object to be type literals:

   ```typescript
   const req = { url: "https://example.com", method: "GET" } as const;
   handleRequest(req.url, req.method);
   ```

   The `as const` suffix acts like `const` but for the type system, ensuring that all properties are assigned the literal type instead of a more general version like `string` or `number`.
