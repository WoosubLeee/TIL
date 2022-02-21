# how to detect click outside div

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



## References

[Detect click outside div using javascript](https://stackoverflow.com/questions/36695438/detect-click-outside-div-using-javascript)