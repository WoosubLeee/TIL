<template>
  <div class="navbar-bg">
    <nav class="d-flex justify-content-center m-auto">
      <div class="nav-left d-flex">
        <router-link :to="{ name: 'Home' }" id="home-link">
          <i class="fas fa-home fa-2x"></i>
        </router-link>
        <ul class="w-100 d-flex justify-content-evenly my-auto">
          <li>
            <router-link :to="{ name: 'Recommend' }" class="menu">추천</router-link>
          </li>
          <li>
            <router-link :to="{ name: 'Community' }" class="menu">커뮤니티</router-link>
          </li>
        </ul>
      </div>
      <div class="nav-right d-flex">
        <li v-if="isLogin" class="w-100 dropdown d-flex justify-content-center">
          <i class="fas fa-user fa-2x dropdown-toggle" role="button" data-bs-toggle="dropdown"></i>
          <ul class="dropdown-menu">
            <li>
              <router-link :to="{ name: 'MyInfo' }">
                <button class="dropdown-item">내 정보</button>
              </router-link>
            </li>
            <li><hr class="dropdown-divider"></li>
            <li><button @click="logout" class="dropdown-item">로그아웃</button></li>
          </ul>
        </li>
        <div v-else class="w-100 d-flex justify-content-evenly">
          <router-link :to="{ name: 'LogIn' }">로그인</router-link>
          <router-link :to="{ name: 'SignUp' }">회원가입</router-link>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'NavBar',
  computed: {
    ...mapState([
      'isLogin',
    ]),
  },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.$store.dispatch('login')
    }
  },
  methods: {
    logout: function () {
      localStorage.removeItem('jwt')
      this.$store.dispatch('logout')
      this.$router.push({ name: 'Home' })
    }
  }
}
</script>

<style scoped>
  .navbar-bg {
    background-color: rgb(72, 104, 112);
  }
  nav {
    width: 1280px;
    height: 60px;
  }
  a {
    color: white;
    text-decoration: none;
    margin: auto 0;
  }
  li {
    list-style-type: none;
    margin: auto 0;
  }
  .menu {
    font-size: 23px;
  }
  .nav-left {
    width: 780px;
  }
  .nav-right {
    width: 500px;
  }
  #home-link {
    margin: auto 0;
  }
  .form-control {
    width: 250px;
    height: 70%;
    margin: auto 0;
  }
  .dropdown-item {
    color: black;
  }
</style>