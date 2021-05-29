import Vue from 'vue'
import Vuex from 'vuex'
// 새로 고침하더라도 데이터가 없어지지 않도록
import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos: []
  },
  // mutation으로 state(data)를 직접 조작
  mutations: {
    ADD_TODO: function (state, todo) {
      state.todos.push(todo)
    },
    DELETE_TODO: function (state, todo) {
      // splice : index부터 1 자리 만큼만 삭제하고 뒤에 이어 붙인다
      state.todos.splice(state.todos.indexOf(todo), 1)
    },
    UPDATE_TODO: function (state, todoItem) {
      // todoItem에 해당하는 부분의 done만 바꾼다
      state.todos = state.todos.map((todo) => {
        if (todo === todoItem) {
          return { ...todo, done: !todo.done }
        }
        return todo
      })
    }
  },
  // actions -> mutation : commit을 통해
  actions: {
    addTodo: function (context, todo) {
      // commit('ADD_TODO', todo)
      context.commit('ADD_TODO', todo)
    },
    deleteTodo: function ({ commit }, todo) {
      commit('DELETE_TODO', todo)
    },
    updateTodo: function ({ commit }, todo) {
      commit('UPDATE_TODO', todo)
    }
  },
  // computed와 같은 역할
  getters: {
    doneCount: function (state) {
      return state.todos.filter((todo) => {
        return todo.done
      }).length
    },
    notDoneCount: function (state) {
      return state.todos.filter((todo) => {
        return !todo.done
      }).length
    }
  },
  modules: {
  },
  plugins: [
    createPersistedState()
  ]
})
