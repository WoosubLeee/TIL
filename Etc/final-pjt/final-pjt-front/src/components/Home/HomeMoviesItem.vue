<template>
  <div class="movie-item">
    <router-link
      :to="{ name: 'MovieDetail', params: { movie_id: movie.id } }"
      class="d-flex justify-content-center"
    >
      <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" class="poster rounded w-100">
      <div class="movie-text w-100 h-100">
        <div class="text-area text-center">
          <h5 class="mb-1">{{ movie.title }}</h5>
          <span>{{ movie.subtitle }}</span>
          <div class="mt-2">
            <i class="fas fa-star"></i>
            <span>{{ movie.userRating }}</span>
          </div>
          <div class="my-2">
          <span v-for="(genre, index) in genres.slice(0, 3)" :key="index">
            {{ genre }}<span v-if="index !== genres.slice(0, 3).length - 1"> |</span>
          </span>
          </div>
          <p>개봉일 : {{ movie.release_date }}</p>
        </div>
        <div class="text-bg w-100 h-100"></div>
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'HomeMoviesItem',
  props: {
    movie: {
      type: Object
    }
  },
  computed: {
    genres: function () {
      const splited = this.movie.genre_ids.slice(1, -1).split(", ")
      return splited.map(function (genre) {
        return genre.slice(1, -1)
      })
    },
    actors: function () {
      const splited = this.movie.actor.slice(1, -1).split(", ")
      return splited.map(function (actor) {
        return actor.slice(1, -1)
      })
    }
  }
}
</script>

<style scoped>
  .movie-item {
    position: relative;
    width: 213px;
    transition: 0.1s;
    padding: 0.5px;
  }
  .poster {
    height: 315px; 
  }
  .movie-item:hover {
    transform: scale(1.2);
    margin: 0 2%;
    z-index: 999;
  }
  .movie-item:hover .movie-text {
    visibility: visible;
  }
  .movie-text {
    position: absolute;
    visibility: hidden;
    transition: visibility 0.2s;
  }
  .text-area {
    position: absolute;
    width: 100%;
    color: white;
    top: 20%;
    z-index: 20;
  }
  .text-bg {
    position: absolute;
    opacity: 0.5;
    background: black;
  }
</style>