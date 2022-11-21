<template>
  <div class="container" id="comment-list">
    <div class="row">
      <div class="col-2" id="comment-writer">
        <font-awesome-icon class="fa-2xl" icon="fa-solid fa-user" />
        <p>{{comment.user.username}}</p>
      </div>
      <div class="col-10">
        <span class="me-4" id="comment-title">{{ comment.title }}</span>     
        <span>{{ comment.created_at }}</span>
        <p>{{ comment.content }}</p>
      </div>
        <button class="btn btn-dark" v-if="isOwner" @click=deleteComment(comment.id)>X</button>
    </div>
    <div class="row d-flex">
      <div class="col-11">
      </div>
      <div class="col-1">
      </div>
    </div>
  </div>
</template>
  
<script src="https://kit.fontawesome.com/7d4867f205.js" crossorigin="anonymous"></script>
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

<style>
#comment-list {
  margin: 5px;
  padding: 5px;
  border-radius: 10px;
}

#comment-title {
  font-weight: bold ;
}

#comment-writer {
  display: flex;
  text-align: center;
  align-content: center;
  flex-direction: column;
}
</style>