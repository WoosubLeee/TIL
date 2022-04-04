# CSS

## position

### CSS position

- 문서 상에서 요소를 배치하는 방법

#### 1. static

- default
- 요소의 일반적인 문서 흐름에 따라 배치(좌측 상단)
- top, bottom, left, right 속성 X
- 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치

#### 2. relative

- 요소의 일반적인 문서 흐름에 따라 배치
- 자기 자신을 기준으로 top, bottom, left, right 속성 O (상대 위치)
- offset은 다른 요소에는 영향 X => 페이지 레이아웃에서 요소가 차지하는 공간은 static과 같다

#### 3. absolute

- 요소를 일반적인 문서 흐름에서 제거
- 페이지 레이아웃에서 요소가 차지하는 공간 X
- 가장 가까운 위치 지정 요소(=부모)(없다면 containing block)에 대해 상대적으로 배치 (절대 위치)

#### 4. fixed

- 요소를 일반적인 문서 흐름에서 제거
- 페이지 레이아웃에서 요소가 차지하는 공간 X
- Viewport 기준으로 배치



## containing block

1. If the `position` property is `static`, `relative`, or `sticky`, the containing block is formed by the edge of the *content box* of the nearest ancestor element that is either **a block container** (such as an inline-block, block, or list-item element) or **establishes a formatting context** (such as a table container, flex container, grid container, or the block container itself).
2. If the `position` property is `absolute`, the containing block is formed by the edge of the *padding box* of the nearest ancestor element that has a `position` value other than `static` (`fixed`, `absolute`, `relative`, or `sticky`).
3. If the `position` property is `fixed`, the containing block is established by the viewport(in the case of continuous media) or the page area (in the case of paged media).
4. If the `position `property is `absolute` or `fixed`, the containing block may also be formed by the edge of the padding box of the nearest ancestor element that has the following:
   1. A `transform` or `perspective` value other than `none`
   2. A `will-change` value of `transform` or `perspective`
   3. A `filter` value other than `none` or a `will-change` value of `filter` (only works on Firefox).
   4. A `contain` value of `paint` (e.g. `contain: paint;`)



## `box-sizing`

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

### `border-box` 

`border-box` tells the browser to account for any border and padding in the values you specify for an element's width and height. If you set an element's width to 100 pixels, that 100 pixels will include any border or padding you added, and the content box will shrink to absorb that extra width. This typically makes it much easier to size elements. `box-sizing: border-box` is the default styling that browsers use for the `<table>`, `<select>`, and `<button>` elements, and for `<input>` elements whose type is `radio`, `checkbox`, `reset`, `button`, `submit`, `color`, or `search`.

### `content-box`

`content-box` gives you the default CSS box-sizing behavior. If you set an element's width to 100 pixels, then the element's content box will be 100 pixels wide, and the width of any border or padding will be added to the final rendered width, making the element wider than 100px.

### References

https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing