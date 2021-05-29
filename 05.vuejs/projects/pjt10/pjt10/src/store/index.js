import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
import axios from 'axios'
export default new Vuex.Store({
  state: {
    movies: [],
    myMovies: [],
  },
  mutations: {
    SUBMIT: function (state, movie) {
      state.myMovies.push(movie)
    }
  },
  actions: {
    getMovieData: function () {
      axios.get('https://gist.githubusercontent.com/eduChange-hphk/d9acb9fcfaa6ece53c9e8bcddd64131b/raw/9c8bc58a99e2ea77d42abd41376e5e1becabea69/movies.json')
        .then((response) => {
          this.state.movies=response.data
        })
    },
    submit: function ({ commit }, movie) {
      commit('SUBMIT', movie)
    }
  },
  modules: {
  }
})