<template>
  <div class="Actor">
    <h1>This is Actor page</h1>
    <MovieList/>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList'

export default {
  name: 'ActorView',
  components: {
    MovieList,
  }
}
</script>
