# JavaScript Etc

## How to copy to clipboard

There are three primary browser APIs for copying to the clipboard:

1. Clipboard API

   ```js
   navigator.clipboard.writeText(text);
   ```

   - 비교적 최근에 도입된(from Chrome 66) API이다.

2. `dcoument.execCommand('copy')` (deprecated)

   ```js
   document.querySelector("copy-btn").addEventListener("click", function() {
     const textArea = document.getElementById('textarea'); 
     textArea.select();
     document.execCommand("copy");
   });
   ```

   - Most browsers support this.
   - Text is read from the DOM and placed on the clipboard.

### References

[How do I copy to the clipboard in JavaScript?](https://stackoverflow.com/questions/400212/how-do-i-copy-to-the-clipboard-in-javascript)

https://velog.io/@godori/js-clipboard-copy

## how to detect click outside div

HTML의 어떤 요소가 차지하고 있는 영역 이외의 영역을 click 했을 때 이를 감지하는 방법은 다음과 같다.

```js
window.addEventListener('click', function(e){   
  if (document.getElementById('clickbox').contains(e.target)){
    // Clicked in box
  } else{
    // Clicked outside the box
  }
});
```

### References

[Detect click outside div using javascript](https://stackoverflow.com/questions/36695438/detect-click-outside-div-using-javascript)

