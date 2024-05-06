<script>
import axios from 'axios';
export default {
    data() {
        return {
            form: {
                Name: ``,
            }
        }
    },

    methods: {
        async putInfo() {
            await axios.put('/account-info', {
                form: this.form,
            });
        }
    }
}
</script>
<template>
    <div class="container mb-3">
        <div class="row pt-5">
            <div class="col-3">
                <h3>Настройки профиля</h3>
            </div>
        </div>
        <hr>
        <div class="ancet d-flex" style="display: flex; gap: 40px;">
            <h5 role="button" class="mb-0" style="color: gray; font-weight: 400;"><a href="#/ProfileSettings">Анкета</a></h5>
            <h5 role="button" class="mb-0 border-bottom border-2 border-dark"><a href="#/AccauntSettings">Аккаунт</a></h5>
        </div>
        <hr>
        <h2 class="text-center mt-4 mb-3">Смена пароля</h2>
        <div class="password-container">
            <h5>Старый пароль</h5>
            <div class="input-group mb-3">
                <input type="text" class="form-control" v-model="n">
            </div>
            <h5 class="mt-4">Новый пароль</h5>
            <div class="input-group mb-3">
                <input type="text" class="form-control" v-model="n">
            </div>
            <h5 class="mt-4">Повторите новый пароль</h5>
            <div class="input-group mb-5">
                <input type="text" class="form-control" v-model="n">
            </div>
        </div>
        <hr>
        <h2 class="text-center mt-4">Смена почты</h2>
        <div class="email-container">
            <h5 class="mt-4">Новый адрес почты</h5>
            <div class="input-group mb-5">
                <input type="text" class="form-control" v-model="n">
            </div>
        </div>
        <div class="d-flex justify-content-start mt-5 ms-0">
            <button class="btn btn-outline-success w-fit ms-0" @click="putInfo" type="submit"><b>Сохранить изменения</b></button>
        </div>
    </div>
</template>
<style scoped>
select {
    padding: 7.5px 15px 7.5px 2px;
    border-radius: 3px;
    transition: all 300ms;
}

select:hover {
    border-color: blue;
}

@media (max-width: 960px) {
    .place-container {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: 15px !important;
    }

    .s-place {
        margin-left: 0 !important;
        max-width: 100%;
    }

    .country-select {
        width: 100% !important;
    }
}

@media (max-width: 540px) {
    .place-container {
        align-items: center;
    }

    .save-btn-block {
        width: 100%;
        text-align: center
    }

    .acent {
        margin-right: 60px !important;
    }

    .contact-input {
        margin-left: 12px !important;
    }
}

@media (max-width: 360px) {
    .country-select {
        max-width: 310px !important;
    }

    .s-place {
        margin-left: 0 !important;
        max-width: 310px;
    }
}
</style>