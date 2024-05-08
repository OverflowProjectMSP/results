<script>
import axios from 'axios';

export default {
    data() {
        return {
            email: '',
            password: '',
            exPassword: '',
            nickname: ``,
            
            error: '',
            eyeOpen1: true,
            eyeOpen2: true,
            eyeImg1: '/src/assets/eye.svg',
            eyeImg2: '/src/assets/eye.svg',
            isShowPassword: false,
            showPassword: 'password',
            isShowExPassword: false,
            showExPassword: 'password',
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
        
        async register() {
            this.check();
            await axios.post('/registration', {
                name: this.nickname,
                email: this.email,
                password: this.password
            });
        },
    }
}

</script>

<template>
    <div class="tototocontainer">
        <div class="background"></div>
        <div class="content">
            <p>Регистрация</p>
            <div class="regist">
                <form>
                    <input class="inp inp-username" type="text" name="" id="" placeholder="Никнейм">
                    <input class="inp inp-email" type="email" placeholder="Почта">
                    <input class="inp inp-password" type="password" placeholder="Пароль">
                    <input class="inp inp-rep-password" type="password" placeholder="Повторите пароль">
                </form>
            </div>
        </div>
    </div>
</template>
    
<style>
    .tototocontainer {
        width: 100%;
        display: flex;
    }

    .background {
        width: 40%;
        height: 92vh;
        background: url(../../assets/backgroundUp.png) center;
        background-repeat: no-repeat; 
    }

    .content p {
        font-size: 38px;
        margin-bottom: 12px;
    }

    .content {
        margin-top: 219px;
        margin-left: 128px;
    }

    .regist form {
        display: flex;
        flex-direction: column;
        gap: 30px;
        border: none;
    }

    .inp {
        width: 750px;
        height: 30px;
        padding-left: 10px;
        border-radius: 15px;
        border: none;
    }


    
</style>