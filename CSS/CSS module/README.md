# CSS module

CSS module은 CSS 클래스를 불러와서 사용할 때 `[파일이름]_[클래스이름]__[해쉬값]` 향태로 클래스네임을 고유하게 자동으로 만들어주어 컴포넌트 중첩현성을 방지해주는 기술입니다.



## How to use

CSS Module을 사용하기 위해서는 `[파일이름].module.css` 이런식으로 파일을 저장하면 된다. css 내부 코드는 기존과 같이 작성하면 된다.

이를 JS에 적용하기 위해선 일단 `import`를 하고, `className={styles.[클래스이름]}` 과 같은 형식으로 설정해주면 된다.

```jsx
import React from 'react';
import styles from './CSSModule.module.css';

const CSSModule = () => {
  return (
    <div className={`${styles.wrapper} ${styles.inverted}`}>
      안녕하세요, 저는 <span className="something">CSS Module!</span>
    </div>
  );
}

export default CSSModule;
```



## References

https://hangem-study.readthedocs.io/en/latest/css/module/

