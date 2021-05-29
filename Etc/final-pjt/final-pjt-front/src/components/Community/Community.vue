<template>
  <div>
    <div class="box-office-header d-flex flex-column align-items-center mt-5">
      <h2>자유게시판</h2>
      <hr width="200px" class="mt-1 mb-3">
    </div>
    <CommunityReviews
    :reviews="reviews"/>
  </div>
</template>

<script>
import axios from 'axios'
import CommunityReviews from "./CommunityReviews.vue"

export default {
  name: 'Community',
  components: {
    CommunityReviews 
  },
  data: function () {
    return {
      reviews: undefined
    }
  },
  created: function () {
    axios.get('http://127.0.0.1:8000/community/review/')
      .then((response) => {
        this.reviews = response.data
      })
      .catch((error) => {
        console.log(error)
      })
  }
}
</script>

<style>

</style>