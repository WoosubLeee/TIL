# Workshop

### 점심메뉴

```vue
// views/TheLunch.vue

<template>
  <div>
    <h2>점심메뉴</h2>
    <button @click="selectMenu">Pick Lunch</button>
    <p>{{ selected }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLunch',
  data: function () {
    return {
      lunch: ['자장면', '햄버거', '잔치국수'],
      selected: '',
    }
  },
  methods: {
    selectMenu: function () {
      this.selected = _.sample(this.lunch)
    }
  }
}
</script>
```

- `name: 'TheLunch',` : Vue 객체의 이름

- ```vue
  data: function () {
    return {
      lunch: ['자장면', '햄버거', '잔치국수'],
      selected: '',
    }
  }
  ```

  component에서는 함수를 사용하여 반환값으로 전달하여야 한다. 그렇게 하지 않으면 data가 서로 다른 instance들에 영향을 미치기 때문이다.

```javascript
// index.js

const routes = [
  {
    path: '/lunch',
    name: 'TheLunch',
    component: TheLunch
  }
```

url 주소와 해당 url 주소로 갔을 때 표시될 component를 등록한다.

```vue
// app.vue

<router-link :to="{ name: 'TheLunch' }">Lunch</router-link>
```

v-bind를 활용한다. index.js에서 'TheLunch'라는 이름으로 등록된 component를 보여준다.

### 로또

```vue
// views/TheLotto.vue

<template>
  <div>
    <h2>로또</h2>
    <button @click="pickNum">Get Lucky Numbers</button>
    <p>{{ pickedNums }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLotto',
  data: function () {
    return {
      pickedNums: [],
    }
  },
  methods: {
    pickNum: function () {
      const nums = _.range(1, 46)
      this.pickedNums = _.sortBy(_.sampleSize(nums, 6))
    }
  }
}
</script>
```

# Homework

### 1.

- F - 처음에 생성될 때 실행된다. DOM에 다 그려지는 시점은 mounted이다.
- T
- F

### 2.

Vue router의 기본 설정은 Hash mode이다. Hash mode는 URL 해시를 사용하여 전체 URL을 시뮬레이트하므로 URL이 변경될 때 페이지가 다시 로드되지 않는다.

History mode는 해시를 사용하지 않게 해준다. History mode를 사용하면 URL을 탐색하더라도 페이지가 다시 로드되지 않는다.

### 3.

created!

mounted!
