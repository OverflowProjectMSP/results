<script>
export default {
    props: {
        comments: Array,
    }
}
</script>

<template>
    <div class="comment-wrapper mb-3 mx-5 px-5">
        <h2>Комментарии: </h2>
        <div class="comm-block">
            <div class="comm border border border-dark-subtle p-3 rounded-2 mt-3 w-100" v-for="comment in comments">
                <h4 class="text-decoration-underline">{{ comment.username }}</h4>
                <p :class="{'fw-bold': comment.isBold, 'fst-italic': comment.isItalic}">{{ comment.comment }}</p>
            </div>
        </div>
    </div>
</template>

<style scoped>
@media (max-width: 768px) {
    .comment-wrapper {
        margin: 12px!important;
        padding: 0!important;
    }
}
</style>