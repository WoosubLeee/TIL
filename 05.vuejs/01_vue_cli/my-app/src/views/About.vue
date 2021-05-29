<template>
  <div>
    <h1>this is about page</h1>
    <NewComponent my-message="this is prop data" @child-input-change="parentGetChange"/>
  </div>
</template>

<script>
// import NewComponent from '../components/NewComponent.vue'
import NewComponent from '@/components/NewComponent.vue'
// @ === '/src'

export default {
  name: 'About',
  components: {
    NewComponent
  },
  methods: {
    parentGetChange: function (textInput) {
      console.log(`이것은 하위 컴포터는 NewComponent로부터 받은 ${textInput}입니다`)
    }
  }
}
</script>

<style>

</style>