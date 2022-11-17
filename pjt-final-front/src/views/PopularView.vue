<template>
  <div class="popular">
    <h1>인기순 보기</h1>
    <MovieList
      :isNew="isNew"
    />
  </div>
</template>

<script>
import MovieList from '@/components/MovieList'

export default {
  name: 'PopularView',
  components: {
    MovieList,
  },
  created() {
    this.getMovies()
  },
  data: function() {
    return{
      isNew: false
    }
  },
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    }
  }

}
</script>
