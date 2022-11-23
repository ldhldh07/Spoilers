<template>
  <div class="container">
    <div class="d-flex justify-content-start" id="divisionbar">
      <font-awesome-icon icon="fa-solid fa-clapperboard" id="justicon"/>
      <span class="align-self-center fs-3">&nbsp;&nbsp;&nbsp;영화 정보</span>
    </div>
    <hr>
    <div class="ratio ratio-16x9">
      <iframe
        id="ytplayer" 
        type="text/html" 
        :src="trailerSrc"
        allowfullscreen
      >
      </iframe>
    </div>
    <div class="row" id="movie-info-box">
      <div class="col-4" id="detail-poster-box">
        <img :src="poster" alt="movie-poster" class="rounded poster">
      </div>
      <div class="col-8" id="movie-title-content">
        <div id="title-wish">
          <h1 id="movie-title"> {{ movie?.movie_title }}</h1>
          <div v-if="isLogIn" @click="addWishList" id="wish-icon" style="cursor: pointer" class="pb-2">
            <font-awesome-icon icon="fa-regular fa-heart" v-if="!isWish" class="fa-2xl"/>
            <font-awesome-icon icon="fa-solid fa-heart" v-else class="fa-2xl"/>
            <span style="white-space:nowrap">wish list</span>
          </div>
        </div>
        <p> {{ movie?.overview }}</p>
        <p>개봉일 : {{ movie?.date_opened }}</p>
        <span>장르: </span>
        <span
          v-for="genre in movie?.genres_of_movie"
          :key="genre.id"
        >
          <router-link :to="{name:'GenreView', params:{genre:genre.name, code:String(genre.id)}}">        
            <span class="badge bg-dark ms-1">
              {{ genre.name }}
            </span>
          </router-link>
        </span>
        <br><br>
        <p>출연 배우 : </p>
        <div class="d-flex flex-wrap">
          <div v-for="actor in movie?.starring" :key="actor.id" class="me-3">
            <router-link :to="{name:'ActorView', params:{name:actor.name, id:String(actor.id)}}" class="text-decoration-none">
              <span id="actorsName">
                {{ actor.name }}
              </span>
            </router-link>
          </div>
        </div>
      </div>
    </div>
    <hr>
    <div class="d-flex justify-content-start" id="divisionbar" v-b-toggle.collapse-1 @click.once="reviewSearch(movie.movie_title+'영화 리뷰')">
      <font-awesome-icon icon="fa-brands fa-youtube" id="icon"/>
      <span class="align-self-center fs-4">&nbsp;&nbsp;&nbsp;리뷰 영상 보기</span>
    </div>
    <b-collapse id="collapse-1">
      <div class="me-1 col-6" v-for="(reviewVid,index) in reviewVideos" :key="`r-${index}`">
        <div class="ratio ratio-16x9">
          <iframe :src="`https://youtube.com/embed/${reviewVid.video_id}`" allowfullscreen></iframe>
        </div>
        <p>{{reviewVid?.channel_name}}
        <p>{{reviewVid?.video_title}}</p>
        <p>{{reviewVid?.video_date}}</p>
        
      </div>
    </b-collapse>
    <hr>
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
import _ from 'lodash'

const API_URL = 'http://127.0.0.1:8000'
const URL = "https://www.googleapis.com/youtube/v3/search"
const API_KEY = "AIzaSyCvN-sRJ2uXtEcwbYqLCvS3NRAoqH70LK4"

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
      reviewVideos: []
    }
  },
  computed: {
    comments() {
      return this.movie?.comment_set
    },
    isLogIn() {
      return this.$store.getters.isLogIn
    },
    isWish() {
      const movieId = this.movie?.id
      const userWishList = this.$store.state.user?.wish_list
      const isWish = userWishList?.some((userWishMovie)=> {
        return movieId === userWishMovie.id
      })
      return isWish ? true : false
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
          this.poster = "https://image.tmdb.org/t/p/original" + this.movie.poster_path
          this.trailerSrc = "https://www.youtube.com/embed/" + this.movie.trailer_key
        })
        .catch((err) => {
          console.log(err)
        })
    },
    reviewSearch(movieTitle) {
      if (this.movie?.reviewvideo_set.length > 0) {
        for (let vid of this.movie?.reviewvideo_set) {
          this.reviewVideos.push(vid)
        }
      } else {
        axios.get(URL, {
          params: {
            key: API_KEY,
            type: 'video',
            part: 'snippet',
            q: movieTitle,
            videoEmbeddable: 'true',
            maxResults: 6
          }
        })
          .then(result =>{
            console.log(result)
            const list = result.data.items
            for (let vid of list) {
              let data = {
                video_title: _.unescape(vid.snippet.title),
                video_id : vid.id.videoId,
                video_date: vid.snippet.publishTime.substr(0,10),
                channel_name: vid.snippet.channelTitle,
                }
              this.reviewVideos.push(data)
              this.saveReview(data)
            }
          })
          .catch(error=> {
          console.log(error)
          })
      }
    },
    saveReview(inputdata) {
      axios({
        method: 'post',
        url: `${API_URL}/api/movies/${this.$route.params.id}/reviews/`,
        data: {
          video_title: inputdata.video_title,
          video_id : inputdata.video_id,
          video_date: inputdata.video_date,
          channel_name: inputdata.channel_name,
        }
      })
        .then((res) => {
          console.log(res)
        })
        .catch((err) => {
          alert(err)
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
  width: 100%;
}

#detail-poster-box {
  border-radius: 10px;
}

#movie-info-box {
  margin-top: 50px;
}

#ytplayer {
  width: 100%;
}

#movie-title {
  margin-bottom: 20px;
}

#title-wish {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

#review-view {
  margin-bottom: 20px;
}

#wish-icon {
  display: flex;
  flex-direction: column;
}

#movie-title-content {
  padding-left: 30px ;
}

#actorsName {
  color: #333d51
}

#icon {
  width: 65px;
  height: auto;
  color: #d42a24;
  cursor: pointer;
}

#justicon {
  width: 60px;
  height: auto;
}

#divisionbar {
  padding-top: 1rem;
  padding-bottom: 1rem;
}

#collapse-1 {
  display: flex;
  flex-wrap: nowrap;

}

</style>