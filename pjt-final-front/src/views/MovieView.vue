<template>
  <div class="movie">
    <h1>This is main page.</h1>
    <h3>Spoilers</h3>
    <MovieList/>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList'

export default {
  name: 'MovieView',
  components: {
    MovieList,
  }
}
</script>
