<template>
  <div>
    <h4>GenreList</h4>
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
    }
  }
}
</script>