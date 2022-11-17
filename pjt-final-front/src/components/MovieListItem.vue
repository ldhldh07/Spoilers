<template>
    <div>
      <router-link :to="{ name: 'MovieDetailView', params: { id: movie.id } }">
        <img src="movie.poster_path" alt="movie-poster">
        <p>{{ movie.movie_title }}</p>  
      </router-link>
    </div>
  </template>
  
  <script>
  export default {
    name: 'MovieListItem',
    props: {
      movie: Object,
    }
  }
  </script>
  
  <style>
  
  </style>  