<template>
  <div id="app">
    <h1>Todo List</h1>
    <h3>Done Count : {{ doneCount }}</h3>
    <h3>Not Done Count : {{ notDoneCount }}</h3>
    <TodoForm/>
    <TodoList/>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import TodoForm from './components/TodoForm'
import TodoList from './components/TodoList'

export default {
  name: 'App',
  components: {
    TodoForm,
    TodoList
  },
  computed: {
    // doneCount: function () {
    //   return this.$store.getters.doneCount
    // }
    // 를 helper를 통해 간단히 구현할 수 있다
    ...mapGetters([
      'doneCount',
      'notDoneCount'
    ])
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
