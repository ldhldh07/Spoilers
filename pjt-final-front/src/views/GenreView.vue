<template>
  <div class="genre">
    <h1>{{genre}} 영화</h1>
    <MovieList
      :genre="genre"
    />
  </div>
</template>

<script>
import MovieList from '@/components/MovieList'

export default {
  name: 'GenreView',
  components: {
    MovieList,
  },
  data: function() {
    return {
      genre: this.$route.params.name
    }
  }
}
</script>
