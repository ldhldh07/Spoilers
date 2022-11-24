<template>
  <div id="actormovie" class="d-flex flex-wrap flex-column">
    <div class="d-flex flex-wrap" id="movieitems">
      <MovieListItem
        v-for="movie in nowPage"
        :key="movie.id"
        :movie="movie"
      />
    </div>
    <b-pagination
      v-model="currentPage"
      :total-rows="rows"
      :per-page="perPage"
      aria-controls="movieitems"
      first-number
      last-number
    ></b-pagination>
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem.vue'

export default {
  name:'MovieList',
  components : {
    MovieListItem
  },
  data() {
    return {
      perPage: 24,
      currentPage: 1,
    }
  },
  computed: {
    movies() {
      const array = this.$store.state.movies
      const actorArray = array.filter(movie => movie.starring.includes(Number(this.actor)))
      return actorArray
    },
    nowPage() {
      return this.movies.slice((this.currentPage-1)*this.perPage, this.currentPage*this.perPage)
    },
    rows() {
      return this.movies.length
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