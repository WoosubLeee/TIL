<template>
  <div class="d-flex justify-content-center">
    <form @submit.prevent class="border rounded">
      <div class="m-4">
        <h2>회원가입</h2>
        <div class="mb-3">
          <label for="user-id" class="form-label">아이디</label>
          <input v-model="credentials.username" type="text" class="form-control" id="user-id">
        </div>
        <div class="mb-3">
          <label for="password" class="form-label">패스워드</label>
          <input v-model="credentials.password" type="password" class="form-control" id="password">
        </div>
        <div class="mb-3">
          <label for="passwordConfirmation" class="form-label">패스워드 확인</label>
          <input v-model="credentials.passwordConfirmation" type="password" class="form-control" id="passwordConfirmation">
        </div>
        <div class="mb-3">
          <label for="email" class="form-label">이메일</label>
          <input v-model="credentials.email" type="email" class="form-control" id="email">
        </div>
        <button @click="signup" class="btn btn-primary my-3">회원가입</button>
        <p>
          이미 회원가입을 하셨나요?
          <router-link :to="{ name: 'LogIn' }">로그인</router-link>
        </p>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'SignUp',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
        email: null,
      }
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials
      })
        .then(() => {
          console.log('회원가입 완료')
          this.$router.push({ name: 'LogIn' })
        })
        .catch(err => {
          console.log(err)
        })
    },
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