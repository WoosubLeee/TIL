# Workshop

## 1. Semantic Tag

```
/* 1. article 태그는 white로 나머지 시멘틱 태그는 lightgrey로 배경색을 바꿔주세요. */
.bg-lightgrey {
  background-color: lightgrey;
}

.bg-white {
  background-color: white;
}

/* 2. 모든 시멘틱 태그의 margin과 padding을 4px로 만들어주세요. */
.m-4 {
  margin: 4px;
}

.p-4 {
  padding: 4px;
}

/* 3. h1 태그를 중앙 정렬 시켜주세요. */
.text-center {
  text-align: center;
}

/* 4. section과 aside 태그의 display를 inline-block으로 바꿔주세요. */
.d-inline-block {
  display: inline-block;
}

/* 5. section 태그는 width 482px height 300px, aside 태그는 width 280px height 300px로 만들어주세요.*/
.section-width-height {
  width: 482px;
  height: 300px;
}

.aside-width-height {
  width: 280px;
  height: 300px
}

/* 6. aside 태그에 vertical-align속성의 값을 top으로 적용해주세요.*/
.v-aside-top {
  vertical-align: top;
}

/* 7. 모든 semantic 태그의 border 모서리 반경을 4px로 만들어주세요. */
.br-4 {
  border-radius: 4px;
}
```

html 파일에서 element에 class 지정 예시 :

`<aside class="bg-lightgrey m-4 p-4 br-4 d-inline-block aside-width-height v-aside-top">`



# Homework

## 1. Semantic Tag

`header, section, footer`



## 2. input Tag

```
<form action="#">
  # <label> tag를 활용. id가 username인 tag를 대상으로 한다.
  <label for="username">USERNAME : </label>
  # placeholder로 비어있을 때 보여줄 값 설정
  <input type="text" id="username" placeholder="아이디를 입력 해 주세요."><br>
  <label for="pwd">PWD : </label>
  # 내용을 적어도 보이지 않게 하기 위해 type="password"
  <input type="password" id="pwd" name="pwd" placeholder="•••••••••">
  # "submit" type 활용
  <input type="submit" value="로그인">
</form>
```



## 3. 크기 단위

rem



## 4. 선택자

자손 선택자 : 모든 자손

자식 선택자 : 자손 중 직계 자식만

