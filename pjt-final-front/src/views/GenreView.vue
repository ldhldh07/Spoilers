<template>
  <div class="genre">
    <h1>{{genre}} 영화</h1>
    <GenreMovieList
      :genre="genre"
    />
  </div>
</template>

<script>
import GenreMovieList from '@/components/GenreMovieList'

export default {
  name: 'GenreView',
  components: {
    GenreMovieList,
  },
  data: function() {
    return {
      genre: this.$route.params.name
    }
  }
}
</script>
