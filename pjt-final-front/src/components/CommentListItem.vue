<template>
  <div>
    <h5>{{comment.title}}</h5>
    <p>작성자 : {{commnet.user_id}}</p>
    <p>{{comment.content}}</p>
    <p>작성일시 : {{comment.created_at}}</p>
  </div>
</template>
  
<script>
export default {
  name: 'CommentListItem',
  props: {
    comment: Object,
  }
}
</script>