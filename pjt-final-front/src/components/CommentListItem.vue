<template>
  <div id="comment-list">
    <div id="comment">
      <div id="comment-writer">
        <font-awesome-icon class="fa-2xl" icon="fa-solid fa-user" />
        <p>{{comment.user.username}}</p>
      </div>
      <div id="comment-content">
        <span class="me-4" id="comment-title">{{ comment.title }}</span>     
        <span>{{ commentCreatedAt }}</span>
        <p>{{ comment.content }}</p>
      </div>
    </div>
      <button
        id="delete-button"
        class="btn btn-dark btn-sm"
        v-if="isOwner"
        @click=deleteComment(comment.id)
      >
      X
      </button>
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
    },
    commentCreatedAt() {
      const createdDate = new Date(this.comment.created_at)
      const now = new Date()
      const timeDiff = now.getTime() - createdDate.getTime()

      var diffText
      if (timeDiff / (1000 * 60) < 1) {
        diffText = `${parseInt(timeDiff / 1000) }초 전`
      } else if (timeDiff / (1000 * 60 * 60) < 1) {
        diffText = `${parseInt(timeDiff / (1000 * 60)) }분 전`
      } else if (timeDiff / (1000 * 60 * 60 * 24) < 1) {
        diffText = `${parseInt(timeDiff / (1000 * 60 * 60)) }시간 전`
      } else if (timeDiff / (1000 * 60 * 60 * 24 * 30) < 1) {
        diffText = `${parseInt(timeDiff / (1000 * 60 * 60 * 24)) }일 전`
      } else {
        diffText = `${createdDate.getFullYear()}/${createdDate.getMonth()+1}/${createdDate.getDate()}`
      }
      return diffText
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
  display: flex;
  justify-content: space-between;
}

#comment-title {
  font-weight: bold ;
}

#comment-writer {
  display: flex;
  text-align: center;
  align-content: center;
  justify-content: center;
  flex-direction: column;
  width: 60px;
}

#comment {
  display: flex;
}

#delete-button {
  margin-bottom: 50px;
}

#comment-content {
  margin-left: 20px;
}
</style>