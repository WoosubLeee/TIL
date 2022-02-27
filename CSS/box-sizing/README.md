# `box-sizing`

`box-sizing` property의 default value는 `content-box`이다. `content-box`는 border나 padding을 width와 height에 포함시키지 않는다. 그렇기에 width나 height가 실제 지정한 크기와 맞지 않는 경우가 발생한다.

가령,

```css
.content {
    height: 10px;
    width: 10px;
    border-width: 1px;
    padding: 1px;
}
```

위와 같이 style을 구성하면, 실제 크기는 12px이 될 것이다.

이를 해결하기 위해 `box-sizing`의 `border-box` 를 활용할 수 있다.

## `border-box` 

`border-box` tells the browser to account for any border and padding in the values you specify for an element's width and height. If you set an element's width to 100 pixels, that 100 pixels will include any border or padding you added, and the content box will shrink to absorb that extra width. This typically makes it much easier to size elements. `box-sizing: border-box` is the default styling that browsers use for the `<table>`, `<select>`, and `<button>` elements, and for `<input>` elements whose type is `radio`, `checkbox`, `reset`, `button`, `submit`, `color`, or `search`.



## `content-box`

`content-box` gives you the default CSS box-sizing behavior. If you set an element's width to 100 pixels, then the element's content box will be 100 pixels wide, and the width of any border or padding will be added to the final rendered width, making the element wider than 100px.



## References

https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing