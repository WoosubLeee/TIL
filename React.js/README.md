# React.js

## Virtual DOM

The virtual DOM (VDOM) is a programming concept where an ideal, or “virtual”, representation of a UI is kept in memory and synced with the “real” DOM by a library such as ReactDOM. This process is called reconciliation.

### Reconciliation

You can think of the `render()` function as creating a tree of React elements. On every render, React needs to figure out how to efficiently update the UI to match the most recent tree. To transform one tree into another, even the state of the art algorithms have a complexity in the order of O(n<sup>3</sup> ) where n is the number of elements in the tree.

## DOM elements

### Differences in attributes

There are a number of attributes that work differently between React and HTML:

#### dangerouslySetInnerHTML

`dangerouslySetInnerHTML` is React’s replacement for using `innerHTML` in the browser DOM. In general, setting HTML from code is risky because it’s easy to inadvertently expose your users to a cross-site scripting (XSS) attack. So, you can set HTML directly from React, but you have to type out `dangerouslySetInnerHTML` and pass an object with a `__html` key, to remind yourself that it’s dangerous. For example:

```jsx
function createMarkup() {
  return {__html: 'First &middot; Second'};
}

function MyComponent() {
  return <div dangerouslySetInnerHTML={createMarkup()} />;
}
```

