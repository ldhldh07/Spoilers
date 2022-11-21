<template>
  <div id="actormovie">
    <div class="d-flex flex-wrap">
      <MovieListItem
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
      />
    </div>
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
      const actorArray = array.filter(movie => movie.starring.includes(Number(this.actor)))
      return actorArray
    }
  },
  props:{
    actor: String
  }
}
</script>

<style>
#actormovie {
  margin-bottom: 0px;
}
</style>