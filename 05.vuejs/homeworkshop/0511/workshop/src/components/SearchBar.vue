<template>
  <div>
    <input @keyup.enter="searchInput" type="text">
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  methods: {
    searchInput: function (event) {
      // 부모 component에 search-input 이벤트가 발생하도록 하고, event.target.value를 전달한다
      this.$emit('search-input', event.target.value)
    }
  }
}
</script>

<style>

</style>