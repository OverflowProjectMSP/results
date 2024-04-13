<script>
import Form from './Form.vue';
export default {
    components: { Form },
    data() {
        return {
            faqs: [
                {
                    question: `Как работает проект UpFollow?`,
                    answer: `Если вам что-нибудь не понятно из курса в мшп, либо же вы создаёте свой проект и зашли 
                в тупик - UpFlow к вашим услугам! Здесь вы можете найти людей, готовых помочь вам в трудную минуту, 
                а если вопрос появится не у вас, то вы всегда можете помочь, ведь вы добрая душа)`,
                    isHide: true
                },
                {
                    question: `Что делать, если на ваш вопрос не дали ответ?`,
                    answer: `Тут не стоит унывать. Подождите больше времени, обычно люди всегда стараются помочь вам, 
                но если не дождётесь ответа в течении суток, можете попробовать опубликовать всё заново. Возможно 
                это поможет)`,
                    isHide: true
                },
                {
                    question: `Как сделать то то то то... lorem`,
                    answer: `Тут не стоит унывать. Подождите больше времени, обычно люди всегда стараются помочь вам, 
                но если не дождётесь ответа в течении суток, можете попробовать опубликовать всё заново. Возможно 
                это поможет)`,
                    isHide: true
                },
                {
                    question: `Как сделать то то то то... lorem`,
                    answer: `Тут не стоит унывать. Подождите больше времени, обычно люди всегда стараются помочь вам, 
                но если не дождётесь ответа в течении суток, можете попробовать опубликовать всё заново. Возможно 
                это поможет)`,
                    isHide: true
                },
                {
                    question: `Как сделать то то то то... lorem`,
                    answer: `Тут не стоит унывать. Подождите больше времени, обычно люди всегда стараются помочь вам, 
                но если не дождётесь ответа в течении суток, можете попробовать опубликовать всё заново. Возможно 
                это поможет)`,
                    isHide: true
                },
                {
                    question: `Как сделать то то то то... lorem`,
                    answer: `Тут не стоит унывать. Подождите больше времени, обычно люди всегда стараются помочь вам, 
                но если не дождётесь ответа в течении суток, можете попробовать опубликовать всё заново. Возможно 
                это поможет)`,
                    isHide: true
                },
                {
                    question: `Как сделать то то то то... lorem`,
                    answer: `Тут не стоит унывать. Подождите больше времени, обычно люди всегда стараются помочь вам, 
                но если не дождётесь ответа в течении суток, можете попробовать опубликовать всё заново. Возможно 
                это поможет)`,
                    isHide: true
                },
            ],
            isHide: true,

            imgClose: 'src/assets/close.svg',
        }
    },
    methods: {
        openAnswer(index) {

            let faq = this.faqs[index];
            faq.isHide = !faq.isHide;

            // this.isHide = !this.isHide;
        }
    }
}
</script>

<template>
    <div class="faq-container d-flex flex-column align-items-center gap-2 px-4 py-2">
        <h1 class="my-2 fw-bold">FAQ: </h1>
        <div class="faq d-flex flex-column border border-dark rounded-3 p-4 mx-5 transition-all"
            v-for="(faq, index) in faqs">
            <div class="quest-block d-flex flex-row justify-content-between mx-2 p-1 align-items-center user-select-none"
                @click="openAnswer(index)">
                <img :class="{ 'rotate-right': faq.isHide }" class="transition-all" :src="imgClose" alt="close">
                <span class="fw-bold fs-3 text-center">{{ faq.question }}</span>
                <img :class="{ 'rotate-left': faq.isHide }" class="transition-all" :src="imgClose" alt="close">
            </div>
            <p class="text-center fs-4" :class="{ 'd-none': faq.isHide }">
                {{ faq.answer }}
            </p>
        </div>
    </div>
    <Form />
</template>

<style scoped>
.faq-container {
    margin: 50px 200px 20px 200px;
}

.faq {
    width: 75%;
}

.faq .quest-block {
    cursor: pointer;
}

.quest-block img {
    transition: all 850ms;
}

.rotate-left {
    rotate: 180deg;
}

.rotate-right {
    rotate: -180deg;
}

@media (max-width: 1024px) {
    .faq-container {
        margin: 17.5px !important;
    }

    .faq {
        width: 100%;
        padding: 12px !important;
    }
}

@media (min-width: 1024px) and (max-width: 1650px) {
    .faq-container {
        margin: 50px 110px 20px 150px !important;
    }

    .faq {
        width: 80%;
        padding: 12px !important;
    }
}
</style>