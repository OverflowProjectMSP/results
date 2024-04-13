<script>
import FooterUserComments from '../CommentsForPost/FooterUserComments.vue';
export default {
    components: { FooterUserComments },
    data() {
        return {
            comments: [],
            countLike: 12,
            countDisLike: 4,

            comment: ``,

            isBold: false,
            isItalic: false,

            error: ``,
            hideError: true,

            countLikeClick: 0,
            countDisLikeClick: 0,

            valid: ``,
        }
    },

    methods: {
        addComment() {
            if(this.comment.length >= 4) {
            this.comments.push({
                username: `Аноним`,
                comment: this.comment,
                isBold: this.isBold,
                isItalic: this.isItalic,
            });
            this.comment = ``;
            this.hideError = !this.hideError;
            this.valid = `green`;
            this.error = `Добавленно!`;
            setTimeout(() => {
                this.error = ``;    
                this.hideError = !this.hideError;
            }, 1250);
            } else {
                this.hideError = !this.hideError;
                this.valid = `rgb(218, 40, 40)`;
                this.error = `Сообщение должно быть больше 4 символов!`;
            }
        },

        Like() {
            if(this.countLikeClick == 0) {
                this.countLike++;
                this.countLikeClick++;
            } else if(this.countLikeClick == 1) {
                this.countLike--;
                this.countLikeClick = 0;
            }
        },

        Dislike() {
            if(this.countDisLikeClick == 0) {
                this.countDisLike++;
                this.countDisLikeClick++;
            } else if(this.countDisLikeClick == 1) {
                this.countDisLike--;
                this.countDisLikeClick = 0;
            }
        }
    }
}
</script>

<template>
<div class="comment-container mx-5 my-2 p-5">
    <div class="info-block d-flex flex-row justify-content-between align-items-center">
        <h4>Оставь коментарий на этот пост</h4>
        <div class="likes d-flex align-items-center gap-1 user-select-none">
            <div class="like d-flex align-items-center">
                <img @click="Like" role="button" :src="'src/assets/LikeImg.png'" alt="Like">
                <span class="fw-bold fs-4 me-4 ms-2">{{ countLike }}</span>
            </div>
            <div class="dislike d-flex align-items-center">
                <img @click="Dislike" role="button" :src="'src/assets/dislikeImg.png'" alt="">
                <div type="text" class="fw-bold fs-4 ms-2 div">{{ countDisLike }}</div>
            </div>
        </div>
    </div>
    <textarea v-model="comment" class="comment-input w-100 rounded-4 p-3 border-dark-subtle fs-4 mt-3" cols="20" rows="10" 
    placeholder="Оставь свой комментарий" :class="{'fw-bold': isBold, 'fst-italic': isItalic}"></textarea>
    <div class="error fs-4 fw-medium transition-all" type="text" :style="{'color': valid}" :class="{'opacity-0': hideError}">{{ error }}</div>
    <div class="wrapper d-flex justify-content-between align-items-center my-2 gap-3">
        <div class="btn-class-container border border-dark-subtle fs-3 rounded-2 d-flex">
            <span @click="this.isBold = !this.isBold" role="button" class="word fw-bold border-end p-3 px-4 user-select-none">B</span>
            <span @click="this.isItalic = !this.isItalic" role="button" class="word fst-italic border-end p-3 user-select-none px-4">i</span>
            <span role="button" class="word border-end p-3 px-4 user-select-none">...</span>
        </div>
        <button @click="addComment()" type="submit" class="btn send-btn btn-outline-primary p-4 fs-4">Отправить!</button>
    </div>
</div>
<FooterUserComments :comments="comments"/>
</template>

<style scoped>
.btn-class-container {
    width: fit-content; 
}
.likes img {
max-width: 35px;
}
.like > span {
    color: #4AA800;
}
.div {
    color: rgb(218, 40, 40);
}
.error {
    color: rgb(218, 40, 40);
}
@media (max-width: 768px) {
    .comment-container {
        margin: 5rem 1.5rem!important;
    }
    .info-block {
        flex-direction: column!important;
        align-items: start!important;
    }
    .word {
        padding: 6px 15px!important;
    }
    .send-btn {
        padding: 10px 10px!important;
        font-size: 20px!important;
    }
    .comment-container {
        margin: 0!important;
        padding: 20px!important;
    }
}
</style>