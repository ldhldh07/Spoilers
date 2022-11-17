<template>
  <div class="popular">
    <h1>Spoilers</h1>
    <MovieList/>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList'

export default {
  name: 'PopularView',
  components: {
    MovieList,
  }
}
</script>
