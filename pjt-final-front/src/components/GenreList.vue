<template>
  <div>
    <h4>GenreList</h4>
    <!-- 드롭다운하여 장르를 선택 -->
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
  name:'GenreList',
  components : {
    MovieListItem
  },
  computed: {
    movies() {
      return this.$store.state.movies
      // 드롭다운에서 선택된 장르를 지닌 영화들로 리스트 생성 후 state에 저장
    }
  }
}
</script>