<template>
  <div>
    <ul>
      <!-- video를 prop으로 전달 -->
      <VideoListItem 
        v-for="(video, index) in videos" 
        :key="index" 
        :video="video"
        @select-video="selectVideo"
      />
    </ul>
  </div>
</template>

<script>
import VideoListItem from './VideoListItem'

export default {
  name: 'VideoList',
  components: {
    VideoListItem
  },
  props: {
    videos: {
      type: Array
    }
  },
  methods: {
    selectVideo: function (video) {
      this.$emit('select-video', video)
    }
  }
}
</script>

<style>

</style>