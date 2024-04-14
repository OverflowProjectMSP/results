<script>
import axios from 'axios';
axios.defaults.baseURL = 'http://localhost:5234';
export default {
    data() {
        return {
            userInfo: {},
            question: {},
            answers: [],
        }
    },
    mounted() {
        this.loadQuestion();
        setInterval(() => {
            this.loadQuestion();
        }, 20000);
    },
    methods: {
        async loadQuestion() {
            let responce = await axios.get(`/questions`, {
                params: {
                    id: this.question.id
                }
            });
            this.question = responce.data;
        }
    }
}
</script>

<template>
<div class="container">
    Never Gonna Give You Up! {{ question.id }}
</div>
</template>

<style scoped>

</style>