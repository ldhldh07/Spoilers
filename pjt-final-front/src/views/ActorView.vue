<template>
  <div class="Actor">
    <h1>This is Actor page</h1>
    <ActorMovieList 
      :genre="actor"
    />
  </div>
</template>

<script>
import ActorMovieList from '@/components/ActorMovieList'

export default {
  name: 'ActorView',
  components: {
    ActorMovieList,
  },
  data: function() {
    return {
      actor: this.$router.params.id
    }
  }
}
</script>
