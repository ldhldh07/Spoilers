<template>
  <div>
    <p @click="toggleToPopular" class="popular">인기순</p>
    <p @click="toggelToNew" class="new">최신순</p>
    <div class="container d-flex justify-content flex-wrap">
      <MovieListItem
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem.vue'

export default {
  name:'GenreMovieList',
  data : function() {
    return {
      toggle: true
    }
  },
  components : {
    MovieListItem
  },
  computed: {
    movies() {
      const array = this.$store.state.movies
      const genreArray = array.filter(movie => movie.genres_of_movie.includes(Number(this.genreCode)))
      if(this.toggle) {
        const popularGenreArray = genreArray.sort((a,b) => b.popularity - a.popularity)
        return popularGenreArray
      } else {
        const newestGenreArray = genreArray.sort((a,b) => new Date(b.date_opened) - new Date(a.date_opened))
        return newestGenreArray
      }
    }
  },
  props:{
    genreCode : String
  },
  methods : {
    toggelToNew() {
      this.toggle = false
      const popularbtn = document.querySelector('.popular')
      const newbtn = document.querySelector('.new')
      newbtn.setAttribute('style','  color: #42b983')
      popularbtn.setAttribute('style','  color: black')
    },
    toggleToPopular() {
      this.toggle = true
      const popularbtn = document.querySelector('.popular')
      const newbtn = document.querySelector('.new')
      popularbtn.setAttribute('style','  color: #42b983')
      newbtn.setAttribute('style','  color: black')
    }
  }
}
</script>

<style>
.popular {
  color: #42b983;
}
</style>