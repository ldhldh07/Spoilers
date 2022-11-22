<template>
  <div class="profile">
    <h1 id="main">{{username}}님의 프로필</h1>
    <WishList/>
  </div>
</template>

<script>
import WishList from '@/components/WishList'

export default {
  name: 'PopularView',
  components: {
    WishList,
  },
  data () {
    return {
      username : this.$route.params.username
    }
  }
}
</script>

<style>
#main{
  font-weight: bold;
}
</style>
