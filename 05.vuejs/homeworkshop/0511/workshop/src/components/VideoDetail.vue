<template>
  <!-- video data가 빈 데이터가 아닐 때 -->
  <div v-if="video">
    <!-- computed의 videoURL 값을 src로 -->
    <iframe :src="videoURL" frameborder="0"></iframe>
    <hr>
    <h3>{{ video.snippet.title }}</h3>
    <p>{{ video.snippet.description }}</p>
  </div>
</template>

<script>
export default {
  name: 'VideoDetail',
  // 부모 객체인 App.vue로부터 video값을 내려받는다
  props: {
    video: {
      type: Object
    }
  },
  computed: {
    videoURL: function () {
      // video data가 빈 데이터가 아닐 때(input값이 입력되고 enter키가 눌려졌을 때)
      if (this.video) {
        return `https://www.youtube.com/embed/${this.video.id.videoId}`
      }
      return ''
    }
  }
}
</script>

<style>

</style>