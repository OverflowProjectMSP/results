<script>
import axios from 'axios';

export default {
    data() {
        return {
            email: '',
            
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
                this.error = '*Вы не ввели Email*';
            }  else {
                this.error = '';
                this.checkPassword();
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
        
        async checkPassword() {
            let res = await axios.post('/new-password-email', {
                email: this.email
            });
            if(res.data.res == 'Error') {
                this.error = '*Ошибка отправки*';
            } else {
                this.error = ''; 
                this.$router.push('/EnterCodePage');
            }
        },
    }
}

</script>

<template>
    <div class="tototocontainer">
        <div class="background"></div>
        <div class="content">
            <p>Востановить пароль</p>
            <div class="regist">
                <form @submit.prevent="check">
                    <input v-model="email" class="inp inp-email" type="email" placeholder="Почта">
                    <p class="error">{{ error }}</p>
                    <button type="submit">Сбросить</button>
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

    .error {
        font-size: 18px !important;
        color: #ff1f1f;
        margin-bottom: -30px !important;
        margin-top: -30px !important;
    }
    
</style>