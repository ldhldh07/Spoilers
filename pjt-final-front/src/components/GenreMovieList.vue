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
  name:'GenreMovieList',
  components : {
    MovieListItem
  },
  computed: {
    movies() {
      const array = this.$store.state.movies
      const result = array.filter(movie => movie.genres_of_movie.includes(this.genre))
      return result
    }
  },
  props:{
    genre: String
  }
}
</script>