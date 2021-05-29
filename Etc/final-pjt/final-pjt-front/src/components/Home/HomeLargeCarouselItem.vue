<template>
  <router-link :to="{ name: 'MovieDetail', params: { movie_id: movie.id } }">
    <div class="large-carousel">
      <div class="d-flex">
        <div id="img-area">
          <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`">
        </div>
        <div id="text-area" class="d-flex flex-column justify-content-center">
          <span class="title">{{ movie.title }}</span>
          <span class="english-title">{{ movie.subtitle }}</span>
          <div>
            <span v-for="(genre, index) in genres" :key="index">
              {{ genre }}<span v-if="index !== genres.length - 1"> |</span>
            </span>
          </div>
          <div class="rating">
            <i class="fas fa-star"></i>
            <span>{{ movie.userRating }}</span>
          </div>
          <div>
            출연 : 
            <span v-for="(actor, index) in actors.slice(0, 5)" :key="index">
              {{ actor }}<span v-if="index !== actors.slice(0, 5).length - 1">, </span>
            </span>
          </div>
          <span class="release-date">개봉일 : {{ movie.release_date }}</span>
          <br>
          <p class="overview">{{ movie.overview }}</p>
        </div>
      </div>
      <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" class="bg-img">
    </div>
  </router-link>
</template>

<script>
export default {
  name: 'HomeLargeCarouselItem',
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
  a {
    text-decoration: none;
    color: white;
  }
  .large-carousel {
    position: relative;
    height: 540px;
  }
  .bg-img {
    position: absolute;
    width: 100%;
    top: -30%;
    z-index: -1;
    opacity: 0.25;
  }
  #img-area {
    width: 500px;
  }
  #img-area > img {
    position: relative;
    height: 480px;
    top: 50px;
    left: 70px;
  }
  #text-area {
    position: relative;
    width: 580px;
    left: 80px;
    font-size: 18px;
  }
  .title {
    font-size: 32px;
  }
  .english-title {
    font-size: 20px;
  }
  .rating {
    font-size: 25px;
    margin: 13px 0;
  }
  .overview {
    font-size: 18px;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
  }
  .fa-star {
    color: gold;
  }
</style>