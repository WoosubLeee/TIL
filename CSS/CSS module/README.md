# CSS module

CSS module은 CSS 클래스를 불러와서 사용할 때 `[파일이름]_[클래스이름]__[해쉬값]` 향태로 클래스네임을 고유하게 자동으로 만들어주어 컴포넌트 중첩현성을 방지해주는 기술입니다.



## How to use

CSS Module을 사용하기 위해서는 `[파일이름].module.css` 이런식으로 파일을 저장하면 된다. css 내부 코드는 기존과 같이 작성하면 된다.

```css
/* Box.module.css */

.Box {
  background: black;
  color: white;
  padding: 2rem;
}
```

이를 JS에 적용하기 위해선 일단 `import`를 하고, `className={styles.[클래스이름]}` 과 같은 형식으로 설정해주면 된다.

```javascript
// Box.js

import React from "react";
import styles from "./Box.module.css";

function Box() {
  return <div className={styles.Box}>{styles.Box}</div>;
}

export default Box;
```

만약에 CSS Module을 사용한 클래스이름을 두개 이상 적용할 때는 이렇게 하면 된다.

```jsx
return (
  <div className={`${styles.wrapper} ${styles.inverted}`}>
    안녕하세요, 저는 <span className="something">CSS Module!</span>
  </div>
);
```

다음과 같이 클래스에 대해 고유한 이름이 만들어져 중복이 발생하지 않게 된다.

<img src="https://i.imgur.com/kEE8Swd.png" alt="img" style="zoom:50%;" />

### `className`에 `-`(hyphen) 사용하는 법

```jsx
<div className={styles.app-body} />
```

위와 같이 `className`에 `-`을 사용하려 하면 오류가 발생한다. 이를 해결하려면, array 형식으로 작성하면 된다.

```jsx
<div className={styles['app-body']} />
```



## References

https://hangem-study.readthedocs.io/en/latest/css/module/

https://react.vlpt.us/styling/02-css-module.html

