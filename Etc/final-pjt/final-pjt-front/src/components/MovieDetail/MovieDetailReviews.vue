<template>
  <div class="d-flex">
    <div class="rating-area d-flex flex-column justify-content-center align-items-center">
      <div>
        <i class="fas fa-star"></i>
        <span>평점</span>
      </div>
      <span class="ms-2">{{ movie.userRating }}</span>
      <span class="rating-count">(1151)</span>
    </div>
    <div class="review-area">
      <table class="table">
        <thead>
          <tr>
            <th scope="col">제목</th>
            <th scope="col">내용</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(review, index) in movie.review_set.slice(0, 5)" :key="index">
            <td>{{ review.title }}</td>
            <td>{{ review.content }}</td>
          </tr>
        </tbody>
      </table>
      <div v-if="isLogin" class="d-flex justify-content-end">
        <router-link :to="{ name: 'ReviewCreate', params: { movie_id: movie.id } }">
          <button class="btn btn-outline-light btn-sm">리뷰 작성</button>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'ReviewList',
  props: {
    movie: {
      type: Object
    }
  },
  computed: {
    ...mapState([
      'isLogin'
    ])
  }
}
</script>

<style scoped>
  .rating-area {
    width: 480px;
    font-size: 32px;
  }
  .rating-count {
    font-size: 20px;
  }
  .review-area {
    width: 100%;
  }
  th {
    color: white;
    font-size: 18px;
  }
  td {
    color: white;
    text-align: center;
  }
</style>