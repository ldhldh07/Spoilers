<template>
  <div>
    <h4>CommentList</h4>
    <CommentListItem
      v-for="comment in comments"
      :key="comment.id"
      :comment="comment"
    />
    <p>댓글 작성</p>
    <form @submit.prevent="createComment">
      <label for="title">제목: </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content">내용: </label>
      <textarea
        id="content"
        cols="30"
        rows="10"
        v-model.trim="content"
      >
      </textarea>
      <input type="submit" id="submit">
    </form>
  </div>
</template>

<script>
import CommentListItem from '@/components/CommentListItem.vue'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name:'CommentList',
  props:{
    commentList : Array,
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
      return this.commentList
    },
  },
  methods: {
    createComment() {
      const title = this.title
      const content = this.content
      if (!title) {
        alert('제목 입력해주세요')
      } else if (!content) {
        alert('내용 입력해주세요')
      }
      axios({
        method: 'post',
        url: `${API_URL}/api/community/${this.movieId}/comments/`,
        data: {
          title:title,
          content:content,
        },
        // headers: {
        //   Authorization: `Token ${this.$store.state.token}`
        // },
      })
        .then((response) => {
          console.log(response)
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>