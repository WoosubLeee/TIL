# DOM (Document Object Model)

## What is DOM?

The Document Object Model (DOM) is a programming **interface** for web documents. It represents the page  as **nodes** and **objects** so that programming languages can interact with the page (change the document structure, style, and content). A web page can be modified with a scripting language such as JS via DOM.

For example, the DOM specifies that the `querySelectorAll` method in this code snippet must return a list of all the `<p>` elements in the document:

```js
const paragraphs = document.querySelectorAll("p");
// paragraphs[0] is the first <p> element
// paragraphs[1] is the second <p> element, etc.
alert(paragraphs[0].nodeName);
```

All of the properties, methods, and events available for manipulating and creating web pages are organized into **objects**.

The DOM is built using multiple APIs that work together:

- The core [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model) defines the entities describing any document and the objects within it.
- The [HTML DOM API](https://developer.mozilla.org/en-US/docs/Web/API/HTML_DOM_API) adds support for representing HTML documents to the core DOM.
- etc...

### DOM and JavaScript

The DOM is not a programming language, but without it, the JavaScript language wouldn't have any model or notion of web pages, HTML documents, SVG documents, and their component parts. The DOM is not part of the JavaScript language, but is instead a **Web API** used to build websites.

So implementations of the DOM can be built for any language, as this Python example demonstrates:

```python
# Python DOM example
import xml.dom.minidom as m
doc = m.parse(r"C:\Projects\Py\chap1.xml")
doc.nodeName # DOM property of document object
p_list = doc.getElementsByTagName("para")
```

### Fundamental data types

| Data type (Interface) | Description                                                  |
| --------------------- | ------------------------------------------------------------ |
| document              | The root `document` object itself                            |
| node                  | Every object located within a document is a node of some kind. In an HTML document, an object can be an element node but also a text node or attribute node. |
| element               | The `element` type is based on `node`. `element` objects implement the DOM `Element` interface and also the more basic `Node` interface. In an HTML document, elements are further enhanced by the HTML DOM API's `HTMLElement` interface as well as other interfaces describing capabilities of specific kinds of elements (for instance, `HTMLTableElement` for `<table>` elements). |
| nodeList              | A `nodeList` is an array of elements. Items in a `nodeList` are accessed by index in either of two ways:<br />- list.item(1)<br />- list[1] |
| attr                  | Attributes are nodes in the DOM just like elements are.      |
| namedNodeMap          | A `namedNodeMap` is like an array, but the items are accessed by name or index, though this latter case is merely a convenience for enumeration, as they are in no particular order in the list. |

### DOM interfaces

For example, the object representing the HTML `form` element gets its `name` property from the `HTMLFormElement` interface but its `className` property from the `HTMLElement` interface. In both cases, the property you want is in that form object.

#### Interfaces and objects

Many objects borrow from several different interfaces. The table object, for example:

- `HTMLTableElement` : methods such as `createCaption` and `insertRow`
- `Element`
- `Node` : from which `Element` derives

### References

https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction



## History API

The DOM [`Window`](https://developer.mozilla.org/en-US/docs/Web/API/Window) object provides access to the browser's session history through the [`history`](https://developer.mozilla.org/en-US/docs/Web/API/Window/history) object. It exposes useful methods and properties that let you navigate back and forth through the user's history, and manipulate the contents of the history stack.

React Router나 Vue Router 모두 History API를 이용해 routing 한다.

### Methods

HTML5 introduced the `pushState()` and `replaceState()` methods for add and modifying history entries, respectively. These methods work in conjunction with the `onpopstate` event.

#### `pushState(state, title, url)`

###### parameters

- `state` : A JS object associated with the new history entry. When a `popstate` event if fired, the `state` property of the event contains a copy of the history entry's state object. The state object can be anything that can be serialized. A size limit of 640k characters.
- `title` : 현재는 안 쓰임
- `url` : optional (If not specified, it's set to the current URL) . The new history entry's URL. `pushState()`로는 이 URL이 로드되지 않는다 (그저 상태를 변경할 뿐). But it might attempt to load the URL later, for instance after the user restarts the browser. Can be absolute or relative. Must be of the same origin as the current URL.

##### Example

- 시작 : `https://mozilla.org/foo.html`, `history.state` = null

```js
let stateObj = {
    foo: "bar",
}

history.pushState(stateObj, "page 2", "bar.html")
```

코드가 실행되면

- 변경 :  `https://mozilla.org/bar.html`, `history.state` = `stateObj`

But it won't cause the browser to load `bar.html` or even check that `bar.html` exists. Only the state changes. The `popstate` event won't be fired because the page has been reloaded.

If the user clicks **Back** once again, the URL will change to `https://mozilla.org/foo.html`, and the document will get a `popstate` event, this time with a `null` state object.

####  `replaceState()`

Operates exactly like `history.pushState()`, except that `replaceState()` modifies the current history entry instead of creating a new one.

#### `back()`, `forward()`, `go()`

- `window.history.back()` : moving backward
- `window.history.forward()` : moving forward
- `window.history.go()` : moving to a specific point identified by its relative position to the current page(`0`)
  - `window.history.go(-1)` : move back a page
  - `window.history.go(1)` : move forward a page

#### `popstate`

A `popstate` event is dispatched to the window every time the active history entry changes.

- `pushState()`, `replaceState()`는 트리거시키지 않는다.
- `back()`, `forward()`, `go()`, 뒤로가기 버튼 등은 트리거 시킨다.

### References

https://developer.mozilla.org/en-US/docs/Web/API/History_API

https://developer.mozilla.org/en-US/docs/Web/API/History

https://developer.mozilla.org/en-US/docs/Web/API/History_API/Working_with_the_History_API

[Using the HTML5 History API](https://css-tricks.com/using-the-html5-history-api/)

[History API in HTML5 :: 마이구미](https://mygumi.tistory.com/299)