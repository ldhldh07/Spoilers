import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    movies: [],
    comments: [],
    genres: [],
    token: null,
    user: null,
  },
  getters: {
    isLogIn(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    GET_MOVIES(state, movies) {
      state.movies = movies
    },
    GET_GENRES(state, genres) {
      state.genres = genres
    },
    // 회원가입 && 로그인
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: 'PopularView' })
    },
    GET_USER_DETAIL(state, user) {
      state.user = user
    },
    LOG_OUT(state) {
      state.token = null
      state.user = null
    }
  },
  actions: {
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/movies/`,
      })
        .then((res) => {
          context.commit('GET_MOVIES', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getGenres(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/movies/genres/`,
      })
        .then((res) => {
          context.commit('GET_GENRES', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
        }
      })
      .then((response)=>{
        // console.log(res)
        const key = response.data.key
        context.commit('SAVE_TOKEN', key)
        return key
      })
      .then((key)=> {
        context.dispatch('getUserDetail', key)
      })
      .catch((error)=>{
        console.log(error)
      })
    },
    logIn(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        }
      })
        .then((response)=>{
          // console.log(res)
          const key = response.data.key
          context.commit('SAVE_TOKEN', key)
          return key
        })
        .then((key)=> {
          context.dispatch('getUserDetail', key)
        })
        .catch((error)=>{
          console.log(error)
        })
    },
    getUserDetail(context, key) {
      axios({
        method: 'post',
        url: `${API_URL}/api/accounts/`,
        data: {
          key: key,
        }
      })
        .then((response) => {
          context.commit('GET_USER_DETAIL', response.data)
        })
        .catch((error)=>{
          console.log(error)
        })
    }
  },
  modules: {
  }
})
