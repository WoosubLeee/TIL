<template>
  <div>
    <MyListForm/>
    <MyList/>
  </div>
</template>

<script>
import MyListForm from '@/components/MyListForm'
import MyList from '@/components/MyList'

export default {
  name: 'MyMovieList',
  components: {
    MyListForm,
    MyList
  }
}
</script>

<style>

</style>