<template>
  <div>
    <h1>Detail</h1>
    <img :src="poster" alt="movie-poster" class="poster">
    <p>제목 : {{ movie?.movie_title }}</p>
    <p>개봉일 : {{ movie?.date_opened }}</p>
    <p>장르: </p>
    <p v-for="(genre,index) in movie?.genres_of_movie" :key="`g-${index}`" >
      {{genre.name}}
    </p>
    <p>출연 배우 : </p>
    <div class="d-flex flex-wrap">
      <div v-for="(actor,index) in movie?.starring" :key="index" class="mx-3">
        <router-link :to="{name:'ActorView', params:{name:actor.name, id:String(actor.id)}}" class="text-decoration-none">
          {{ actor.name }}
        </router-link>
      </div>
    </div>
    <p>줄거리 : {{ movie?.overview }}</p>
    <p>트레일러</p>
    <div>
      <iframe 
        id="ytplayer" 
        type="text/html" 
        width="720" 
        height="405"
        :src="trailerSrc"
        frameborder="0" allowfullscreen></iframe>
    </div>
    <b-button v-b-toggle.collapse-1 variant="primary">리뷰영상 보기</b-button>
    <b-collapse id="collapse-1">
      <div class="ratio ratio-16x9 m-5" v-for="(reviewVid,index) in reviewVideos" :key="`r-${index}`">
        <iframe :src="`https://youtube.com/embed/${reviewVid.id.videoId}`" frameborder="0"></iframe>
      </div>
    </b-collapse>
    <br>
    <button v-if="!isWish" class="btn btn-warning" @click="addWishList">위시리스트추가</button>
    <button v-else class="btn btn-warning" @click="addWishList">위시리스트제거</button>
    <CommentList
      :movieId = 'movie?.id'
      :comments = comments
      @update-comment-list="getMovieDetail"
      />
  </div>
</template>

<script>
import CommentList from '@/components/CommentList'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'
const URL = "https://www.googleapis.com/youtube/v3/search"
const API_KEY = "AIzaSyArNN1EdBS-8JxzjJLvBNtA1lRYR7w8MPs"

export default {
  name: 'MovieDetailView',
  components: {
    CommentList,
  },
  data() {
    return {
      movie: null,
      poster: null,
      trailerSrc: null,
      reviewVideos: Array,
    }
  },
  computed: {
    comments() {
      return this.movie?.comment_set
    },
    isWish() {
      const movieId = this.movie?.id
      const userWishList = this.$store.state.user?.wish_list
      return userWishList?.includes(movieId) ? true : false
    },
  },
  created() {
    this.getMovieDetail()
  },
  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/movies/${this.$route.params.id}/`
      })
        .then((res) => {
          this.movie = res.data
          this.reviewSearch(this.movie.movie_title+" 영화 리뷰")
          this.poster = "https://image.tmdb.org/t/p/original" + this.movie.poster_path
          this.trailerSrc = "https://www.youtube.com/embed/" + this.movie.trailer_key
        })
        .catch((err) => {
          console.log(err)
        })
    },
    reviewSearch(movieTitle) {
      axios.get(URL, {
        params: {
          key: API_KEY,
          type: 'video',
          part: 'snippet',
          q: movieTitle
        }
      })
        .then(result =>{
          this.reviewVideos= result.data.items
        })
        .catch(error=> {
        console.log(error)
        })
    },
    addWishList() {
      const movieId = this.movie.id
      const userId = this.$store.state.user.id
      axios({
        method: 'post',
        url: `${API_URL}/api/community/${movieId}/wish/`,
        data: {
          user_id: userId,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
      })
        .then(() => {
          this.getMovieDetail()
          const key = this.$store.state.token
          this.$store.dispatch('getUserDetail', key)
        })
        .catch((error) => {
          console.log(error)
        })
    }
  },
}
</script>


<style>
.poster {
  height: 50rem;
}
</style>