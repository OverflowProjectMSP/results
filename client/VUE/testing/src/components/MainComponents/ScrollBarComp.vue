<script>
export default {
    data() {
        return {
            devolepers: [
                {
                    name: `kosty_py`,
                    role: `Тимлид/Старший бекенд разработчик`,
                    imageProfileDS: `kosty-py.png`
                },
                {
                    name: `kinestrik`,
                    role: `Заместитель тимлида/Старший фронтенд разработчик`,
                    imageProfileDS: `Kinestrick.png`
                },
                {
                    name: `therisingdream`,
                    role: `Заместитетель ведущего Фронтенд разработчика`,
                    imageProfileDS: `therisingdream.png`
                },
                {
                    name: `febolo`,
                    role: `Заместитель ведущего Бекенд разработчика`,
                    imageProfileDS: `febolo.png`
                },
                {
                    name: `habbock`,
                    role: `Фронтенд разработчик`,
                    imageProfileDS: `hebber.png`
                },
                {
                    name: `kenmaxd`,
                    role: `Дизайнер/Фронтенд разработчик`,
                    imageProfileDS: `kenma.gif`
                },
                {
                    name: `garleenn`,
                    role: `Лучший фронтенд разработчик`,
                    imageProfileDS: `garleen.png`
                },
                {
                    name: `nikit0_17`,
                    role: `Главный дизайнер`,
                    imageProfileDS: `disainerImg.png`
                },
            ],
            index: 0,
            index1: 1,
            index2: 2,
            index3: 3,
            names: [],
            roles: [],
            images: [],
        }
    },
    mounted() {
        this.resImage();
    },
    methods: {
        resImage() {
            for (let i = 0; i < this.devolepers.length; i++) {
                this.names.push(this.devolepers[i].name);
                this.roles.push(this.devolepers[i].role);
                this.images.push(this.devolepers[i].imageProfileDS);
            }
        },
        nextDev() {
            this.index++;
            this.index1++;
            this.index2++;
            this.index3++;
            if (this.index == this.roles.length) {
                this.index = 0;
            } else if (this.index1 == this.roles.length) {
                this.index1 = 0;
            } else if (this.index2 == this.roles.length) {
                this.index2 = 0;
            } else if (this.index3 == this.roles.length) {
                this.index3 = 0;
            }

        },
        prevDev() {
            this.index--;
            this.index1--;
            this.index2--;
            this.index3--;
            if (this.index < 0) {
                this.index = this.roles.length - 1;
            }
            if (this.index1 < 0) {
                this.index1 = this.roles.length - 1;
            }
            if (this.index2 < 0) {
                this.index2 = this.roles.length - 1;
            }
            if (this.index3 < 0) {
                this.index3 = this.roles.length - 1;
            }
        }
    }
}
</script>

<template>
    <hr>
    <div class="develop d-flex gap-3 justify-content-center align-items-center gap-2 mx-5 flex-column my-4">
        <h1>Команда разработчиков</h1>
        <div class="dev-container d-flex flex-row">
            <div @click="prevDev" role="button"
                class="arrow arrow-left mx-5 d-flex justify-content-center align-items-center gap-2 fs-1 fw-bold user-select-none">
                < </div>
                    <div class="collaps-container d-flex justify-content-center flex-wrap gap-4">
                        <div class="dev-card d-flex flex-column gap-0 align-items-center">
                            <img class="rounded-2 user-select-none" :src="`src/assets/` + images[index]"
                                :alt="names[index]">
                            <h4 class="mt-2">{{ names[index] }}</h4>
                            <span class="text-center">{{ roles[index] }}</span>
                        </div>
                        <div class="dev-card dev-card-2 d-flex flex-column gap-0 align-items-center">
                            <img class="rounded-2 user-select-none" :src="`src/assets/` + images[index1]"
                                :alt="names[index1]">
                            <h4 class="mt-2">{{ names[index1] }}</h4>
                            <span class="text-center">{{ roles[index1] }}</span>
                        </div>
                        <div class="dev-card dev-card-3 d-flex flex-column gap-0 align-items-center">
                            <img class="rounded-2 user-select-none" :src="`src/assets/` + images[index2]"
                                :alt="names[index2]">
                            <h4 class="mt-2">{{ names[index2] }}</h4>
                            <span class="text-center">{{ roles[index2] }}</span>
                        </div>
                        <div class="dev-card dev-card-4 d-flex flex-column gap-0 align-items-center">
                            <img class="rounded-2 user-select-none" :src="`src/assets/` + images[index3]"
                                :alt="names[index3]">
                            <h4 class="mt-2">{{ names[index3] }}</h4>
                            <span class="text-center">{{ roles[index3] }}</span>
                        </div>
                    </div>
                    <div @click="nextDev" role="button"
                        class="arrow arrow-right mx-5 d-flex justify-content-center align-items-center gap-2 fs-1 fw-bold user-select-none">
                        > </div>
            </div>
        </div>
        <div class="footer-container pt-5 p-4 bg-primary w-100 h-100 d-flex flex-column align-items-center text-white">
            <h4>UpFollow</h4>
            <span><a class="text-white text-muted" href="#/FAQ">FAQ</a></span>
        </div>

</template>

<style scoped>
.dev-card {
    max-width: 250px;
    height: 342.8px;
    transition: all 300ms;
    cursor: pointer;
}

.dev-card:hover {
    transform: translateY(-10px)
}

.dev-card img {
    max-width: 250px;
}

@media (max-width: 1624px) {
    .dev-card-4 {
        display: none !important;
    }
}

@media (max-width: 1224px) {

    .dev-card-3,
    .dev-card-4 {
        display: none !important;
    }
}

@media (max-width: 880px) {

    .dev-card-2,
    .dev-card-3,
    .dev-card-4 {
        display: none !important;
    }

    hr {
        margin-top: 200px !important;
    }

    .develop {
        margin: 30px 10px !important;
    }

    .arrow {
        margin: 0 20px !important;
    }
}
</style>