<template>
  <li>
    <input v-model=todo.done type="checkbox">
    <!-- map 헬퍼를 사용하면 methods 부분에 인자를 넣을 수 없으므로 아래처럼 호출할 때 인자를 같이 넣어 보낸다 -->
    <span 
      :class="{ done: todo.done }" 
      @click="updateTodo(todo)"
    >
      {{ todo.job }}
    </span>
    <button @click="deleteTodo(todo)">Del</button>
  </li>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'Todo',
  props: {
    todo: {
      type: Object
    }
  },
  methods: {
    ...mapActions([
      'deleteTodo',
      'updateTodo'
    ])
  }
}
</script>

<style scoped>
li {
  list-style-type: none;
}
.done {
  text-decoration: line-through;
}
button {
  margin-left: 10px;
}
</style>