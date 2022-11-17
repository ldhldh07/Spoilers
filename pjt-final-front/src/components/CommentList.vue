<template>
  <div>
    <h4>CommentList</h4>
    <CommentListItem
      v-for="comment in comments"
      :key="comment.id"
      :comment="comment"
    />
  </div>
</template>

<script>
import CommentListItem from '@/components/CommentListItem.vue'


export default {
  name:'CommentList',
  props:{
    movieId : Number,
  },
  components : {
    CommentListItem
  },
  data() {
    return {
      title: null,
      content: null,
    }
  },
  computed: {
    comments() {
      return this.$store.state.comments
    },
  },
}
</script>
