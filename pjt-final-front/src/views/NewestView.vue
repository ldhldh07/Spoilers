<template>
  <div class="popular">
    <h1>최신순 보기</h1>
    <MovieList
      :genre="newest"
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
    return {
      newest: 10
      // 타 장르값과 겹치지 않도록 한다.
    }
  }
}
</script>
