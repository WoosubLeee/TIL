<template>
  <div>
    <input v-model="job" @keyup.enter="addTodo" type="text">
    <button @click="addTodo">Add</button>
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  data: function () {
    return {
      job: '',
    }
  },
  methods : {
    addTodo: function () {
      const todo = {
        job: this.job,
        done: false
      }
      // component => action : dispatch를 통해 실행
      if (todo.job.trim()) {
        this.$store.dispatch('addTodo', todo)
      }
      this.job = ''
    }
  }
}
</script>

<style>

</style>