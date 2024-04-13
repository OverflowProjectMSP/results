<script>
export default {
    data() {
        return {
            countLike: 0,
            color: ``,
            countLikeClick: 0,
            countDisLikeClick: 0,

            likes: null,

            favorite: false,
            remindLater: false,


            ArrowUpImg: `src/assets/ArrowUp.svg`,
            ArrowDownImg: `src/assets/ArrowDown.svg`,
            bookmarkImg: `src/assets/bookmark.svg`,
            timeImg: `src/assets/time.svg`,
        }
    },

    computed: {
        count() {
            return this.likes = this.countLike;
        }
    },

    methods: {
        likeUp() {
            if(this.countLikeClick == 0) {
                this.countLike++;
                this.countLikeClick++;
                this.countDisLikeClick = 0;
            } else if(this.countDisLikeClick == 1 && this.countLikeClick == 1) {
                this.countDisLikeClick = 0;
                this.countLikeClick = 0;
            }
            this.chengeColor();
        },
        likeDown() {
            if(this.countDisLikeClick == 0) {
                this.countLike--;
                this.countDisLikeClick++;
                this.countLikeClick = 0;
            } else if(this.countDisLikeClick == 1 && this.countLikeClick == 1) {
                this.countDisLikeClick = 0;
                this.countLikeClick = 0;
            }
            this.chengeColor();
        },
        chengeColor() {
            if(this.countLike > 0) {
                return this.color = `green`;
            } else if(this.countLike == 0) {
                return this.color = `#000`;
            } else if (this.countLike < 0) {
                return this.color = `red`;
            }
        }
    }
}
</script>

<template>
    <div class="menu-container d-flex flex-column align-items-center gap-2 mt-3">
        <button @click="likeUp" class="btn respect-btn up-btn border border-black rounded-circle d-flex justify-conten-center align-items-center p-2">
            <img :src="ArrowUpImg" alt="Up">
        </button>
        <span class="fs-2 fw-bold" :style="{'color': color}">{{ countLike }}</span>
        <button @click="likeDown" class="btn respect-btn down-btn border border-black rounded-circle d-flex justify-conten-center align-items-center p-2">
            <img :src="ArrowDownImg" alt="Down">
        </button>
        <button role="button" class="border-0 rounded-circle bookmark d-flex justify-conten-center align-items-center text-center p-3">
            <img @click="this.favorite = !this.favorite" :src="bookmarkImg" alt="Down">
        </button>
        <button role="button" class="border-0 rounded-circle bookmark d-flex justify-conten-center align-items-center p-3">
            <img @click="this.remindLater = !this.remindLater" :src="timeImg" alt="Down">
        </button>
    </div>
</template>

<style scoped>
.bookmark {
    transition: all 300ms;
}
.bookmark:hover,
.respect-btn:hover {
    background-color: rgb(189, 189, 189);
}
</style>