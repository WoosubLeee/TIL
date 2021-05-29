<template>
  <div id="app">
    <h1>My first youtube project</h1>
    <!-- search-input 이벤트가 SearchBar component로부터 emit되면 search method 실행  -->
    <SearchBar @search-input="search"/>
    <!-- VideoDetail component의 video data(prop)으로 selectedVideo를 보낸다 -->
    <VideoDetail :video="selectedVideo"/>
    <VideoList :videos="searchData" @select-video="sendVideo"/>
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from './components/SearchBar.vue'
import VideoDetail from './components/VideoDetail.vue'
import VideoList from './components/VideoList.vue'

// API_KEY 보안을 위해 .env 활용
// API 키 앞에는 반드시 'VUE_APP_'이 붙어야 한다
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  components: {
    SearchBar,
    VideoDetail,
    VideoList
  },
  data: function () {
    return {
      searchData: [],
      selectedVideo: undefined
    }
  },
  methods: {
    search: function (inputVal) {
      const params = {
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q: inputVal
      }
      axios.get(API_URL, { params })
      .then(res => {
        this.searchData = res.data.items
      })
      .catch(err => {
        console.log(err)
      })
    },
    // VideoList component에서 emit된 video 데이터를 selectedVideo에 할당
    sendVideo: function (video) {
      this.selectedVideo = video
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
