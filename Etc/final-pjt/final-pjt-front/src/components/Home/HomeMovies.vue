<template>
  <div :id="category" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-inner">
      <div v-for="(movies, index) in dividedMovies" :key="index" class="carousel-item" :class="{ 'active': index == 0 }" data-bs-interval="10000">
        <div class="row flex-row justify-content-center flex-nowrap overflow-visible">
          <HomeMoviesItem
            v-for="(movie, index) in movies"
            :key="index"
            :movie="movie"
          />
        </div>
      </div>
    </div>
    <!-- slide move buttons -->
    <button class="carousel-button carousel-control-prev" type="button" :data-bs-target="`#${category}`" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    </button>
    <button class="carousel-button carousel-control-next" type="button" :data-bs-target="`#${category}`" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
    </button>
  </div>
</template>

<script>
import HomeMoviesItem from './HomeMoviesItem'

export default {
  name: 'HomeMovies',
  components: {
    HomeMoviesItem
  },
  props: {
    movies: {
      type: Array
    },
    category: {
      type: String
    }
  },
  computed: {
    dividedMovies: function () {
      const divided = []
      for(var i = 0; i < (this.movies.length / 6 - 1); i++) {
        divided.push(this.movies.slice(6*i, 6*(i+1)))
      }
      return divided
    }
  }
}
</script>

<style scoped>
  .carousel-inner {
    overflow: visible;
  }
  .row {
    padding: 3% 0;
    z-index: 999;
  }
  .carousel-button {
    top: 40%;
    height: 20%;
    z-index: 1000;
  }
</style>