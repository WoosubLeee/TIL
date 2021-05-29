# pjt 10

> 20210514에 진행한 프로젝트입니다.

### Home.vue

```vue
<template>
  <div class="row row-cols-1 row-cols-md-3 g-4">
    <MovieCard
      v-for="(movie, id) in movieList" 
      :key="id" 
      :movie="movie"
    />
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'

export default {
  name: 'Home',
  components: {
    MovieCard
  },
  computed: {
    movieList: function () {
      return this.$store.state.movies
    }
  },
  created: function () {
    this.$store.dispatch('getMovieData')
  }
}
</script>
```

created 상태가 되면 store.actions의 getMovieData를 실행하여 store.state.movies에 영화 데이터를 받아오고, computed를 사용해 movieList를 해당 component까지 불러온다.

### MovieCard.vue

```vue
<template>
  <div class="col">
    <div class="card h-100">
      <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" class="card-img-top" alt=".">
      <div class="card-body">
        <h5 class="card-title">{{ movie.title }} </h5>
        <p class="card-text">{{ movie.overview }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieCard',
  props:{
    movie: {
      type: Object
    }
  }
}
</script>
```

영화 하나의 내용은 vuex를 이용하면 불필요하게 여러 단계를 거쳐야 하므로 props를 활용했다.

### Random.vue

```vue
<template>
  <div>
    <button @click="randomPick">랜덤 픽!</button>
    <h3>{{ pickedMovie.title }}</h3>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  name: 'Random',
  data: function () {
    return {
      pickedMovie: []
    }
  },
  methods: {
    randomPick: function () {
      this.pickedMovie= _.sample(this.$store.state.movies, 1)
    }
  }
}
</script>
```

### MyMovieList.vue

```vue
<template>
  <div>
    <MyListForm/>
    <MyList/>
  </div>
</template>

<script>
import MyListForm from '@/components/MyListForm'
import MyList from '@/components/MyList'

export default {
  name: 'MyMovieList',
  components: {
    MyListForm,
    MyList
  }
}
</script>
```

### MyListForm.vue

```vue
<template>
  <div>
    <input type="text" @keyup.enter="submit">
    <button @click="submit">제출</button>
  </div>
</template>

<script>
export default {
  name: 'MyListForm',
  methods: {
    submit: function (event) {
      this.$store.dispatch('submit', event.target.value)
    }
  },
}
</script>
```

### MyList.vue

```vue
<template>
  <div>
    <ul v-for="(movie, id) in myMovies" :key="id">
      {{ movie }}
    </ul> 
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'MyList',
  computed: {
    ...mapState([
      'myMovies'
    ])
  }
}
</script>
```

### Points

- Vuex를 활용하여 어떻게 데이터를 받아오는지 조금 더 익힐 수 있었다.
- 최종 Project를 할 때 어떻게 해야할지 감을 잡을 수 있었다.