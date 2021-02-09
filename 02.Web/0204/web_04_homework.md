# Workshop

## 1. 기본 그리드 레이아웃

### 1)

```
<div class="item col">
```

세 칼럼 모두 col을 선언하여 3분의 1씩 나눠지게 하였다.

### 2)

```
<!-- 1과 같음 -->
<div class="item col">
```

column이 2개이므로 2분의 1씩 나눠가진다.

### 3)

```
<div class="item col-3">
  <p>3개</p>
</div>  
<div class="item col-6">
  <p>6개</p>
</div>
<div class="item col-3">
  <p>3개</p>
</div>
```

`col-n`개의 형식으로 각각 n개씩의 칸 수를 차지하게 하였다.

### 4)

```
<div class="item col-2">
  <p>2개</p>
</div>
<div class="item col-7">
  <p>7개</p>
</div>
<div class="item col-3">
  <p>3개</p>
```

3과 같은 방법이다.



## 2. 반응형 그리드

### 1)

```
<div class="item col col-sm-2">
  <p>576px 미만 4 <br> 576px 이상 2</p>
</div>
<div class="item col col-sm-5">
  <p>576px 미만 4 <br> 576px 이상 5</p>
</div>
<div class="item col col-sm-5">
  <p>576px 미만 4 <br> 576px 이상 5</p>
</div>
```

`col-n col-sm-m` : 576px 이상일 경우 m, 아닐 경우 n개의 column을 가진다.

### 2)

```
<div class="item col-1 col-md-2">
  <p>768px 미만 1 <br> 768px 이상 2</p>
</div>
<div class="item col-3 col-md-3">
  <p>768px 미만 3 <br> 768px 이상 3</p>
</div>
<div class="item col-4 col-md-3">
  <p>768px 미만 4 <br> 768px 이상 3</p>
</div>
<div class="item col-1 col-md-2">
  <p>768px 미만 1 <br> 768px 이상 2</p>
</div>
<div class="item col-3 col-md-2">
  <p>768px 미만 3 <br> 768px 이상 2</p>
</div>
```

`col-n col-md-m` : 768px 이상일 경우 m, 아닐 경우 n개의 column을 가진다.

### 3)

```
<div class="item col-4 col-sm-3 col-md-6">
  <p>576px 미만 4 <br> 768px 미만 3 <br> 768px 이상 6</p>
</div>
<div class="item col-6 col-sm-3 col-md-6">
  <p>576px 미만 6 <br> 768px 미만 3 <br> 768px 이상 6</p>
</div>
<div class="item col-2 col-sm-6 col-md-12">
  <p>576px 미만 2 <br> 768px 미만 6 <br> 768px 이상 12</p>
</div>
```

`col-n col-sm-m col-md-l` : 576px 이상일 경우 m, 768px 이상일 경우 l, 아닐 경우(576px 미만) n개의 column을 가진다.

### 4)

```
<div class="item col-12 col-md-4 col-xl-2">
  <p>768px 미만 12 <br> 768px 이상 4 <br> 1200px 이상 2</p>
</div>
<div class="item col-12 col-md-4 col-xl-2">
  <p>768px 미만 12 <br> 768px 이상 4 <br> 1200px 이상 2</p>
</div>
<div class="item col-12 col-md-4 col-xl-12">
  <p>768px 미만 12 <br> 768px 이상 4 <br> 1200px 이상 12</p>
</div>
```

`col-n col-md-m col-xl-l` : 768px 이상일 경우 m, 1200px 이상일 경우 l, 아닐 경우(768px 미만) n개의 column을 가진다.



## 3. 그리드 심화

### 1)

```
<div class="item col-4">
  <p>item1</p>
</div>
<div class="item col-8 col-md-4 offset-md-4">
  <p>item2</p>
</div>
```

`offset-md-4` : 768px 이상일 경우 4칸의 `offset` 발생

### 2)

```
<div class="item col-4 offset-md-4 col-lg-5 offset-lg-7">
  <p>item1</p>
</div>
<div class="item col-4 offset-4 offset-md-0 col-lg-8 offset-lg-2">
  <p>item2</p>
</div>
```

`offset-md-4` : 768px 이상일 경우 4칸의 `offset` 발생

`offset-lg-7` : 992px 이상일 경우 7칸의 `offset` 발생

### 3)

```
<div class="item col-12 col-md-3">
  item1
</div>
<div class="item col-12 col-md-9">
  <div class="row">
    <div class="item col-6 col-lg-3">item2</div>
    <div class="item col-6 col-lg-3">item3</div>
    <div class="item col-6 col-lg-3">item4</div>
    <div class="item col-6 col-lg-3">item5</div>
  </div>
</div>
```

nesting을 위해 안쪽에 `row`를 한 번 더 선언



# Homework

## 1. CSS flex-direction

`row` : 좌에서 우로

`row-reverse` : 우에서 좌로

`column` : 위에서 아래로

`column-reverse` : 아래서 위로



## 2. Bootstrap flex-direction

`row` - `flex-row`

`row-reverse` - `flex-row-reverse`

`column` - `flex-column`

`column-reverse` - `flex-column-reverse`



## 3. align-items

`stretch` : 교차축 방향으로 부모 요소를 가득 채우게 된다.

`center` : 교차축 방향으로 중앙 정렬한다.

`start` : 교차축의 시작 방향으로 정렬한다.

`end` : 교차축의 끝 방향으로 정렬한다.



## 4. flex-flow

(1)



## 5. Bootstrap Grid System

(a) : `container`

(b) : `row`



## 6. Breakpoint prefix

1)

부모 `container`의 너비가

`xs` : 576px 미만

`sm` : 576px 이상

`md` : 768px 이상

`lg` : 992px 이상

`xl` : 1200px 이상

`xxl` : 1400px 이상



2)

1~12

부모 `container`를 12 column으로 나누고 그 중 몇 column을 차지하는가를 나타낸다.

