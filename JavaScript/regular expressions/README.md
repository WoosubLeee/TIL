# Regular expressions

## What are regular expressions?

Regular expressions are patterns used to match character combinations in strings.



## Creating a regular expression

1. Regular expression literal : pattern enclosed between slashes.
2. Constructor function : `RegExp` object

```js
let re = /ab+c/;
let re = new RegExp('ab+c');
```



## Using regex in JS

### `.test()`

One way to test a regex. The `.test()` method takes the regex, applies it to a string and return boolean value.

```js
let testStr = "freeCodeCamp";
let testRegex = /Code/;
testRegex.test(testStr);  // true
```

### `.match()`

You can extract the actual matches.

```js
"Hello, World!".match(/Hello/);  // ["Hello"]
```



## Writing a regex pattern

### Simple pattern

Finds a direct match

```js
/abc/
```

Only finds `abc`, not `ab c` or `a bc`.

### Special characters

#### `|`

Match a literal string with different possibilities. You can search for multiple patterns.

```js
/yes|no/
```

You can search for `yes` or `no`.

#### `i`

Ignore case while matching.

```js
/ignorecase/i
```

This regex can match the strings `ignorecase`, `igNoreCase`, and `IgnoreCase`.

#### `g`

Find more than the first match.

```js
let testStr = "Repeat, Repeat, Repeat";
let ourRegex = /Repeat/;
testStr.match(ourRegex);  // ["Repeat", "Repeat", "Repeat"]
```

#### `.`

The wildcard character `.` will match any one character.

```js
let hugStr = "hug";
let huhStr = "huh";
let hutStr = "hut";
let huRegex = /hu./;
huRegex.test(humStr);  // true
huRegex.test(huhStr);  // true
hutStr.match(huRegex);  // ["hut"]
```

#### `[]`

Match single character with multiple possibilites. 

```js
let bigStr = "big";
let bagStr = "bag";
let bugStr = "bug";
let bogStr = "bog";
let bgRegex = /b[aiu]g/;
bigStr.match(bgRegex);  // ["big"]
bagStr.match(bgRegex);  // ["bag"]
bugStr.match(bgRegex);  // ["bug"]
bogStr.match(bgRegex);  // null
```

#### `-`

You can define a range of characters to match using a hyphen character: `-`.

```js
// [a-d]는 [abcd]와 같다
// [a-z]는 [abcdefghijklmnopqrstuvwxyz]와 같다
// [0-9]는 [0123456789]와 같다
```

But if the hyphen appears as the first or last character enclosed in the square brackets it is taken as a literal hyphen to be included in the character class as a normal character.

```js
let exStr = "non-profit";
let hypRegex = /[abcd-]/;
hypRegex.match(exStr);  // "-"
```

#### `^`

##### Inside a character set

Match single characters not specified. Negated character set, a set of characters that  you do not want to match.

```js
let exStr = "I love you much";
let vowelRegex = /[^aeiou]/gi;
exStr.match(vowelRegex);  // [' ', 'l', 'v', ' ', 'y', ' ', 'm', 'c', 'h']
```

##### Outside a character set

Match beginning string patterns.

```js
let firstRegex = /^Ricky/;
let firstString = "Ricky is first and can be found.";
let notFirst = "You can't find Ricky now.";
firstRegex.test(firstString);  // true
firstRegex.test(notFirst);  // false
```

#### `$`

Match ending string patters.

```js
let storyRegex = /story$/;
let theEnding = "This is a never ending story";
let noEnding = "Sometimes a story will have to end";
storyRegex.test(theEnding);  // true
storyRegex.test(noEnding);  // false
```

#### `+`

Match characters that occur one or more times.

```js
let exRegex = /a+/g;
let abcStr = "abc";
let aabcStr = "aabc";
let ababStr = "abab";
abcStr.match(exRegex);  // ["a"]
aabcStr.match(exRegex);  // ["aa"]
ababStr.match(exRegex);  // ["a", "a"]
```

#### `*`

Match characters that occur zero or more times.

```js
let exRegex = /go*/;
let gStr = "gx";
let goStr = "gox";
let gooStr = "goox";
gStr.match(exRegex);  // g
goStr.match(exRegex);  // go
gooStr.match(exRegex);  // goo
```

#### `{,}`

Quantity specifiers. Specify upper and lower number of matches. You put two numbers between the curly brackets, for the lower and upper number of patterns.

```js
let A4 = "aaaah";
let A2 = "aah";
let multipleA = /a{3,5}h/;
multipleA.test(A4);  // true
multipleA.test(A2);  // false
```

To only specify the lower number of patterns, keep the second number blank.

```js
let A4 = "haaaah";
let A2 = "haah";
let multipleA = /ha{3,}h/;
multipleA.test(A4);  // true
multipleA.test(A2);  // false
```

To specify a certain number of patterns, just have that one number between the curly brackets.

```js
let A4 = "haaaah";
let A3 = "haaah";
let multipleHA = /ha{3}h/;
multipleHA.test(A4);  // false
multipleHA.test(A3);  // true
```

#### `?`

A **greedy** match finds the longest possible part of a string that fits the regex pattern and returns it as a match, which is default in regular expressions. The alternative is called a **lazy** match, which finds the smallest possible part of the string that satisfies the regex pattern.

```js
let exStr = "titanic";
let greedyRegex = /t[a-z]*i/;
let lazyRegex = /t[a-z]*?i/;
exStr.match(greedyRegex);  // ["titani"]
exStr.match(lazyRegex);  // ["ti"]
```

#### `\w`

`\w` is same with `[A-Za-z0-9_]`. Note, this character class also includes the underscore character (`_`).

#### `\W`

It's the opposite of `\w`. It's same with `[^A-Za-z0-9_]`.

#### `\d`

It's same with `[0-9]`.

#### `\D`

It's the opposite of `\d`. It's same with `[^0-9]`.

#### `\s`

It matches whitespaces. It's same with `[ \r\t\f\n\v]`.

#### `\S`

It's the opposite of `\s`. It's same with `[^ \r\t\f\n\v]`.

#### `(?=...)`

Positive lookahead. It will look to make sure the element in the search pattern is there, but won't actually match it.

```js
let quit = "qu";
let quRegex = /q(?=u)/;
quit.match(quRegex);  // ["q"]
```

#### `(?!...)`

Negative lookahead. It will look to make sure the element in the search pattern is not there.

```js
let noquit = "qt";
let qRegex = /q(?!u)/;
noquit.match(qRegex);  // ["q"]
```

#### `()`

Check for mixed grouping of characters.

If you want to find either `Penguin` or `Pumpkin` in a string, you can use the following Regular Expression: `/P(engu|umpk)in/g`.

```js
let testStr = "Pumpkin";
let testRegex = /P(engu|umpk)in/;
testRegex.test(testStr);  // true
```

##### Capturing groups

Matches and remembers the match. For example, `/(foo)/` matches and remembers "foo" in "foo bar". The substring matched by the group is saved to a temporary variable, which can be accessed within

- same regex : a backslash and the number of the capture group (e.g. `\1`).
- else : a dollar sign(`$`) and the number (e.g. `$1`)

```js
let repeatRegex = /(\w+) \1 \1/;
repeatRegex.test(repeatStr); // Returns true
repeatStr.match(repeatRegex); // Returns ["row row row", "row"]
```

`.match()` returns the match and captured groups in order.

```js
"Code Camp".replace(/(\w+)\s(\w+)/, '$2 $1');  // "Camp Code"
```



## References

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions