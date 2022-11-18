<template>
  <div class="Actor">
    <h1> {{actorname}}가 출연한 영화들</h1>
    <ActorMovieList 
      :actor="actor"
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
      actor: this.$route.params.id,
      actorname: this.$route.params.name
    }
  }
}
</script>
