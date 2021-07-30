# containing block

1. If the `position` property is `static`, `relative`, or `sticky`, the containing block is formed by the edge of the *content box* of the nearest ancestor element that is either **a block container** (such as an inline-block, block, or list-item element) or **establishes a formatting context** (such as a table container, flex container, grid container, or the block container itself).
2. If the `position` property is `absolute`, the containing block is formed by the edge of the *padding box* of the nearest ancestor element that has a `position` value other than `static` (`fixed`, `absolute`, `relative`, or `sticky`).
3. If the `position` property is `fixed`, the containing block is established by the viewport(in the case of continuous media) or the page area (in the case of paged media).
4. If the `position `property is `absolute` or `fixed`, the containing block may also be formed by the edge of the padding box of the nearest ancestor element that has the following:
   1. A `transfrom` or `perspective` value other than `none`
   2. A `will-change` value of `transform` or `perspective`
   3. A `filter` value other than `none` or a `will-change` value of `filter` (only works on Firefox).
   4. A `contain` value of `paint` (e.g. `contain: paint;`)

