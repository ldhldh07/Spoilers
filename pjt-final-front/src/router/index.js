import Vue from 'vue'
import VueRouter from 'vue-router'
import SignUpView from '@/views/SignUpView'
import PopularView from '@/views/PopularView'
import GenreSelectView from '@/views/GenreSelectView'
import NewestView from '@/views/NewestView'
// import LogInView from '@/views/LogInView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'PopularView',
    component: PopularView
  },

  {
    path: '/new',
    name: 'NewestView',
    component: NewestView
  },

  {
    path: '/genre',
    name: 'GenreSelectView',
    component: GenreSelectView
  },

  {
    path: '/genre/:name',
    name: 'GenreView',
    component: () => import('../views/GenreView.vue')
  },

  // {
  //   path: '/profile/:id/:username',
  //   // 미인증 시 라우터가드로 로그인 페이지로 이동시킬 것.
  //   name: 'ProfileView',
  //   component: () => import('../views/ProfileView.vue'),
  //   beforeEnter(to,from,next) {
  //     //로그인 여부 확인하는 방법 확인해두기
  //     const login = true
  //     if (login === false) {
  //       next({name:'LogInView'})
  //     } else {
  //       next()
  //     }
  //   }
  // },

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
