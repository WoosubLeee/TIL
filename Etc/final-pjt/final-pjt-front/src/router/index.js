import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/components/Home/Home'
import MovieDetail from '@/components/MovieDetail/MovieDetail'
import Recommend from '@/components/Recommend/Recommend'
import ReviewCreate from '@/components/Review/ReviewCreate'
import SignUp from '@/components/Account/SignUp'
import LogIn from '@/components/Account/LogIn'
import MyInfo from '@/components/Account/MyInfo'
import Community from '@/components/Community/Community'
import ReviewDetail from '@/components/ReviewDetail/ReviewDetail'
import ReviewDetailComment from '@/components/ReviewDetail/ReviewDetailComment'


Vue.use(VueRouter)

const routes = [
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/movie/:movie_id',
    name: 'MovieDetail',
    component: MovieDetail
  },
  {
    path: '/recommend',
    name: 'Recommend',
    component: Recommend
  },
  {
    path: '/movie/:movie_id/review/',
    name: 'ReviewCreate',
    component: ReviewCreate
  },
  {
    path: '/movie/:movie_id/review/:review_id',
    name: 'ReviewUpdate',
    component: ReviewCreate
  },
  {
    path: '/account/signup',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/account/login',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/community',
    name: 'Community',
    component: Community
  },
  {
    path: '/review/:review_id',
    name: 'ReviewDetail',
    component: ReviewDetail
  },
  {
    path: '/review/:review_id/comment',
    name: 'ReviewDetailComment',
    component: ReviewDetailComment
  },
  {
    path: '/account/myinfo',
    name: 'MyInfo',
    component: MyInfo
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
