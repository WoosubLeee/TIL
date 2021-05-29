<template>
  <div class="d-flex justify-content-center">
    <form @submit.prevent class="border rounded">
      <div class="m-4">
        <h2 class="text-center">{{ movie.title }}</h2>
        <h5 class="text-center">{{ movie.subtitle }}</h5>
        <div class="my-3">
          <input v-model="title" type="text" class="form-control" placeholder="제목">
        </div>
        <div class="my-3">
          <textarea v-model="content" cols="30" rows="15" class="form-control" placeholder="내용"></textarea>
        </div>
        <button @click="submit" class="btn btn-primary my-3 w-100">작성</button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ReviewCreate',
  data: function () {
    return {
      movie: null,
      review: Object,
      title: '',
      content: '',
      methodType: 'post',
    }
  },
  created: function () {
    axios.get(`http://127.0.0.1:8000/movies/${this.$route.params.movie_id}/`)
      .then((response) => {
        this.movie = response.data
      })
      .catch((error) => {
        console.log(error)
      })
    if (this.$route.params.review_id != undefined) {
      console.log('chechec')  
      axios.get(`http://127.0.0.1:8000/community/review/${this.$route.params.review_id}/`)
        .then((response) => {
          this.review = response.data
          console.log(this.review.title)
          this.title = this.review.title
          this.content = this.review.content
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
  methods: {
    setToken : function () { // header 내용에 토큰 붙여주기
      const token = localStorage.getItem('jwt')
      const config = {
         Authorization : `JWT ${token}`
      }
      return config
    },
    update: function () {
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/community/movies/${this.movie.id}/review/${this.review.id}/`,
        headers : this.setToken(),
        data: {
          title: this.title,
          content: this.content,
          movie: this.movie.id
        }
      }).then(() => {
          this.$router.push({ name: 'MovieDetail', params: { movie_id: this.movie.id } })
        })
        .catch(err => {
          console.log(err)
        })
    },
    submit: function () {
      if (this.review.id != undefined) {
        console.log('post!')
        this.update()
      } else {
        console.log('put!')
       axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/community/movies/' + this.movie.id + '/review/',
        headers : this.setToken(),
        data: {
          title: this.title,
          content: this.content,
          movie: this.movie.id
        }
      }).then(() => {
          this.$router.push({ name: 'MovieDetail', params: { movie_id: this.movie.id } })
        })
        .catch(err => {
          console.log(err)
        }) 
      }
    }
  }
}
</script>

<style scoped>
  form {
    width: 1000px;
    margin: 50px 0;
  }
</style>