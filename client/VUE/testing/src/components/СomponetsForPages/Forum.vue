<script>
export default {
    data() {
        return {
            posts: [
                {
                    accountIcon: 'person.svg',
                    accountName: 'Nick Endgy',
                    title: 'Как сделать регистрацию с использованием только JavaScript?',
                    description: 'Подскажите, пожалуйста, как сделать регистрацию пользователя на сайте? Сайт у меня на node.js. Я первый раз такую форму делаю и не знаю какой путь выбрать. Какой вариант лучше? Просто к кнопке "зарегистрироваться" подвязать эвент и в нем делать функцию? Или как-то использовать method="post" у формы?',
                    answers: 28,
                    Decided: true,

                },
                {
                    accountIcon: 'person1.svg',
                    accountName: 'Dave Hogger',
                    title: 'Помогите добавить правильно асинхронную подгрузку тегов при сколе',
                    description: 'Пытаюсь добавить асинхронную подгрузку, но на данный момент она работает не правильно, при первом открытии списка отображается 15 тегов при прокрутке происходит скачек и подгружается еще 10, после закрытия списка и повторного открытия догружаются остальные теги, в чем может быть проблема? (сейчас с бека не приходит длина всех тегов, пока это захардкодил, зная длину 38)',
                    answers: 34,
                    Decided: false,
                },

            ],
            plusImg: 'src/assets/plus.svg',
        }
    }
}
</script>

<template>
    <div class="contant-head mt-3">
        <div class="container-one">
            <div class="name-and-image">
                <img class="forum-image" :src="'src/assets/js.jpg'" alt="">
                <p>JavaScript</p>
            </div>
            <button class="create-post"><img class="plus-icon" :src="plusImg" alt=""><a href="#/Quetion">Создать вопрос</a></button>
        </div>
    </div>
    <div class="contant-post">
        <div class="sort-and-search">
            <div class="cont-search">
                <img width="30" :src="'src/assets/search.svg'" alt=""><input class="search" type="search">
            </div>
            <select class="sort-select form-select" name="sort" id="sort">
                <option value="0">Сортировать</option>
                <option value="1">Новые</option>
                <option value="2">Старые</option>
            </select>
        </div>
        <!-- <div class="hr"></div> -->

        <div class="post" v-for="(post, index) in posts">
            <div class="account">
                <a href="#!"><img class="account-img" :src="'src/assets/' + post.accountIcon" alt="">{{ post.accountName
                    }}</a>
            </div>
            <div class="main-post-and-check">
                <div class="main-post">
                    <h2 class="title">{{ post.title }}</h2>
                    <p class="description">{{ post.description }}</p>
                </div>
                <div class="decided" v-if="post.Decided">
                    <div class="decid"><img width="60" class="decided-img" :src="'src/assets/decided.svg'" alt=""><span
                            class="hover-hidden">Вопрос решён</span></div>
                </div>
            </div>
            <div class="answer">
                <a href="#"><button><img src="../assets/comments.svg" alt=""><span>{{ post.answers }}</span>
                        Ответов</button></a>
            </div>
        </div>

    </div>


</template>

<style scoped>
a {
    text-decoration: none !important;
    color: #fff;
    transition: all 300ms;
}

.contant-head {
    margin-left: 30px;
    margin-right: 30px;
}

.container-one {
    display: flex;
    justify-content: space-between;
    align-items: center;

    /* border-bottom: 3px solid#1d1d1d; */

    width: 100%;
    height: 100px;
    margin-bottom: 50px;
    /* background-color: #b0b0b0; */
}

.name-and-image {
    display: flex;
    align-items: end;
    gap: 30px;
}

.name-and-image img {
    width: 70px;
    border-radius: 50px;
}

.name-and-image p {
    color: #1d1d1d;
    font-size: 30px;
    text-decoration: underline;
    margin: 0;
}

.plus-icon {
    width: 25px;
    margin-right: 10px;
}

.create-post {
    display: flex;
    justify-content: center;
    align-items: center;

    border: none;
    width: 240px;
    height: 55px;
    border-radius: 12px;
    background-color: #4200FF;
    color: #fff;

    font-size: 24px;
    font-weight: 500;

    transition: all 100ms;
}

