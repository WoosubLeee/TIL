<template>
  <div>
    <ul v-for="(movie, id) in myMovies" :key="id">
      {{ movie }}
    </ul> 
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'MyList',
  computed: {
    ...mapState([
      'myMovies'
    ])
  }
}
</script>

<style>

</style>