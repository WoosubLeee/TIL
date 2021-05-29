<template>
  <div>
    <input type="text" @keyup.enter="submit">
    <button @click="submit">제출</button>
  </div>
</template>

<script>
export default {
  name: 'MyListForm',
  methods: {
    submit: function (event) {
      this.$store.dispatch('submit', event.target.value)
    }
  },
}
</script>

<style>

</style>