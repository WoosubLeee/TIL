<template>
  <div id="app">
    <h1>App</h1>
    <input type="text" v-model="appNum">
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ childData }}</p>
    <Parent :appData="appNum" @parent-input-change="parentDataChange" @child-input-change="childDataChange"/>
  </div>
</template>

<script>
import Parent from './components/Parent'

export default {
  name: 'App',
  data: function() {
    return {
      appNum: '',
      parentData: '',
      childData: ''
    }
  },
  components: {
    Parent
  },
  methods: {
    parentDataChange: function (inputNum) {
      this.parentData = inputNum
    },
    childDataChange: function (inputNum) {
      this.childData = inputNum
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
