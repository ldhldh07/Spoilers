<template>
  <div>
    <h4>WishList</h4>
    <MovieListItem
      v-for="movie in movies"
      :key="movie.id"
      :movie="movie"
    />
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem.vue'

export default {
  name:'WishList',
  components : {
    MovieListItem
  },
  computed: {
    movies() {
      return this.$store.state.movies
      // 로그인한 유저의 wish_list 데이터를 가져와서 해당 id의 영화 목록 생성
    }
  }
}
</script>