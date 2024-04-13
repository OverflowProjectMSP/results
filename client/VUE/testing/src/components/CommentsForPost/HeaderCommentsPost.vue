<script>
import VidComp from '../MainComponents/VidComp.vue';
export default {
  components: { VidComp },
    data() {
        return {
          language: `JavaScript`,
          countLangQuestion: 2,
          countAnswer: 1,

          subscriber: 15,
          date: `5.01.2024 12:31`,
          views: 473,

          langImg: `src/assets/js.jpg`,
          levelImg: `src/assets/level.png`,
        }
    },

    computed: {
      count() {
        return this.views += 1;
      }
    },
}
</script>

<template>
  <div class="wrap">
    <VidComp/>
    <div class="hr"></div>
  </div>
</template>

<style scoped>
.hr {
  border-bottom: 1.1px solid black;
  margin: 0;
  padding: 0!important;
  width: 100%;
}
</style>