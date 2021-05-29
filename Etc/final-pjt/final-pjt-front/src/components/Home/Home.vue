<template>
  <div id="home">
    <div class="box-office-header d-flex flex-column align-items-center mt-5">
      <h2>Movies</h2>
      <hr width="200px" class="mt-1">
    </div>
    <HomeLargeCarousel
      :movies="movies.slice(0, 10)"
    />
    <h3 class="mt-5">최신 영화</h3>
    <hr>
    <HomeMovies
      :movies="moviesLatest"
      category="latest"
    />
  </div>
</template>

<script>
import { mapState } from 'vuex'
import HomeLargeCarousel from './HomeLargeCarousel'
import HomeMovies from './HomeMovies'

export default {
  name: 'Home',
  components: {
    HomeLargeCarousel,
    HomeMovies
  },
  computed: {
    ...mapState([
      'movies',
      'isLogin'
    ]),
    moviesLatest: function () {
      return this.movies.slice().sort(function (a, b) {
        return Date.parse(b.release_date) - Date.parse(a.release_date)
      }).slice(0, 31)
    }
  }
}
</script>

<style scoped>
  #home {
    overflow: visible;
  }
  h2 {
    font-size: 35px;
  }
  h3 {
    font-size: 28px;
  }
</style>