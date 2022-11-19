<template>
  <div>
    <h5>{{ comment.title }}</h5>
    <p>{{ comment.content }}</p>
    <p>작성자 : {{comment.user.username}}</p>
    <p>작성일시 : {{ comment.created_at }}</p>
    <button v-if="isOwner" @click=deleteComment(comment.id)>X</button>
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
  computed: {
    isOwner() {
      return this.$store.state.user?.id === this.comment.user.id ? true : false
    }
  },
  methods: {
    deleteComment(commentId) {
      axios({
        method: 'delete',
        url: `${API_URL}/api/community/${commentId}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
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