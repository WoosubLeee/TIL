# SVG(Scalable Vector Graphics)

SVG는 2차원 벡터 그래픽의 표현을 위한 XML 마크업 언어이다.



## Raster vs Vector

일반적으로 가장 널리 사용되는 이미지 형식인 PNG, JPG 등과의 가장 큰 차이는 이미지를 구성하는 방식에 있다.

### Raster

이미지의 모양과 색을 색상 정보가 담긴 픽셀로 표현하는 방식이다. 흔히 비트맵 방식이라고 불린다. 각각의 픽셀을 이용해 작업하는 만큼 자연스러운 이미지를 표현할 수 는 있지만, 확대를 할 경우 그림이 깨져서 보이는 계단식 현상이 나타나고, 픽셀의 수가 많아질수록 파일의 크기가 커지는 단점이 있다.

### Vector

수학적 함수를 이용하여 도형이나 선을 그려서 표시하는 방식으로써, 확대하였을 때 계단식 현상이 일어나지 않고 선명함을 유지한다. 레스터 방식에 비해 용량이 작은 편이다. 하지만 색상의 자연스러운 변화나 세밀한 표현이 어렵다는 단점이 있다.

SVG 의 경우는 수학적 계산 능력을 요구한다. 단순한 이미지는 신경쓰지 않아도 되지만, 복잡해질수록 크기가 커지거나 속도 저하를 초래한다. 또한 SVG 로 표현하기 어려운 이미지들도 많이 존재한다. **그렇기에, SVG 는 로고 또는 단순화된 이미지에 많이 활용한다.**



## SVG in React

SVG 코드는 다음과 같다.

```html
<svg
  xmlns="http://www.w3.org/2000/svg"
  width="24"
  height="24"
  viewBox="0 0 24 24"
>
  <path fill="#fff" fill-rule="evenodd" d="...." />
</svg>
```

### 사용법

#### 1. img src에 이용

```jsx
import Reservation from 'assets/icon-24-reservation.svg'

<img src={Reservation}>
```

#### 2. React component로 만들어 사용하기

```jsx
import { ReactComponent as Reservation } from "assets/icon-24-reservation.svg";

<Reservation />;
```

이 방법을 사용하면 SVG의 색, 크기를 쉽게 변경할 수 있다.

먼저 SVG에서 바꾸고자 하는 요소를 `current`로 바꿔준다.

```html
<svg
  xmlns="http://www.w3.org/2000/svg"
  width="current"
  height="current"
  viewBox="0 0 24 24"
>
  <path fill="current" fill-rule="evenodd" d="...." />
</svg>
```

해당 요소들은 props로 지정하여 값을 내려준다.

```jsx
import { ReactComponent as Reservation } from "assets/icon-24-reservation.svg";

<Reservation width="10" height="10" fill="blue" />;
```



## References

https://mygumi.tistory.com/283

https://post.naver.com/viewer/postView.nhn?volumeNo=27689642&memberNo=43589165

https://kyounghwan01.github.io/blog/React/handling-svg

