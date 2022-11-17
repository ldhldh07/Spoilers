<template>
  <div>
    <h4>movielist</h4>
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
  name:'MovieList',
  components : {
    MovieListItem
  },
  computed: {
    movies() {
      return this.$store.state.movies
    }
  },
  props:{
    genre
  }
}
</script>