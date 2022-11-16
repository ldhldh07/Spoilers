<template>
  <div>
    <h4>CommentList</h4>
    <MovieListItem
      v-for="comment in commnets"
      :key="comment.id"
      :comment="comment"
    />
  </div>
</template>

<script>
import CommentListItem from '@/components/CommentListItem.vue'

export default {
  name:'CommentList',
  components : {
    CommentListItem
  },
  computed: {
    comments() {
      return this.$store.state.comments
    }
  }
}
</script>