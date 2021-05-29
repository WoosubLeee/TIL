<template>
  <div class="recommend-item d-inline-block">
    <router-link
      :to="{ name: 'MovieDetail', params: { movie_id: movie.id } }"
    >
      <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" class="poster rounded w-100">
      <p class="title">{{ movie.title }}</p>
      <p class="rating">
        <i class="fas fa-star"></i>
        {{ movie.userRating }}
      </p>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'RecommendItem',
  props: {
    movie: {
      type: Object
    }
  }
}
</script>

<style scoped>
  .recommend-item {
    width: 426px;
    text-align: center;
  }
  a {
    text-decoration: none;
    color: white;
  }
  img {
    height: 600px;
  }
  .title {
    font-size: 20px;
  }
  .rating {
    font-size: 20px;
  }
  .rating > i {
    color: gold;
  }
</style>