<template>
  <div id="largeCarousel" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-indicators">
      <button
        v-for="i in moviesLength"
        :key="i"
        type="button"
        data-bs-target="#largeCarousel"
        :data-bs-slide-to="i - 1"
        :class="{ 'active': i == 1 }"
        :aria-current="{ 'true': i == 1 }"
      >
      </button>
    </div>
    <div class="carousel-inner">
      <div
        v-for="(movie, index) in movies"
        :key="index"
        class="carousel-item"
        :class="{ 'active': index == 0 }"
      >
        <HomeLargeCarouselItem :movie="movie"/>
      </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#largeCarousel" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#largeCarousel" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
    </button>
  </div>
</template>

<script>
import HomeLargeCarouselItem from './HomeLargeCarouselItem'

export default {
  name: 'HomeLargeCarousel',
  components: {
    HomeLargeCarouselItem
  },
  props: {
    movies: {
      type: Array
    }
  },
  computed: {
    moviesLength: function () {
      return this.movies.length
    }
  }
}
</script>

<style>

</style>