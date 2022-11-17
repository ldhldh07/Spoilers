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
      const array = this.$store.state.movies
      return array
    }
  },
  props:{
    isNew: Boolean,
  }
}
</script>