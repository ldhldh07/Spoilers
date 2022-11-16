import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '@/views/MovieView'
import SignUpView from '@/views/SignUpView'
import LogInView from '@/views/LogInView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'MovieView',
    component: MovieView
  },

  {
    path: '/profile/:id/:username',
    // 각 유저별 username을 넣은 프로필 페이지로 만들어야 함
    // 미인증 시 라우터가드로 로그인 페이지로 이동시킬 것.
    name: 'ProfileView',
    component: () => import('../views/ProfileView.vue')
  },

  {
    path: '/moviedetail/:id',
    name: 'MovieDetailView',
    component: () => import('../views/MovieDetailView.vue')
  },

  {
    path: '/actor/:id',
    name: 'ActorView',
    component: () => import('../views/ActorView.vue')
  },

  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },

  {
    path: '/login',
    name: 'LogInView',
    component: LogInView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
