<template>
  <ul>
    <Todo 
      v-for="(todo, idx) in todos" 
      :key="idx" 
      :todo="todo"
    />
  </ul>
</template>

<script>
import { mapState } from 'vuex'
import Todo from './Todo'

export default {
  name: 'TodoList',
  components: {
    Todo
  },
  computed: {
    // todos: function () {
    //   return this.$store.state.todos
    // }
    // 를 mapState로 축약할 수 있다
    ...mapState([
      'todos'
    ])
  }
}
</script>

<style>

</style>