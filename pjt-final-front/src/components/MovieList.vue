<template>
  <div class="d-flex flex-wrap">
    <div id="movieitems">
      <MovieListItem
        v-for="movie in movies"
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
      if (this.isNew) {
        const orderedDate = array.sort((a,b) => new Date(b.date_opened) - new Date(a.date_opened))
        return orderedDate.slice((this.currentPage-1)*this.perPage, this.currentPage*this.perPage)
      } else {
        const orderedPopularity = array.sort((a,b) => b.popularity - a.popularity)
        return orderedPopularity.slice((this.currentPage-1)*this.perPage, this.currentPage*this.perPage)
      }
    },
    rows() {
      return this.$store.state.movies.length
    }
  },
  props:{
    isNew: Boolean,
  },
}
</script>

<style>

.pagination {
  margin-right: auto;
  margin-left: auto;
}

.pagination .page-item.disabled .page-link{
  background-color:#333d51;
  color : #f4f3ea;
}

.pagination .page-link {
  background-color: #333d51 ;
  color : #f4f3ea;
}

.pagination .page-item.active .page-link {
  color: #333d51;
  background-color: #d3ac2b;
  border: solid white 1px;
}

</style>