import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/components/Home.vue'
import Random from '@/components/Random.vue'
import MyMovieList from '@/components/MyMovieList.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/random/',
    name: 'Random',
    component: Random
  },

  {
    path: '/mymovielist/',
    name: 'MyMovieList',
    component: MyMovieList
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
