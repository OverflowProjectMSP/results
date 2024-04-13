<script>
import HeaderCommentsPost from '../CommentsForPost/HeaderCommentsPost.vue';
import MyPostComments from '../CommentsForPost/MyPostComments.vue';
import FooterComments from '../CommentsForPost/FooterComments.vue';
export default {
  components: { HeaderCommentsPost, MyPostComments, FooterComments },
}
</script>

<template>

  <header>
    <HeaderCommentsPost />
  </header>

  <main>
    
    <div class="post">
      <MyPostComments />
    </div>
    <FooterComments />

  </main>

  <footer>
    <!-- <FooterComp /> -->
  </footer>

</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Lato&family=Poppins&family=Roboto&family=Rubik:ital,wght@0,300..900;1,300..900&display=swap');
* {
  margin: 0;
  padding: 0px;
  box-sizing: border-box;
  font-family: 'Rubik';
}
.post {
  padding: 0 170px;
}
main {
  padding: 0 320px;
}
@media (max-width: 1700px) {
  main {
    padding: 0 200px;
  }
  .post {
    padding: 0 100px;
  }
}
@media (max-width: 1200px) {
  main {
    padding: 0 60px;
  }
  .post {
    padding: 0 0;
  }
}
@media (max-width: 950px) {
  main {
    margin: 0 0 !important;
    padding: 0px;
  }
  .post {
    padding: 0 0;
  }
}
</style>