<template>
  <div class="genre">
    <h1>Spoilers</h1>
    <MovieList/>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList'

export default {
  name: 'GenreView',
  components: {
    MovieList,
  },
}
</script>
