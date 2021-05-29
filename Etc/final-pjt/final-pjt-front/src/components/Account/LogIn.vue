<template>
  <div class="d-flex justify-content-center">
    <form @submit.prevent class="border rounded">
      <div class="m-4">
        <h2>로그인</h2>
        <p class="mb-3">
          아이디가 없으신가요?
          <router-link :to="{ name: 'SignUp' }">회원가입</router-link>
        </p>
        <div class="mb-3">
          <label for="user-id" class="form-label">아이디</label>
          <input v-model="credentials.username" type="text" class="form-control" id="user-id">
        </div>
        <div class="mb-3">
          <label for="password" class="form-label">패스워드</label>
          <input v-model="credentials.password" type="password" class="form-control" id="password">
        </div>
        <button @click="login" class="btn btn-primary mt-3">로그인</button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LogIn',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null
      }
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: this.credentials
      })
        .then((res) => {
          localStorage.setItem('jwt', res.data.token)
          this.$store.dispatch('login')
          this.$store.dispatch('setUsername', {
            username: this.credentials.username
          })
          this.$router.push({ name: 'Home' })
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>

<style scoped>
  form {
    width: 500px;
    margin: 50px 0;
  }

  button {
    width: 100%;
  }

</style>