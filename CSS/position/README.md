# position

## CSS position

- 문서 상에서 요소를 배치하는 방법

### 1. static

- default
- 요소의 일반적인 문서 흐름에 따라 배치(좌측 상단)
- top, bottom, left, right 속성 X
- 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치

### 2. relative

- 요소의 일반적인 문서 흐름에 따라 배치
- 자기 자신을 기준으로 top, bottom, left, right 속성 O (상대 위치)
- offset은 다른 요소에는 영향 X => 페이지 레이아웃에서 요소가 차지하는 공간은 static과 같다

### 3. absolute

- 요소를 일반적인 문서 흐름에서 제거
- 페이지 레이아웃에서 요소가 차지하는 공간 X
- 가장 가까운 위치 지정 요소(=부모)(없다면 containing block)에 대해 상대적으로 배치 (절대 위치)

### 4. fixed

- 요소를 일반적인 문서 흐름에서 제거
- 페이지 레이아웃에서 요소가 차지하는 공간 X
- Viewport 기준으로 배치

