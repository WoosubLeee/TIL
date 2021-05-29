<template>
  <div>
    <h2>로또</h2>
    <button @click="pickNum">Get Lucky Numbers</button>
    <p>로또 번호 {{ $route.params.lottoNum }}개 추천</p>
    <p>{{ pickedNums }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLotto',
  data: function () {
    return {
      pickedNums: [],
    }
  },
  methods: {
    pickNum: function () {
      const nums = _.range(1, 46)
      this.pickedNums = _.sortBy(_.sampleSize(nums, this.$route.params.lottoNum))
    }
  }
}
</script>

<style>

</style>