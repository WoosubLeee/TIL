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

<style>

</style>