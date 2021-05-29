<template>
<div class="d-flex justify-content-center m-4">
    <form @submit.prevent class="border rounded">
      <div class="m-4 ">
        <h1>My Profile</h1><br>
        <div class="mb-3">
          <label for="user-id" class="form-label fs-3">아이디</label><br>
          <label for="user-id" class="form-label fs-5"> {{ myinfo.username }}</label>
        </div>
        <div class="mb-3">
          <label for="date_joined" class="form-label fs-3">가입일</label><br>
          <label for="date_joined" class="form-label fs-5">{{ myinfo.date_joined }}</label>
        </div>
        <div class="mb-3">
          <label for="email" class="form-label fs-3">이메일</label><br>
          <label for="email" class="form-label fs-5">{{ myinfo.email }}</label>
        </div>
      </div>
    </form>
  </div>
  
</template>

<script>
export default {
  name: 'MyInfoList',
  props: {
    myinfo: {
      type: Object
    }
  }
}
</script>

<style>
.myinfo-area {
    width: 100%;
  }
  div {
    color: white;
    text-align: center;
  }
</style>