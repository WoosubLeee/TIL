<template>
  <div>
    <h2>점심메뉴</h2>
    <button @click="selectMenu">Pick Lunch</button>
    <p>{{ selected }}</p>
    <hr>
    <input type="text" v-model.number="lottoNum">
    <button @click="getLotto">Get Lotto Nums</button>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLunch',
  data: function () {
    return {
      lunch: ['자장면', '햄버거', '잔치국수'],
      selected: '',
      lottoNum: '',
    }
  },
  methods: {
    selectMenu: function () {
      this.selected = _.sample(this.lunch)
    },
    getLotto: function () {
      this.$router.push({ name: 'TheLotto', params: { lottoNum: this.lottoNum }})
    }
  }
}
</script>

<style>

</style>