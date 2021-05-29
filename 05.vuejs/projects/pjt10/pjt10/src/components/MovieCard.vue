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

<style>

</style>