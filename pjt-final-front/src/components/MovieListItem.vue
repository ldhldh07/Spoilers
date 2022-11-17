<template>
    <div>
      <router-link :to="{ name: 'MovieDetailView', params: { id: movie.id } }">
        <img :src="poster" alt="movie-poster" class="thumbnail"> 
        <p>{{ movie.movie_title }}</p>  
      </router-link>
    </div>
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
  .thumbnail {
    width: 20%;
    height: 40%;
  }
  </style>  