<template>
  <div class="container d-flex justify-content flex-wrap">
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
      if (this.isNew) {
        const orderedDate = array.sort((a,b) => new Date(b.date_opened) - new Date(a.date_opened))
        return orderedDate
      } else {
        const orderedPopularity = array.sort((a,b) => b.popularity - a.popularity)
        return orderedPopularity
      }
    }
  },
  props:{
    isNew: Boolean,
  }
}
</script>