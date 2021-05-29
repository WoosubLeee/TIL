<template>
  <div>
    <MovieDetailSummary
      :movie="movie"
    />
    <MovieDetailReviews
      :movie="movie"
    />
  </div>
</template>

<script>
import axios from 'axios'
import MovieDetailSummary from './MovieDetailSummary'
import MovieDetailReviews from './MovieDetailReviews'

export default {
  name: 'MovieDetail',
  components: {
    MovieDetailSummary,
    MovieDetailReviews
  },
  data: function () {
    return {
      movie: undefined
    }
  },
  created: function () {
    axios.get(`http://127.0.0.1:8000/movies/${this.$route.params.movie_id}`)
      .then((response) => {
        this.movie = response.data
        console.log(this.movie)
      })
      .catch((error) => {
        console.log(error)
      })
  }
}
</script>

<style>

</style>