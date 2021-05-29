<template>
  <div id="app">
    <NavBar/>
    <div id="site-width">
      <router-view/>
      <footer class="text-center bottom-0">
        <h3>박준 장진우 이우섭</h3>
      </footer>
    </div>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar'

export default {
  name: 'App',
  components: {
    NavBar
  },
  created: function () {
    this.$store.dispatch('movieDataInitialize')
    const token = localStorage.getItem('jwt')
    if (token) {
      this.$store.dispatch('Login')
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: white;
}
#site-width {
  width: 1280px;
  margin: auto;
}
</style>