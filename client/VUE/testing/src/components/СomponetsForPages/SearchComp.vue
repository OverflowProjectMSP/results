<script>
import VidComp from '../MainComponents/VidComp.vue'

export default {
    componets: {
        VidComp,
    },
    data() {
        return {

        }
    }
}

</script>
<template>
    <div class="content d-flex align-items-center">
        <h4 class="text">Поиск</h4>
        <input type="text" class="form-control" placeholder="Название проблемы" aria-label="First name">
        <input type="text" class="form-control" placeholder="Автор" aria-label="Last name">
        <button class="input-group-text" id="inputGroupPrepend">Найти</button>
        <div class="dropdown-center">
            <button class="btn btn-light dropdown-toggle d-flex align-items-center" type="button"
                data-bs-toggle="dropdown" aria-expanded="false">
                <img src="../../assets/js.jpg" alt="" class="image"><span>JavaScript</span>
            </button>
            <ul class="dropdown-menu">
                <li><a class="dropdown-item d-flex align-items-center" href="#"><img src="../../assets/js.jpg" alt=""
                            class="image"><span>JavaScript</span></a></li>
                <li><a class="dropdown-item d-flex align-items-center" href="#"><img src="../../assets/js.jpg" alt=""
                            class="image"><span>JavaScript</span></a></li>
                <li><a class="dropdown-item d-flex align-items-center" href="#"><img src="../../assets/js.jpg" alt=""
                            class="image"><span>JavaScript</span></a></li>
            </ul>
        </div>
    </div>
</template>
<style scoped>
.image {
    margin-right: 10px;
    width: 25px;
}

.btn {
    font-size: 16px;
    font-weight: bold;
    color: blueviolet;
}

.content {
    margin: 10px;
}

.form-control {
    margin: 5px;
}

.dropdown-center {
    margin-left: 15px;
}

.content input {
    width: 500px;
}

@media (max-width: 1000px) {
    .content {
        flex-wrap: wrap;
    }

    .content .text {
        margin-right: 100px;

    }
}
</style>