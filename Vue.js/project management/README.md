# project management

## Architecture

#### how to make architecture tree

터미널에서 `$ tree > 파일명.txt` 를 입력한다.

### example

#### 1)

```
.
├─ README.md
├─ index.html
├─ webpack.config.js
├─ package.json
└─ src
   ├─ main.js
   ├─ App.vue
   ├─ components        컴포넌트
   │  ├─ common
   │  └─ ...
   ├─ routes            라우터
   │  ├─ index.js
   │  └─ routes.js
   ├─ views             라우터 페이지
   │  ├─ MainView.vue
   │  └─ ...
   ├─ store             상태 관리
   │  ├─ auth
   │  ├─ index.js
   │  └─ ...
   ├─ api               api 함수
   │  ├─ index.js
   │  ├─ users.js
   │  └─ ...
   ├─ utils             필터 등의 유틸리티 함수
   │  ├─ filters.js
   │  ├─ bus.js
   │  └─ ...
   ├─ mixins            믹스인
   │  ├─ index.js
   │  └─ ...
   ├─ plugins           플러그인
   │  ├─ ChartPlugin.js
   │  └─ ...
   ├─ translations      다국어
   │  ├─ index.js
   │  ├─ en.json
   │  └─ ...
   ├─ images            이미지
   ├─ fonts             폰트
   └─ assets            기타 자원
```

# References

- https://velog.io/@cindy-choi/VUE-%EC%9A%B0%EC%95%84%ED%95%9C-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EA%B5%AC%EC%A1%B0-%EC%A7%9C%EA%B8%B0 ([VUE] 🌱우아한 프로젝트 구조 짜기)

- https://joshua1988.github.io/web-development/vuejs/vue-structure/ (실무에서 사용하는 Vue.js 프로젝트 구조)