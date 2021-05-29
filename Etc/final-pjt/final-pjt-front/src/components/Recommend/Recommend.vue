<template>
  <div class="recommend-container">
    <h2>추천 영화</h2>
    <hr>
    <RecommendItem
      v-for="(movie, index) in moviesRated"
      :key="index"
      :movie="movie"
    />
  </div>
</template>

<script>
import { mapState } from 'vuex'
import RecommendItem from './RecommendItem'

export default {
  name: 'Recommend',
  components: {
    RecommendItem
  },
  computed: {
    ...mapState([
      'movies'
    ]),
    moviesRated: function () {
      return this.movies.slice().sort(function (a, b) {
        return parseFloat(b.userRating) - parseFloat(a.userRating)
      }).slice(0, 30)
    }
  }
}
</script>

<style scoped>
  .recommend-container {
    margin: 45px 0 0;
  }
  h2 {
    font-size: 32px;
    text-align: center;
  }
</style>