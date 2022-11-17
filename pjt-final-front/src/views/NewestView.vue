<template>
  <div class="popular">
    <h1>최신순 보기</h1>
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
  data: function() {
    return{
      isNew: true
    }
  },
}
</script>
