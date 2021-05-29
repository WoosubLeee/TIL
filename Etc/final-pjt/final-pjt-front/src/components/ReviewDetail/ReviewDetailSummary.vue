<template>
  <div class="summary-area d-flex justify-content-center align-items-center">
    <div class="summary-inner d-flex">
      <img :src="`https://image.tmdb.org/t/p/w500/${comments.movie_poster_path}`" class="rounded-3">
      <div class="summary-description">
        <h1>{{ comments.movie_title }}</h1>
        <h3>{{ comments.movie_subtitle }}</h3>
        <div class="rating-area">
          <i class="fas fa-star"></i>
          <span class="mt-2 mx-2">{{ comments.movie_userRating }}</span>
          <router-link :to="{ name: 'ReviewUpdate', params: { movie_id: comments.movie, review_id: comments.id } }">
            <button class="btn btn-outline-light btn-sm mx-2">수정</button>
          </router-link>
          <button @click="del" class="btn btn-outline-danger btn-sm">삭제</button>
        </div>
        <!-- <div class="button-area">
          <i class="fas fa-pencil-alt"></i>
          <i class="fas fa-heart"></i>
        </div> -->
        <h4 class="my-3">{{ comments.title }} | {{ comments.username }}님</h4>
        <p>{{ comments.content }}</p>
      </div>
    </div>
    <div class="bg-area">
      <img :src="`https://image.tmdb.org/t/p/w500/${comments.movie_poster_path}`" class="bg-img">
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ReviewDetailSummary',
  props: {
    comments: {
      type: Object
    }
  },
  data: function () {
    return {
      movie: null,
      review: null,
    }
  },
  created: function () {
    axios.get(`http://127.0.0.1:8000/movies/${this.$route.params.movie_id}/`)
      .then((response) => {
        this.movie = response.data
      })
      .catch((error) => {
        console.log(error)
      })
    axios.get(`http://127.0.0.1:8000/community/review/${this.$route.params.review_id}/`)
      .then((response) => {
        this.review = response.data
      })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
    setToken : function () { // header 내용에 토큰 붙여주기
      const token = localStorage.getItem('jwt')
      const config = {
         Authorization : `JWT ${token}`
      }
      return config
    },
    del: function () {
      axios({
        method: 'delete',
        headers : this.setToken(),
        url: `http://127.0.0.1:8000/community/review/${this.review.id}/`,
      }).then(() => {
          this.$router.go(-1)
        })
        .catch(err => {
          console.log(err)
        })
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
  .button-area > i {
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