<template>
  <div>
    <h1>Child</h1>
    <input v-model="childNum" @input="childInputChange" type="text">
    <p>appData: {{ appData }}</p>
    <p>ParentData: {{ parentData }}</p>
  </div>
</template>

<script>
export default {
  name: 'Child',
  props: {
    appData: {
      type: String,
      required: true
    },
    parentData: {
      type: String,
      required: true
    }
  },
  methods: {
    childInputChange: function (event) {
      this.$emit('child-input-change', event.target.value)
    }
  }
}
</script>

<style>

</style>