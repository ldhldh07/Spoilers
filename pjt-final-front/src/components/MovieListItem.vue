<template>
  <b-card class="text-center moviecard">
    <router-link :to="{ name: 'MovieDetailView', params: { id: movie.id } }" class="text-decoration-none">
      <b-card-img :src="poster" alt="movie-poster" class="card-img-top"></b-card-img>
      <b-card-title> {{movie.movie_title}} </b-card-title>
    </router-link>
  </b-card>
</template>
  
<script>
export default {
  name: 'MovieListItem',
  props: {
    movie: Object,
  },
  data: function() {
    return {
      poster: "https://image.tmdb.org/t/p/original" + this.movie.poster_path
    }
  }
}
</script>

<style>
.thumbnail{
  height: 20rem;
  object-fit: scale-down;
}

.moviecard{
 width: 200px; 
 margin: 6px;
}

</style>
