<script>
export default {

}
</script>
<template>
    <div class="container mb-3">
        <div class="row pt-5">
            <div class="col-3 ">
                <h3>Настройки профиля</h3>
            </div>
        </div>
        <hr>
        <div class="ancet row d-flex align-items-center" style="display: flex; gap: 40px;">
            <div class="col-1 acent">
                <h5>Анкета</h5>
            </div>
            <div class="col-1">
                <h5 style="color: gray; font-weight: 400;">Аккаунт</h5>
            </div>
        </div>
        <hr>
        <div class="row">
            <div class="col-12" style="text-align: center;">
                <img src="" style="height: 100px;">
                <p style="color: gray;">Ваша фотография.</p>
                <p style="color: gray;">Размер загружаемой фотографии <br> не должен быть более 2 МБ.</p>
                <button id="download" style="margin-right: 10px;" type="file">Загрузить</button>
                <button id="delete">Удалить</button>
            </div>
        </div>
        <hr>
        <div class="row">
            <div class="col-12">
                <h5>Имя</h5>
                <div class="input-group mb-3">
                    <input type="text" class="form-control" placeholder="" aria-label="Name"
                        aria-describedby="basic-addon1">
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-12">
                <h5>Фамилия</h5>
                <div class="input-group mb-3">
                    <input type="text" class="form-control" placeholder="" aria-label="Secondname"
                        aria-describedby="basic-addon1">
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-12">
                <h5>Интересы</h5>
                <div class="input-group mb-3">
                    <input type="text" class="form-control" placeholder="" aria-label="Interests"
                        aria-describedby="basic-addon1">
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-12">
                <h5>О себе</h5>
                <div class="input-group mb-3">
                    <textarea type="text" class="form-control" placeholder="" aria-label="About"
                        aria-describedby="basic-addon1" style="height: 150px;"></textarea>
                </div>
            </div>
        </div>
        <div class="row contact-container">
            <h5>Контакты</h5>
            <div class="col-12" style="display: flex;">
                <select role="button" class="contact-select mb-3">
                    <option value="email">E-mail</option>
                    <option value="Telegram">Telegram</option>
                    <option value="Skype">Skype</option>
                    <option value="Discord">Discord</option>
                    <option value="Facebook">Facebook</option>
                    <option value="Telephone">Telephone</option>
                </select>
                <input type="text" class="form-control contact-input mb-3" placeholder="" aria-label="About"
                    aria-describedby="basic-addon1" style="margin-left: 30px;">
            </div>
        </div>
        <div class="row pt-2">
            <div class="col-2">
                <button id="add">Добавить</button>
            </div>
        </div>
        <div class="row pt-4">
            <h5>Местоположение</h5>
            <div class="col-12 place-container gap-3" style="display: flex;">
                <select style="width: 350px;" role="button" class="country-select col-4">
                    <option value="Russia" selected>Россия</option>
                    <option value="Belarus">Белоруссия</option>
                    <option value="Germany">Германия</option>
                    <option value="China">Китай</option>
                    <option value="Japan">Япония</option>
                    <option value="USA">США</option>
                    <option value="UK">Великобритания</option>
                </select>
                <input type="text" class="form-control s-place" placeholder="Регион" aria-label="About"
                    aria-describedby="basic-addon1" style="margin-left: 30px;">
                <input type="text" class="form-control s-place" placeholder="Город" aria-label="About"
                    aria-describedby="basic-addon1" style="margin-left: 30px;">
            </div>
        </div>
        <div class="row pt-4">
            <div class="col-4 save-btn-block">
                <button id="save"><b>Сохранить изменения</b></button>
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