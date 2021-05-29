<template>
  <div>
    <button @click="randomPick">랜덤 픽!</button>
    <h3>{{ pickedMovie.title }}</h3>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  name: 'Random',
  data: function () {
    return {
      pickedMovie: []
    }
  },
  methods: {
    randomPick: function () {
      this.pickedMovie= _.sample(this.$store.state.movies, 1)
      
    }
  }
}
</script>

<style>

</style>