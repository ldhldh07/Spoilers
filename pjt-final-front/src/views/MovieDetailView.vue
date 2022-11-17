<template>
  <div>
    <h1>Detail</h1>
    <p>제목 : {{ movie?.movie_title }}</p>
    <p>개봉일 : {{ movie?.date_opened }}</p>
    <p>출연 배우 : {{ movie?.actors }}</p>
    <p>줄거리 : {{ movie?.overview }}</p>
    <p>트레일러</p>
    <p>리뷰영상</p>
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
        url: `${API_URL}/api/movies/${this.$route.params.id}`
      })
        .then((res) => {
          console.log(res)
          this.movie = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>
