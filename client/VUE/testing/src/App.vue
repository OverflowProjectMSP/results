<script>
// импортируем компонент
import HeaderComp from "./components/MainComponents/HeaderComp.vue";
import VidComp from "./components/MainComponents/VidComp.vue";
import FooterComp from "./components/MainComponents/FooterComp.vue"
import HeadComp from "./components/MinorComponents/HeadComp.vue"
import UserInfo from "./components/СomponetsForPages/UserInfo.vue"
import hours from "./components/MinorComponents/hours.vue"
import ModelWindowVue from './components/СomponetsForPages/ModelWindow.vue';
// Описываем компонент
export default {
    components: {
        HeaderComp,
        VidComp,
        FooterComp,
        HeadComp,
        UserInfo,
        hours,
        ModelWindowVue,
    },
    data() {
        return { pass } // А где Олег???
    },
    methods: { pass }
}

</script>
<!-- Вызываем компонент -->
<template>
    <router-link />

    <header-comp />
    <footer-comp />

</template>
<!-- npm run dev прописывай в папке testing -->
<style scoped>
@import url('https://fonts.cdnfonts.com/css/rubik');

html {
    margin: 0;
    background-color: #EEF1F4;
}

main {
    margin: 10px;

}

template {
    font-family: Rubik !important;

}



.t-alig-c {
    text-align: center;
}

.head {
    margin-top: 20px;
}

.ttt {
    user-select: none;
    pointer-events: none;
    opacity: 0.7;

}

/* модальное окно */
.window {
    background-color: #ffffff;
    border: 4px solid #2a2a2a;
    width: 500px;
    height: 300px;
    border-radius: 30px;
    position: absolute;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 50px;
    z-index: 1;
    font-family: "Rubik", sans-serif;

    top: 30%;
    left: 34%;


    margin-left: auto;
    margin-right: auto;

}

.btn {
    width: 170px;
    height: 50px;
    border-radius: 12px;
    border: none;
    background-color: #4200FF;
    color: #fff;
    cursor: pointer;
    font-weight: 600;
    font-size: 16px;
}

.buttons {
    display: flex;
    gap: 20px;
}

.close {
    width: 50px;
    height: 50px;
    background-color: #2a2a2a;
    position: absolute;
    top: 0;
    right: 0;
    border-radius: 0px 16px 0px 16px;

    display: flex;
    justify-content: center;
    align-items: center;
}

.btn-close {
    width: 50px;
    height: 50px;
    border-radius: 16px;
    background: none;
    border: none;
    color: #fff;
    font-size: 22px;
    font-weight: 500;

    cursor: pointer;
}
</style>
