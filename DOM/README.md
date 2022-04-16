# DOM (Document Object Model)

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



## DOM and JavaScript

The DOM is not a programming language, but without it, the JavaScript language wouldn't have any model or notion of web pages, HTML documents, SVG documents, and their component parts. The DOM is not part of the JavaScript language, but is instead a **Web API** used to build websites.

So implementations of the DOM can be built for any language, as this Python example demonstrates:

```python
# Python DOM example
import xml.dom.minidom as m
doc = m.parse(r"C:\Projects\Py\chap1.xml")
doc.nodeName # DOM property of document object
p_list = doc.getElementsByTagName("para")
```



## Fundamental data types

| Data type (Interface) | Description                                                  |
| --------------------- | ------------------------------------------------------------ |
| document              | The root `document` object itself                            |
| node                  | Every object located within a document is a node of some kind. In an HTML document, an object can be an element node but also a text node or attribute node. |
| element               | The `element` type is based on `node`. `element` objects implement the DOM `Element` interface and also the more basic `Node` interface. In an HTML document, elements are further enhanced by the HTML DOM API's `HTMLElement` interface as well as other interfaces describing capabilities of specific kinds of elements (for instance, `HTMLTableElement` for `<table>` elements). |
| nodeList              | A `nodeList` is an array of elements. Items in a `nodeList` are accessed by index in either of two ways:<br />- list.item(1)<br />- list[1] |
| attr                  | Attributes are nodes in the DOM just like elements are.      |
| namedNodeMap          | A `namedNodeMap` is like an array, but the items are accessed by name or index, though this latter case is merely a convenience for enumeration, as they are in no particular order in the list. |



## DOM interfaces

For example, the object representing the HTML `form` element gets its `name` property from the `HTMLFormElement` interface but its `className` property from the `HTMLElement` interface. In both cases, the property you want is in that form object.

### Interfaces and objects

Many objects borrow from several different interfaces. The table object, for example:

- `HTMLTableElement` : methods such as `createCaption` and `insertRow`
- `Element`
- `Node` : from which `Element` derives



## References

https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction