<script>
import SideMenuPost from '../CommentsForPost/SideMenuPost.vue'
export default {
    components: { SideMenuPost },
    data() {
        return {
            lies: [
            {
                title: `Перейдите в нужную папку с помощью команды cd`, //2
                PostImg: `PostImg1`
            },
            {
                title: `Введите команду npm create vue@3 <Имя проекта>`, //3
                PostImg: `PostImg2`
            },
            {
                title: `На всё отвечаете no, просто нажимаете enter`, //4
                PostImg: `PostImg3`
            },
            {
                title: `Выполняем переход в созданную папку`, //5
                PostImg: `PostImg4`
            },
            {
                title: `Выполняем установку vue с помощью команды npm install`, //6
                PostImg: `PostImg5`
            },
            {
                title: `Запускаем проект с помощью команды npm run dev и переходим на сайт который он выдал`, //7
                PostImg: `PostImg6`
            },
            ],
        }
    }
}
</script>


<template>
    <SideMenuPost class="menu position-absolute"/>
    <div class="post-container d-flex flex-column mb-5 justify-content-center mx-5">
        <h2 class="fs-2">Чтобы установить VUE через терминал надо:</h2>
        <ol class="fs-4">
            <li>Установленный Node.js</li>
            <li class="mt-2">Пакетный менеджер npm</li>
        </ol>
        <h3 class="fs-3">Итак: </h3>
        <ol class="fs-4">
            <li v-for="li in lies">
                {{ li.title }} <br>
                <li class="mt-1">Откройте командную строку или консоль в VScode</li>
                <img class="mt-2 mb-1" :src="'src/assets/' + li.PostImg + '.png'">
            </li>
        </ol>
    </div>
</template>

<style scoped>
.post-container {
    margin: 20px 150px;
}
ol li img {
    max-width: 700px;
}

@media (max-width: 768px) {
    .post-container {
        margin: 20px 10px!important;
    }
    ol li img {
    max-width: 310px;
    }
    .menu {
        display: none!important;
    }
}
.menu {
    left: 435px;
}
@media (min-width: 769px) and (max-width: 950px) {
    .post-container {
        margin-right: 15px!important;
        margin-left: 90px!important;
    }
    ol li img {
    max-width: 500px;
    }
    .menu {
        left: 20px;
    }
}
@media (min-width: 950px) and (max-width: 1600px) {
    .menu {
        left: 20px;
    }
}
</style>