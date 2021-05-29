# Practice

```html
<h1>Cat Image</h1>
<div id="app">
  <img v-bind:src="imgSrc">
  <br>
  <button v-on:click="getCat">Get Cat</button>
</div>
```

- `v-bind:src="imgSrc"` : v-bind 디렉티브를 사용하여 src 속성에 Vue의 상태 데이터를 값으로 할당한다.
- `<button v-on:click="getCat">Get Cat</button>` : button 클릭 시 getCat method 실행

```javascript
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    data: {
      imgSrc: '',
    },
    methods: {
      getCat: function () {
  		const API_URI = 'https://api.thecatapi.com/v1/images/search'
        axios.get(API_URI)
          .then((response) => {
            this.imgSrc = response.data[0].url
          })
      }
    }
  })
</script>
```

- `const app = new Vue({` : Vue 인스턴스 생성

- `el: '#app'` : Vue 인스턴스에 DOM element를 마운트

- ```javascript
  data: {
    imgSrc: "",
  }
  ```

  Vue 앱의 상태 데이터를 정의

- `this.imgSrc = response.data[0].url` : arrow function을 쓰지 않아 this를 통해 imgSrc로 접근 가능