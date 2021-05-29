<template>
  <div>
    <h1>Parent</h1>
    <input v-model="parentNum" @input="parentInputChange" type="text">
    <p>appData: {{ appData }}</p>
    <p>childData: {{ childData }}</p>
    <Child :appData="appData" :parentData="parentNum" @child-input-change="childDataChange"/>
  </div>
</template>

<script>
import Child from './Child'

export default {
  name: 'Parent',
  data: function () {
    return {
      parentNum: '',
      childData: ''
    }
  },
  components: {
    Child
  },
  props: {
    appData: {
      type: String,
      required: true
    }
  },
  methods: {
    parentInputChange: function (event) {
      this.$emit('parent-input-change', event.target.value)
    },
    childDataChange: function (inputNum) {
      this.childData = inputNum
      this.$emit('child-input-change', inputNum)
    }
  }
}
</script>

<style>

</style>