.title {
    /* width: 55ch;
        overflow: hidden;
        white-space: nowrap;
        text-overflow: ellipsis; */
    margin: 0 !important;
}

.create-post:hover {
    background-color: #2d00aa;
    border-radius: 25px 5px;
}

.create-post:active {
    background-color: #240088;
}

.sort-and-search {
    width: 100%;
    height: 60px;

    display: flex;
    justify-content: space-between;

    margin-bottom: 30px;

}

.cont-search {
    height: 30px;
    position: relative;

    display: flex;
    align-items: center;

}


.search {
    width: 350px;
    padding: 0 20px 0 45px;
    height: 40px;

    border: none;

    border: 2px solid #1d1d1d;
    border-radius: 50px
}

.cont-search img {
    position: absolute;
    margin-left: 10px;
}

.hr {
    width: 100%;
    height: 1px;
    background-color: #1d1d1d;
    border: none;

    margin-bottom: 30px;
}

.sort-select {
    width: 150px;
    height: 40px;
}

.contant-post {
    margin-left: 30px;
    margin-right: 30px;

}

.post {
    width: 100%;
    /* border: 2px solid #1d1d1d; */
    border-radius: 20px;

    background-color: #EEF1F4;




    padding: 10px;
    margin-bottom: 25px !important;

    /* background-color: #cdcdcd */
}




.account-img {
    width: 60px;
    height: 60px;
    border-radius: 50px;
    border: 3px solid #1d1d1d;
    background-color: #fff;
}

.account a {
    width: 200px;
    display: flex;
    align-items: end;
    gap: 15px;

    font-size: 20px;
    color: #1d1d1d;
}

.main-post-and-check {
    width: 100%;
    display: flex;
    align-items: center;
    gap: 60px;
}

.main-post {
    margin-top: 20px;
    width: 90%;
    padding: 10px;

    border: 1px solid #1d1d1d;
    border-radius: 10px;

    /* background-color: #fff2dd; */

    /* background-color: #afafaf; */
}

.answer {
    margin-top: 10px;
}

.answer button {

    background-color: #4200FF;
    border-radius: 12px;
    border: none;
    width: 190px;
    height: 55px;

    color: #fff;
    font-size: 20px;

    transition: all 100ms;
}

.answer button:hover {
    background-color: #2d00aa;
    border-radius: 25px 5px;
}

.answer button:active {
    background-color: #240088;
}

.answer img {
    margin-right: 10px;
    width: 50px;
}

.answer a {
    text-decoration: none;

}


.answer span {
    font-weight: 700
}



.decid {
    position: relative;
    display: inline-block;
    cursor: pointer;
}

.decid .hover-hidden {
    visibility: hidden;
    width: 120px;
    background-color: #4200FF;
    color: #fff;
    text-align: center;
    border-radius: 6px;
    padding: 5px 0;
    position: absolute;
    z-index: 1;
    bottom: 125%;
    left: 50%;
    margin-left: -60px;
    opacity: 0;
    transition: all 100ms;
}

.decid .hover-hidden::after {
    content: "";
    position: absolute;
    top: 100%;
    left: 50%;
    margin-left: -5px;
    border-width: 5px;
    border-style: solid;
    border-color: #4200FF transparent transparent transparent;
}

.decid:hover .hover-hidden {
    visibility: visible;
    opacity: 1;
}

@media ((min-width: 100px) and (max-width: 600px)) {
    .title {
        text-align: start;
    }
}

@media (max-width: 700px) {

    .container-one {
        flex-direction: column;
        align-items: start;
        gap: 30px;
        margin-bottom: 80px;
    }

    .sort-and-search {
        display: flex;
        flex-direction: column;
        gap: 30px;

        margin-bottom: 70px;
    }
}

@media (max-width: 550px) {
    .description {
        display: block;
        width: -webkit-min-content;
        width: -moz-min-content;
        width: min-content;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        width: clamp(300px, 100%, 600ch);
    }
}

@media (max-width: 549px) {
    .main-post-and-check {
        display: flex;
        flex-direction: column;
        gap: 20px;
        align-items: start;

        margin-bottom: 20px;
    }

    .description {
        width: clamp(200px, 100%, 600ch);
    }

    .title {
        font-size: 23px !important;
        text-align: left;
    }
}
</style>

