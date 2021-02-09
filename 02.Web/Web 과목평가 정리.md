# Web 과목평가 정리

## HTML

##### 시맨틱 웹

- 웹 상에 존재하는 수많은 웹 페이지들에 메타데이터를 부여하여,
- 기존의 단순한 데이터의 집합이었던 웹페이지를 '의미'와 '관련성'을 가지는 거대한 데이터베이스로 구축하고자 하는 발상



## CSS

##### CSS

Cascading Style Sheets

스타일, 레이아웃 등을 통해 문서(HTML)를 표시하는 방법을 지정하는 언어

##### CSS 구문

<img src="Web 과목평가 정리.assets/image-20210208011846929.png" alt="image-20210208011846929" style="zoom:50%;" />

##### CSS 정의 방법

1. 인라인(inline)

   해당 태그에 직접 style 속성을 활용

2. 내부 참조(embedding)

   `head` 태그 내에 `<style>`에 지정

3. 외부 참조(link file)

   외부 CSS 파일을 `<head>` 내 `<link>`를 통해 불러오기

##### 선택자

- 기본 선택자
  - 전체 선택자, 요소 선택자
  - class 선택자, id 선택자, 속성 선택자
- 결합자(Combinators)
  - 자손 결합자, 자식 결합자
  - 일반 형제, 인접 형제 결합자
- 의사 클래스/요소(pseudo class)
  - 링크, 동적 의사 클래스
  - 구조적 의사 클래스

##### CSS 적용 우선순위(cascading order)

1. `!important`
2. 인라인
3. id 선택자
4. class 선택자
5. 요소 선택자
6. 소스 순서

##### CSS 상속

- 상속 되는 것
  - ex) Text 관련 요소(font, color, text-align), opacity, visibility 등
- 상속 되지 않는 것
  - ex) Box model 관련 요소(width, height, margin, padding, border, box-sizing, display)
          position 관련 요소(position, top/right/bottom/left, z-index) 등

##### CSS 단위

- (상대) 크기 단위
  - px(픽셀)
  - %
  - em : 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
  - rem : 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐
  - Viewport 기준 단위
- 색상 단위
  - 색상 키워드
  - RGB 색상
    - '#' + 16진수 표기법
    - rgb() 함수형 표기법
  - HSL 색상
    - 색상, 채도, 명도
- CSS 문서 표현

##### Margin, Padding shorthand

```
.margin {
  margin: 10px 20px 30px 40px;
}
```

- 1개 : 상하좌우
- 2개 : 상하 / 좌우
- 3개 : 상 / 좌우 /하
- 4개 : 상 / 우 / 하 / 좌

##### Border shorthand

```
.border {
  border-width: 2px;
  border-style: dashed;
  border-color: black;
}

==

.border {
  border: 2px dashed black;
}
```

##### box-sizing

기본적으로 모든 요소의 `box-sizing`은 `content-box`만

border까지의 너비로 정하고 싶으면 `box-sizing`을 `border-box`로 설정

##### display

- `display: block`
  - 대표적인 블록 레벨 요소
    - `div / ul, ol, li / p / hr / form`

- `display: inline`
  - `width, height, margin-top, margin-bottom`을 지정할 수 없다.
  - 상하 여백은 `line-height`로 지정한다.
  - 대표적인 인라인 레벨 요소
    - `span / a / img / input, label / b, em, i, strong` 등
- `display: inline-block`
  - block과 inline 레벨 요소의 특징을 모두 갖는다.
  - inline처럼 한 줄에 표시 가능하며,
  - block처럼 width, height, margin 속성을 모두 지정할 수 있다.
- `display: none`
  - 해당 요소를 화면에 표시하지 않는다.(공간조차 사라진다.)
  - 이와 비슷한 `visibility: hidden`은 해당 요소가 공간은 차지하나 화면에 표시만 하지 않는다.

##### CSS position

- `static` : 디폴트 값(기준 위치)
  - 기본적인 요소의 배치 순서에 따름(좌측 상단)
  - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치된다.
- `relative` : `static` 위치를 기준으로 이동(상대 위치)
- `absolute` : `static`이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동(절대 위치)
- `fixed` : 부모 요소와 관계 없이 브라우저를 기준으로 이동(고정 위치)
                 스크롤 시에도 항상 같은 곳에 위치



## CSS layout

### Float

- Float된 이미지 좌우측 주변으로 텍스트를 둘러싸는 레이아웃을 위해 도입
- 더 나아가 이미지가 아닌 다른 요소들에도 적용해 웹 사이트의 전체 레이아웃을 만드는 데까지 발전

##### Float 속성

- `none` : 기본값

- `left` : 요소를 왼쪽으로 띄움

- `right` : 요소를 오른쪽으로 띄움

  ```
  .left {
    float: left;
  }
  ```

##### Float clear

부모 요소에 `class="clearfix"`를 주고

```
.clearfix::after {
  content: "";
  display: block;
  clear: both;
}
```

### Flexbox

- 요소

  - Flex Container(부모 요소)
  - Flex Item(자식 요소)

- 축

  - main axis(메인축)
  - cross axis(교차축)

- 시작

  ```
  .flex-container {
    display: flex;
  }
  ```