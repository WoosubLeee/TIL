# Vue

## Installation - CDN

```html
<head>
  <!-- vue@ 뒤로 버전을 삽입한다('next'가 들어가면 최신 버전) -->
  <script src="https://unpkg.com/vue@3.0.2"></script>
</head>
```

CDN을 사용해 Vue를 사용한다.
`vue@` 뒤에는 버전을 삽입한다. 이 tutorial에서는 3.0.2 버전을 사용한다.

### Vue app mount

```javascript
// Vue app 생성
const app = Vue.createApp()

// app이란 id 셀렉터를 가진 태그에 mount 한다
app.mount('#app')
```

### v-if vs v-show

v-if는 조건에 따라  실제로 컴포넌트가 제거되고 생성된다.

v-show는 항상 생성되어 있고, css의 display 속성을 사용해 보여지거나 안 보여지게 하는 것이다.

