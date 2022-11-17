<template>
  <div>
    <h5>{{ comment.title }}</h5>
    <!-- <p>작성자 : {{comment.user_id}}</p> -->
    <p>{{ comment.content }}</p>
    <p>작성일시 : {{ comment.created_at }}</p>
    <button @click=deleteComment(comment.id)>X</button>
  </div>
</template>
  
<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'


export default {
  name: 'CommentListItem',
  props: {
    comment: Object,
  },
  methods: {
    deleteComment(commentId) {
      axios({
        method: 'delete',
        url: `${API_URL}/api/community/${commentId}`
      })
        .then(() => {
          this.$emit('update-comment-list')
        })
        .catch((error)=> {
          console.log(error)
        })
    }
  }
}
</script>