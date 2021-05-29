<template>
  <div class="d-flex">
    <div class="review-area">
      <table class="table">
        <tbody>
          <tr class="fw-bold">
            <td>번호</td>
            <td>영화</td>
            <td>리뷰</td>
            <td>작성자</td>
          </tr>
          <tr v-for="review in reviews" :key="review">
            <td>{{ review.id }}</td>
            <td><router-link :to="{ name: 'MovieDetail', params: { movie_id: review.movie } }" class="text-decoration-none text-white">{{ review.movie_title }}</router-link></td>
            <td><router-link :to="{ name: 'ReviewDetail', params: { review_id: review.id } }" class="text-decoration-none text-white">{{ review.title }}</router-link></td>
            <td>{{ review.username }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CommunityReviews',
  props: {
    reviews: {
      type: Object
    }
  },
}

</script>

<style scoped>
.review-area {
    width: 100%;
  }
  td {
    color: white;
    text-align: center;
  }
</style>