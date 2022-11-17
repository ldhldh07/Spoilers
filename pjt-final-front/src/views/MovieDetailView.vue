<template>
  <div>
    <h1>Detail</h1>
    <img :src="poster" alt="movie-poster">
    <p>제목 : {{ movie?.movie_title }}</p>
    <p>개봉일 : {{ movie?.date_opened }}</p>
    <p>장르: </p>
    <p v-for="(genre,index) in movie?.genres_of_movie" :key="`g-${index}`" >
      {{genre.name}}
    </p>
    <p>출연 배우 : </p>
    <p v-for="(actor,index) in movie?.starring" :key="index">
      {{ actor.name }}
      <!-- <router-link :to="{name:'ActorView', params: {id:actor.id }}">{{ actor.name }}</router-link> -->
    </p>
    <p>줄거리 : {{ movie?.overview }}</p>
    <p>트레일러</p>
    <iframe 
      id="ytplayer" 
      type="text/html" 
      width="720" 
      height="405"
      :src="trailerSrc"
      frameborder="0" allowfullscreen></iframe>
    <p>리뷰영상</p>
    <div class="ratio ratio-16x9">
      <iframe :src="videoSrc" frameborder="0"></iframe>
    </div>
    <p>코멘트</p>
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
    }
  },
  computed: {
    comments() {
      return this.movie?.comment_set
    }
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
          console.log(res)
          this.movie = res.data
          this.reviewSearch(this.movie.movie_title+"리뷰")
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
          console.log(result)
          this.videos= result.data.items
          this.selectedVideo1 = this.videos[0].id.videoId
          this.selectedVideo2 = this.videos[1].id.videoId
          console.log(this.selectedVideo1)
        })
        .catch(error=> {
        console.log(error)
        })
    }
  },
  data() {
    return {
      movie: null,
      poster: null,
      trailerSrc: null,
      videos: Array,
      selectedVideo1 : null,
      selectedVideo2 : null,
    }
  },
  computed: {
    videoSrc() {
      return `https://youtube.com/embed/${this.selectedVideo1}`
    } 
  }
}

// array로 갖고와서 여러개 노출시키기
</script>


