<script>
import axios from 'axios';
axios.defaults.baseURL = 'http://localhost:5234';
export default {
    data() {
        return {
            question: {

            }
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
                    id: id
                }
            });
            this.question = responce.data.get('all');
        }
    }
}
</script>

<template>
<div class="container">
    Never Gonna Give You Up!
</div>
</template>

<style scoped>

</style>