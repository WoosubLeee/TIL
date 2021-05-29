<template>
  <div class="d-flex">
    <div class="comment-area">
      <hr>
      <table class="table">
        <tbody>
          <tr class="fw-bold">
            <td>댓글</td>
            <td>작성자</td>
            <td></td>
          </tr>
          <tr v-for="comment in review.comment_set" :key="comment">
            <td>{{ comment.content }}</td>
            <td>{{ comment.username }}</td>
            <td><button @click="del(comment.id)" class="btn btn-outline-danger btn-sm">삭제</button></td>
          </tr>
        </tbody>
      </table>
      <hr>
      <div class="d-flex justify-content-center mb-4">
        <input @keyup.enter ="submit" v-model="content" type="text" class="border rounded mx-2 mt-1" id="comment_content">
        <button @click="submit" class="btn btn-outline-light mx-2 fw-bold">등록</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ReviewDetailComment',
  // props: {
  //   review: {
  //     type: Object
  //   }
  // },
  data: function () {
    return {
      review: null,
      content: '',
    }
  },
  created: function () {
    axios.get(`http://127.0.0.1:8000/community/review/${this.$route.params.review_id}/`)
      .then((response) => {
        console.log('res')
        this.review = response.data
        console.log('created')
        console.log(this.review.id)
      })
      .catch((error) => {
        console.log(error)
      })
  },
  methods: {
    update: function () {
    axios.get(`http://127.0.0.1:8000/community/review/${this.$route.params.review_id}/`)
      .then((response) => {
        console.log('res')
        this.review = response.data
        console.log('created')
        console.log(this.review.id)
      })
      .catch((error) => {
        console.log(error)
      })
  },
    setToken : function () { // header 내용에 토큰 붙여주기
      const token = localStorage.getItem('jwt')
      const config = {
         Authorization : `JWT ${token}`
      }
      return config
    },
    submit: function () {
      axios({
        method: 'post',
        headers : this.setToken(),
        url: `http://127.0.0.1:8000/community/review/${this.review.id}/comment/`,
        data: {
          content: this.content,
        }
      })
        .then((res) => {
          console.log(res.data.content)
          console.log(this.review.id)
          // this.$router.push({ name: 'ReviewDetail', params: { review_id: this.review.id } })
          this.update()
          console.log(this.review.id)
        })
        .catch(err => {
          console.log(err)
        })
    },
    del: function (comment_id) {
      axios({
        method: 'delete',
        headers : this.setToken(),
        url: `http://127.0.0.1:8000/community/review/${this.review.id}/comment/${comment_id}`,
      }).then(() => {
          // this.$router.go(0)
          this.update()
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}

</script>

<style scoped>
.comment-area {
    width: 100%;
  }
  td {
    color: white;
    text-align: center;
  }
</style>