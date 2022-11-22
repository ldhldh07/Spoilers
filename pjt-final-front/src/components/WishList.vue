<template>
  <div class="d-flex flex-wrap flex-column align-items-start">
    <h4>위시리스트</h4>
    <div id="movieitems">
      <MovieListItem
        v-for="movie in wishList"
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
    <h4>지금까지 적은 스포일러</h4>
    {{comments}}
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem.vue'

export default {
  name:'WishList',
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
    wishList() {
      return this.$store.state.user.wish_list
      // 로그인한 유저의 wish_list 데이터를 가져와서 해당 id의 영화 목록 생성
    },
    comments() {
      return this.$store.state.user
    },
    rows() {
      return this.wishList.length
    }
  }
}
</script>

<style>
.pagination {
  margin-right: auto;
  margin-left: auto;
}

</style>