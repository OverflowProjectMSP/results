<script>
import axios from 'axios';
axios.defaults.baseURL = 'http://localhost:5234';
export default {
    data() {
        return {
            userInfo: {},
            question: {
                    accountIcon: 'person.svg',
                    accountName: 'Nick Endgy',
                    title: 'Как сделать регистрацию с использованием только JavaScript?',
                    description: 'Подскажите, пожалуйста, как сделать регистрацию пользователя на сайте? Сайт у меня на node.js. Я первый раз такую форму делаю и не знаю какой путь выбрать. Какой вариант лучше? Просто к кнопке "зарегистрироваться" подвязать эвент и в нем делать функцию? Или как-то использовать method="post" у формы?',
                    answers: 28,
                    Decided: true,
                    id: 123,
            },
            answers: [],
        }
    },
    // mounted() {
    //     this.loadQuestion();
    //     setInterval(() => {
    //         this.loadQuestion();
    //     }, 20000);
    // },
    // methods: {
    //     async loadQuestion() {
    //         let responce = await axios.get(`/questions`, {
    //             params: {
    //                 id: id
    //             }
    //         });
    //         this.question = responce.data;
    //     }
    // }
}
</script>

<template>
    <div class="container">
        <div class="content-1">
            <div class="account">
                <img class="accountIcon" :src="'src/assets/' + question.accountIcon" width="70px" alt="">
                <div class="name-ring">
                    <p><span class="name">JavaScript</span><span class="more">+2 ЕЩЁ</span></p>
                    <p>Уровень: <span class="difficult">Легкий</span></p>
                </div>
            </div>
            <div class="title">
                <h3>{{ question.title }}</h3>
                
            </div>
            <div class="about">
                <p>15 подписчиков</p>
                <p>5.01.2024 12:31</p>
                <p>473 просмотра</p>
            </div>
        </div>
        <button class="answer-btn">Ответов: {{ question.answers }}</button>
    </div>
</template>

<style scoped>
.content-1 {
    /* background-color: rgb(225, 225, 225); */
    margin-top: 50px;
    width: 100%;
    height: 250px;

    padding: 19px;

    border: 1px solid #000;
    border-radius: 25px;
}

.account {
    display: flex;
    gap: 12px;
    align-items: center;
}

.accountIcon {
    border-radius: 50px;
    border: 2px solid #1d1d1d;
}

.name {
    font-weight: 700;
    color: #8355E3;
    margin-right: 10px;
}

.name-ring {
    display: flex;
    flex-direction: column;
    gap: 5px;
}

.name-ring p {
    margin: 0;
}

.more {
    color: #3B82F6;
}

.difficult {
    margin-left: 5px;
    color: #1E7200;
}

.title {
    margin: 0 !important; 
    margin-top: 20px !important;

    display: flex;
    justify-content: space-between;
    align-items: center
}

.answer-btn {
    width: 100px;
}

.about {
    display: flex;
    align-items: center;
    gap: 10px;
}

.about p {
    border-right: 2px solid #3B82F6;
    padding-right: 16px;
    color: #3B82F6;
}

.about p:last-child {
    border: none;
}
</style>