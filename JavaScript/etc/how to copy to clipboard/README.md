# How to copy to clipboard

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



## References

[How do I copy to the clipboard in JavaScript?](https://stackoverflow.com/questions/400212/how-do-i-copy-to-the-clipboard-in-javascript)

https://velog.io/@godori/js-clipboard-copy