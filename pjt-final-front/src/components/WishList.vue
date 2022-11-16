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
    }
  }
}
</script>