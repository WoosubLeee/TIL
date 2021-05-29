<template>
  <div class="summary-area d-flex justify-content-center align-items-center">
    <div class="summary-inner d-flex">
      <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" class="rounded-3">
      <div class="summary-description">
        <h1>{{ movie.title }}</h1>
        <h3>{{ movie.subtitle }}</h3>
        <div class="rating-area">
          <i class="fas fa-star"></i>
          <span class="ms-2">{{ movie.userRating }}</span>
        </div>
        <div class="button-area">
          <router-link :to="{ name: 'ReviewCreate', params: { movie_id: movie.id } }">
            <i class="fas fa-pencil-alt"></i>
          </router-link>
        </div>
        <h4 class="my-3">줄거리</h4>
        <p>{{ movie.overview }}</p>
      </div>
    </div>
    <div class="bg-area">
      <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" class="bg-img">
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieDetailSummary',
  props: {
    movie: {
      type: Object
    }
  }
}
</script>

<style scoped>
  .summary-area {
    position: relative;
    height: 600px;
    overflow: hidden;
  }
  .summary-inner {
    height: 83%;
    width: 90%;
  }
  .summary-description {
    width: 100%;
    margin: auto 0;
    padding: 0 0 0 40px;
  }
  .rating-area {
    font-size: 20px;
  }
  .button-area {
    font-size: 22px;
  }
  a {
    text-decoration: none;
    color: white;
  }
  .button-area i {
    margin: 20px 20px 10px 0;
    border-radius: 70px;
    box-shadow: 0px 0px 2px #888;
    padding: 0.5em 0.6em;
  }
  .bg-area {
    position: absolute;
    height: 100%;
    width: 100%;
    top: -30%;
    z-index: -1;
  }
  .bg-img {
    width: 100%;
    opacity: 0.25;
  }
</style>