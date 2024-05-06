<script>
import axios from 'axios';
export default {
    data() {
        return {
            form: {
                Name: ``,
                SurName: ``,
                interestings: ``,
                about: ``,
                contactsType: ``,
                contacts: ``,
                Country: ``,
                Region: ``,
                City: ``,
            }
        }
    },
    
    methods: {
        async putInfo() {
            await axios.put('/user-info', {
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
            <h5 role="button" class="mb-0 border-bottom border-2 border-dark"><a href="#/ProfileSettings">Анкета</a></h5>
            <h5 role="button" class="mb-0" style="color: gray; font-weight: 400;"><a href="#/AccauntSettings">Аккаунт</a></h5>
        </div>
        <hr>
        <div class="main-block d-flex flex-row gap-4 mt-2">
            <hr class="hr-down">
            <div class="image-block">
                <div class="d-flex flex-column justify-content-center">
                    <div style="text-align: center;">
                        <img :src="'src/assets/profileDefaultImg.png'" class="mb-2" alt="Фото профиля" style="height: 100px;">
                        <p style="color: gray;">Ваша фотография.</p>
                        <p style="color: gray;">Размер загружаемой фотографии <br> не должен быть более 2 МБ.</p>
                        <button class="btn btn-outline-primary" style="margin-right: 10px;" type="file">Загрузить</button>
                        <button class="btn btn-outline-secondary">Удалить</button>
                    </div>
                </div>
            </div>
            <div class="info-block">
                <div class="row">
                    <div class="col-6">
                        <div>
                            <h5>Имя</h5>
                            <div class="input-group mb-3">
                                <input type="text" class="form-control" v-model="form.Name">
                            </div>
                        </div>
                    </div>
                    <div class="col-6">
                        <div>
                            <h5>Фамилия</h5>
                            <div class="input-group mb-3">
                                <input type="text" class="form-control" v-model="form.SurName">
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-12">
                        <h5>Интересы</h5>
                        <div class="input-group mb-3">
                            <input type="text" class="form-control" aria-label="Interests"
                                aria-describedby="basic-addon1" v-model="form.interestings">
                        </div>
                    </div>
                </div>
                <hr>
                <div class="row">
                    <div class="col-12">
                        <h5>О себе</h5>
                        <div class="input-group mb-3">
                            <textarea type="text" class="form-control" placeholder="" aria-label="About"
                                aria-describedby="basic-addon1" style="height: 150px;" v-model="form.about"></textarea>
                        </div>
                    </div>
                </div>
                <div class="row contact-container">
                    <h5>Контакты</h5>
                    <div class="col-12" style="display: flex;">
                        <select role="button" class="contact-select mb-3" v-model="form.contactsType">
                            <option value="email">E-mail</option>
                            <option value="Telegram">Telegram</option>
                            <option value="Skype">Skype</option>
                            <option value="Discord">Discord</option>
                            <option value="Facebook">Facebook</option>
                            <option value="Telephone">Telephone</option>
                        </select>
                        <input type="text" class="form-control contact-input mb-3" aria-label="About"
                            aria-describedby="basic-addon1" style="margin-left: 30px;" v-model="form.contacts">
                    </div>
                </div>
                <div class="row pt-2">
                    <div class="col-2">
                        <button id="add">Добавить</button>
                    </div>
                </div>
                <div class="pt-4">
                    <h5>Местоположение</h5>
                    <div class="row place-container gap-3" style="display: flex;">
                        <select style="width: 350px;" role="button" class="country-select col-12 ms-2 w-50" v-model="form.Country">
                            <option value="Russia" selected>Россия</option>
                            <option value="Belarus">Белоруссия</option>
                            <option value="Germany">Германия</option>
                            <option value="China">Китай</option>
                            <option value="Japan">Япония</option>
                            <option value="USA">США</option>
                            <option value="UK">Великобритания</option>
                        </select>
                        <input type="text" class="s-place col-12 ms-2 w-50" placeholder="Регион" v-model="form.Region">
                        <input type="text" class="s-place col-12 ms-2 w-50" placeholder="Город" v-model="form.City">
                    </div>
                </div>
                <div class="d-flex justify-content-start mt-4 ms-0">
                    <button class="btn btn-outline-success w-fit ms-0" @click="putInfo" type="submit"><b>Сохранить изменения</b></button>
                </div>
            </div>
        </div>
    </div>
</template>
<style scoped>
#download,
#save {
    background-color: white;
    color: #7ac97a;
    border-color: #90EE90;
    border-radius: 5px;
    padding-right: 15px;
    padding-left: 15px;
    text-align: center;
    transition: all 300ms;
    padding: 10px 25px;
}

#save:hover,
#download:hover {
    background-color: #90EE90 !important;
    color: #2c2c2c;
}

#add:hover {
    color: #000000;
}

#delete,
#add {
    background-color: white;
    border: none;
    color: gray;
    transition: all 300ms;
}

#delete:hover {
    color: #000;
}

#preview {
    background-color: white;
    color: #D3D3D3;
    border-color: #D3D3D3;
    border-radius: 5px;
    padding-right: 15px;
    padding-left: 15px;
    text-align: center;
}

select {
    padding: 7.5px 15px 7.5px 2px;
    border-radius: 3px;
    transition: all 300ms;
}

select:hover {
    border-color: blue;
}

@media (max-width: 1224px) {
    .place-container {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: 15px !important;
    }
    .s-place {
        margin-left: 10px !important;
        width: 90% !important;
    }
    .country-select {
        width: 100% !important;
    }
    .main-block {
        flex-direction: column !important;
    }
    .hr-down {
        display: none !important;
    }
}

@media (max-width: 540px) {
    .country-select {
        max-width: 90% !important;
    }
    .contact-input {
        margin-left: 12px !important;
    }
}

@media (max-width: 360px) {
    .country-select {
        max-width: 90% !important;
    }
}
</style>