<script>
import axios from 'axios';

export default {
    data() {
        return {
            email: '',
            password: '',
            exPassword: '',
            
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
            if (this.email === '') {
                this.error = '*Вы не ввели Email*'
            } else if (this.password === '') {
                this.error = '*Вы не ввели пароль*'
            } else if (this.exPassword === '') {
                this.error = '*Вы не повторили пароль*'
            } else if (this.password !== this.exPassword) {
                this.error = '*Пароли не совпадают'
            }
            else {
                this.error = '';
                this.login();
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
        
        async login() {
            await axios.post('/login', {
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
            <p>Войти</p>
            <div class="regist">
                <form @submit.prevent="check">
                    <input v-model="email" class="inp inp-email" type="email" placeholder="Почта">
                    <input v-model="password" class="inp inp-password" type="password" placeholder="Пароль">
                    <input v-model="exPassword" class="inp inp-rep-password" type="password" placeholder="Повторите пароль">
                    <p class="error">{{ error }}</p>
                    <button type="submit">Войти</button>
                </form>
                <div class="haveacc">
                    <p>Забыли</p><a href="#/RecoveryPassPage">пароль</a><p>?</p>
                </div>
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
        height: 91vh;
        background: url(../../assets/backgroundUp.png) center;
        background-repeat: no-repeat; 
    }

    .content p {
        font-size: 56px;
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
        margin-bottom: 40px;
    }


    .inp {
        font-size: 18px;
        width: 750px;
        height: 35px;
        padding-left: 10px;
        border-radius: 12px !important;

        border: 1px solid #121212 !important;
    }

    .regist button {
        margin-top: 40px;
        margin-bottom: 15px;

        width: 320px;
        height: 50px;
        font-size: 24px;
        background: none;

        border: 1px solid #2D72D9;
        border-radius: 8px;
        color: #2D72D9;

        transition: all 100ms;
    }

    .regist button:hover {
        background-color: #2D72D9;
        color: #fff;
    }

    .regist button:active {
        background-color: #1b54a9;
    }

    .regist p {
        font-size: 26px;
        margin: 0;
    }

    .regist a {
        font-size: 26px;
        color: #2D72D9;
        font-weight: 500;
    }

    .regist a:hover {
        color: #1b54a9;
    }

    .regist a:active {
        color: #114189;
    }

    .haveacc {
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .error {
        color: #ff1f1f;
        margin-bottom: -30px !important;
        margin-top: -30px !important;
    }

    .haveacc p:last-child {
        margin-left: -7px;
    }
    
</style>