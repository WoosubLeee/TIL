<template>
  <div>
    <div class="box-office-header d-flex flex-column align-items-center mt-5">
      <h2>리뷰</h2>
      <hr width="200px" class="mt-1 mb-3">
    </div>
    <ReviewDetailSummary
    :comments="comments"/>
    <ReviewDetailComment
    :comments="comments"/>
  </div>
</template>

<script>
import axios from 'axios'
import ReviewDetailSummary from "./ReviewDetailSummary"
import ReviewDetailComment from "./ReviewDetailComment"

export default {
  name: 'ReviewDetail',
  components: {
    ReviewDetailSummary, 
    ReviewDetailComment
  },
  data: function () {
    return {
      comments: undefined
    }
  },
  created: function () {
    axios.get(`http://127.0.0.1:8000/community/review/${this.$route.params.review_id}`)
      .then((response) => {
        this.comments = response.data
        console.log(this.comments)
      })
      .catch((error) => {
        console.log(error)
      })
  }
}
</script>

<style>

</style>