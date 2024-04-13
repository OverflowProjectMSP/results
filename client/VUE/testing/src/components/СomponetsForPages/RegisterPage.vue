<script>

export default {
    data() {
        return {
            email: '',
            password: '',
            isShowPassword: false,
            showPassword: 'password',
            exPassword: '',
            isShowExPassword: false,
            showExPassword: 'password',
            error: '',
            eyeOpen1: true,
            eyeOpen2: true,
            eyeImg1: '/src/assets/eye.svg',
            eyeImg2: '/src/assets/eye.svg',
            nickname: ``,
        }
    },
    methods: {
        check() {
            if (this.nickname === ``) {
                this.error = '*Вы не ввели никнейм*'
            }
            else if (this.email === '') {
                this.error = '*Вы не ввели Email*'
            } else if (this.password === '') {
                this.error = '*Вы не ввели пароль*'
            } else if (this.exPassword === '') {
                this.error = '*Вы не повторили пароль*'
            } else if (this.password.length <= 9) {
                this.error = '*Пароль должен включать 8 символов*'
            } else if (!this.password.includes('*')) {
                this.error = '*Пароль должен включать спец символ*'
            } else if (this.password !== this.exPassword) {
                this.error = '*Пароли не совпадают'
            }
            else {
                this.error = ''
            }


            if (this.password !== this.exPassword) {
                this.error = '*Пароли не совпадают'
            }
        },
        toggleVisibility1() {
            this.isShowPassword = !this.isShowPassword;
            this.eyeOpen1 = !this.eyeOpen1

            if (this.isShowPassword) {
                this.showPassword = 'text'
                this.eyeImg1 = '/src/assets/svg-editor-image2.svg'
            } else {
                this.showPassword = 'password'
                this.eyeImg1 = '/src/assets/eye.svg'
            }
        },
        toggleVisibility2() {
            this.isShowExPassword = !this.isShowExPassword;
            this.eyeOpen2 = !this.eyeOpen2

            if (this.isShowExPassword) {
                this.showExPassword = 'text'
                this.eyeImg2 = '/src/assets/svg-editor-image2.svg'
            } else {
                this.showExPassword = 'password'
                this.eyeImg2 = '/src/assets/eye.svg'
            }
        },

    }
}

</script>

<template>
    <div class="container">
        <h1>Регистрация</h1>
        <form action="#!">
            <input class="form-item form-item-1" v-model="nickname" placeholder="Введите никнейм" type="email" name=""
                id="">
            <input class="form-item form-item-1" v-model="email" placeholder="Email" type="email" name="" id="">
            <div class="password">
                <input class="form-item form-item-2" :type="showPassword" v-model="password" placeholder="Пароль"
                    type="password" name="password" id="password-input">
                <img @click="toggleVisibility1" class="password-show" :src="eyeImg1" alt="">
            </div>
            <div class="exPassword">
                <input class="form-item form-item-3" :type="showExPassword" v-model="exPassword"
                    placeholder="Повторите пароль" type="password" name="exPassword" id="exPassword-input">
                <img @click="toggleVisibility2" class="exPassword-show" :src="eyeImg2" alt="">
            </div>
        </form>
        <div class="error-end-btn">
            <p class="have_account">Уже есть аккаунт? <a href="#/Login">Войти</a></p>
            <p class="error">{{ error }}</p>
            <button class="btn-reg" @click="check">Зарегистрироваться</button>
        </div>
    </div>
</template>

<style scoped>
.container {
    background: #ffffff;
    width: 400px;
    height: 580px;
    margin-left: auto;
    margin-right: auto;
    margin-top: 100px;
    border-radius: 30px;
    border: solid 3px #2a2a2a;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
}

h1 {
    font-size: 45px;
    margin-bottom: 50px;
    user-select: none;
}

form {
    display: flex;
    flex-direction: column;
}

.form-item {
    border: 2px solid #2a2a2a;
    border-radius: 10px;
    width: 300px;
    height: 40px;

    margin-bottom: 25px;
    padding-left: 10px;
    padding-right: 10px;
}

.form-item:focus {
    outline: 2px solid #4200FF;
    border: none;
}

.btn-reg {
    margin-top: 10px;

    width: 280px;
    height: 60px;
    border-radius: 12px;
    border: none;
    background-color: #4200FF;
    color: #fff;
    cursor: pointer;
    font-weight: 600;
    font-size: 16px;

    transition: all 100ms;
}

.btn-reg:hover {
    background-color: #2d00aa;
    border-radius: 25px 5px;
}

.btn-reg:active {
    background-color: #240088;
}

.error {
    color: #ff2600;
    height: 20px;
    user-select: none;
}

.have_account {
    font-size: 20px;
    user-select: none;
}

div a {
    text-decoration: none;
    color: #4200FF;
}


.password {
    position: relative;
}

.password-show {
    position: absolute;
    cursor: pointer;
    top: 5px;
    right: 12px;
    width: 30px;

}

.exPassword {
    position: relative;
}

.exPassword-show {
    position: absolute;
    cursor: pointer;
    top: 5px;
    right: 12px;
    width: 30px;

}


/* .password-control.view {
	background: url(../assets/eyeclose.svg) 0 0 no-repeat;
} */
</style>