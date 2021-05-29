<template>
  <div>
    <div class="box-office-header d-flex flex-column align-items-center mt-5">
      <h2>내 정보</h2>
      <hr width="200px" class="mt-1 mb-3">
    </div>
    <MyInfoList 
      :myinfo="myinfo"
    />
  </div>
</template>

<script>
import axios from 'axios'
import MyInfoList from './MyInfoList'

export default {
  name: 'MyInfo',
  components: {
    MyInfoList,
  },
  data: function () {
    return {
      myinfo: null,
      username: null,
    }
  },
  created: function () {
    axios.get(`http://127.0.0.1:8000/accounts/myinfo/${this.$store.state.username}/`)
      .then((response) => {
        console.log(response)
        this.myinfo = response.data
      })
      .catch((error) => {
        console.log(error)
      })
  }
}
</script>
<style>
</style>