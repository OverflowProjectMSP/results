<script>
import VidQuetions from './components/MainComponents/VidQuetions.vue';

export default {
    components: {
        VidQuetions,
    },

    data() {
        return {
            quetions: [
                {
                    title: `Как создать переменную?`,
                    subscribers: 50,
                    hours: 43,
                    views: 43,
                    answers: 423,
                    language: 'Python',
                    complexity: 'Средне',

                },
                {
                    title: `Как создать переменную?`,
                    subscribers: 50,
                    hours: 43,
                    views: 43,
                    answers: 423,
                    language: 'C++',
                    complexity: 'Средне',
                },
                {
                    title: `Как создать переменную?`,
                    subscribers: 45,
                    hours: 0,
                    views: 43,
                    answers: 423,
                    language: 'Асембелер',
                    complexity: 'Средне',
                },
            ],

        }
    }



}




</script>

<template>
    <div class="quest-menu mt-3">
        <div class="active-container d-flex flex-column p-2">
            <h2>Активные вопросы</h2>
            <p>В данном разделе находятся вопросы, которые ждут именно <b>твоего</b> ответа!</p>
            <div class="select-block d-flex border rounded-3 gap-1 py-0">
                <img class="border-end pe-2 ps-2" src="./assets/image.png" alt="level">
                <select class="form-select border-0">
                    <option value="easy" selected>Лёгкие</option>
                    <option value="middle">Средние</option>
                    <option value="hard">Сложные</option>
                </select>

            </div>
        </div>
    </div>

    <vid-quetions :quetion="quetion" v-for="quetion in quetions" />

</template>

<style scoped>
.quest-menu {
    margin: 0 20% 15px 20%;
}

@media(max-width: 500px) {
    .quest-menu {
        margin: 0;
        margin-bottom: 5px;
    }
}

.select-block {
    width: fit-content;
}

.select-block img {
    background-color: #e7e7e7;
}

.active-container {
    margin-bottom: 40px;

}
</style>
