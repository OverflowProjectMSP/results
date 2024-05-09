<script>
import axios from 'axios';

export default {
    data() {
        return {
            email: 'example@gmail.com',
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

            inputNumber: '',
        }
    },
    methods: {
        check() {
        
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
            <p>Введите код доступа</p>
            <p class="toemail">На почту <br> {{ email }} вам был <br> отправлен ключ доступа </p>
            <div class="regist">
                <form>
                    <input class="numinp" type="number">
                    <input class="numinp" type="number">
                    <input class="numinp" type="number">
                    <input class="numinp" type="number">
                </form>
                <p class="error">{{ error }}</p>
                <button @click="check">Подтвердить через ...</button>
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
        font-size: 42px;
        margin-bottom: 12px;
    }

    .content {
        margin-top: 219px;
        margin-left: 128px;
    }

    .regist form {
        display: flex;
        flex-direction: row;
        gap: 20px;
        margin-bottom: 40px;
    }

    .toemail {
        font-size: 30px !important;
        color: #A4A4A4;
    }

    input[type=number]::-webkit-inner-spin-button,
    input[type=number]::-webkit-outer-spin-button {
        -webkit-appearance: none;
        margin: 0; /* Удалить отступы */
    }

    .numinp {
        padding-left: 25px;

        width: 100px;
        height: 100px;
        font-size: 80px;

        border-radius: 15px !important;
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

    .error {
        font-size: 18px !important;
        color: #ff1f1f;
        margin-bottom: -30px !important;
        margin-top: -30px !important;
    }
    
</style>