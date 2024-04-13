<script>

</script>

<template>

    <body>
        <main>
            <div class="container">
                <div class="row pt-5">
                    <div class="col-3 ">
                        <h3>Настройки профиля</h3>
                    </div>
                </div>
                <hr>
                <div class="row" style="display: flex; gap: 40px;">
                    <div class="col-1">
                        <h5>Анкета</h5>
                    </div>
                    <div class="col-1">
                        <h5 style="color: gray; font-weight: 400;">Аккаунт</h5>
                    </div>
                </div>
                <hr>
                <div class="row">
                    <div class="col-12" style="text-align: center;">
                        <img src="../../assets/4213460-account-avatar-head-person-profile-user_115386.png"
                            style="height: 100px;">
                        <p style="color: gray;">Ваша фотография.</p>
                        <p style="color: gray;">Размер загружаемой фотографии <br> не должен быть более 2 МБ.</p>
                        <button id="download">Загрузить</button>
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
                            <input type="text" class="form-control" placeholder="" aria-label="About"
                                aria-describedby="basic-addon1" style="height: 150px;">
                        </div>
                    </div>
                </div>
                <div class="row">
                    <h5>Контакты</h5>
                    <div class="col-12" style="display: flex;">
                        <select>
                            <option value="email">E-mail</option>
                            <option value="Telegram">Telegram</option>
                            <option value="Skype">Skype</option>
                            <option value="Discord">Discord</option>
                            <option value="Facebook">Facebook</option>
                            <option value="Telephone">Telephone</option>
                        </select>
                        <input type="text" class="form-control" placeholder="" aria-label="About"
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
                    <div class="col-12" style="display: flex;">
                        <select style="width: 350px;">
                            <option value="email">Страна</option>
                            <option value="Telegram">Россия</option>
                            <option value="Skype">Белоруссия</option>
                            <option value="Discord">Германия</option>
                            <option value="Facebook">Китай</option>
                            <option value="Telephone">Япония</option>
                        </select>
                        <input type="text" class="form-control" placeholder="Регион" aria-label="About"
                            aria-describedby="basic-addon1" style="margin-left: 30px;">
                        <input type="text" class="form-control" placeholder="Город" aria-label="About"
                            aria-describedby="basic-addon1" style="margin-left: 30px;">
                    </div>
                </div>
                <div class="row pt-5">
                    <div class="col-4">
                        <button id="save"><b>Сохранить изменения</b></button>
                    </div>
                </div>
            </div>
        </main>
    </body>

</template>

<style>
#download,
#save {
    background-color: white;
    color: #7ac97a;
    border-color: #90EE90;
    border-radius: 5px;
    padding-right: 15px;
    padding-left: 15px;
    text-align: center;
}

#delete,
#add {
    background-color: white;
    border: none;
    color: gray;

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
</style>