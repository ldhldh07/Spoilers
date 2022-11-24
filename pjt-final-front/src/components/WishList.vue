<template>
  <div class="d-flex flex-wrap flex-column align-items-start">
    <h4>위시리스트</h4>
    <div id="wishlist">
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
      aria-controls="wishlist"
      first-number
      last-number
    ></b-pagination>
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem.vue'

export default {
  name:'WishList',
  components : {
    MovieListItem,
  },
  data() {
    return {
      perPage: 12,
      currentPage: 1,
    }
  },
  props: {
    user : Object,
  },
  computed: {
    wishList() {
      return this.user?.wish_list.slice((this.currentPage-1)*this.perPage, this.currentPage*this.perPage)
    },
    rows() {
      return this.user?.wish_list.length
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