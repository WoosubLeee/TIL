import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
import axios from 'axios'

export default new Vuex.Store({
  state: {
    movies: [],
    isLogin: false,
    username: '',
  },
  mutations: {
    SETUSERNAME(state, username) {
      state.username = username
    },
    LOGIN: function (state) {
      state.isLogin = true
    },
    LOGOUT: function (state) {
      state.isLogin = false
    }
  },
  actions: {
    movieDataInitialize: function () {
      axios.get('http://127.0.0.1:8000/movies')
        .then((response) => {
          this.state.movies = response.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
    login: function ({ commit }) {
      commit('LOGIN')
    },
    logout: function ({ commit }) {
      commit('LOGOUT')
    },
    setUsername: function ({ commit }, info) {
      commit('SETUSERNAME', info.username)
    }
  },
  modules: {
  }
})
