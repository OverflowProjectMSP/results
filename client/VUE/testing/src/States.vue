<script>
import VidComp from './components/MainComponents/VidComp.vue'
import ModelWind from './components/СomponetsForPages/ModelWind.vue';
export default {
    components: {
    VidComp,
    ModelWind,  
    },
    data() {
        return {
            items: [
                {
                    title: `Как создать переменную?`,
                    subscribers: 50,
                    hours: 43,
                    views: 43,
                    answers: 423,
                    language: 'Python',
                    complexity: 'Средне',

                },
                {
                    title: `Как создать переменную?`,
                    subscribers: 50,
                    hours: 43,
                    views: 43,
                    answers: 423,
                    language: 'C++',
                    complexity: 'Средне',
                },
                {
                    title: `Как создать переменную?`,
                    subscribers: 45,
                    hours: 0,
                    views: 43,
                    answers: 423,
                    language: 'Асембелер',
                    complexity: 'Средне',
                },
            ],
            Show: false,
        }
    },
    methods: {
        OpenModal() {
            this.Show = !this.Show
        },
        CloseModal(Show) {
            this.Show = false
        }
    }
}
</script>

<template>
<!-- Компонент поиска -->
<h4 class="text">Поиск статьи</h4>

<div class="content d-flex align-items-center">
    <input type="text" class="form-control" placeholder="Название проблемы" aria-label="First name">
    <input type="text" class="form-control" placeholder="Автор" aria-label="Last name">
   <!-- селект -->
  <div class="down-menu d-flex align-items-center">
      <div class="dropdown-center">
      <button class="btn btn-light dropdown-toggle d-flex align-items-center" type="button" data-bs-toggle="dropdown" aria-expanded="false">
        <img src="./assets/js.jpg" alt="" class="image"><span>JavaScript</span>
      </button>
      <ul class="dropdown-menu">
        <li><a class="dropdown-item d-flex align-items-center" href="#/States"><img src="./assets/js.jpg" alt="" class="image"><span>JavaScript</span></a></li>
        <li><a class="dropdown-item d-flex align-items-center" href="#/States"><img src="./assets/js.jpg" alt="" class="image"><span>JavaScript</span></a></li>
        <li><a class="dropdown-item d-flex align-items-center" href="#/States"><img src="./assets/js.jpg" alt="" class="image"><span>JavaScript</span></a></li>
      </ul>
      </div>
      <!-- плюсик -->
      <div class="contain" @click="OpenModal" >
        <img src="./assets/add.png" class="add" alt="">
      </div>
      </div>
  </div>




<!-- Див с виджетами -->
<div class="con mt-3">
<a href="#/CommentsPost">
    <vid-comp :item="item"  v-for="item in items" role="button" />
</a>
</div>


<model-wind v-if="Show" @CloseModal="CloseModal"/>


</template>

<style scoped>
a {
    text-decoration: none;
    color: #000;
}
h4{
    margin-left: 20.5%;
    margin-top: 20px;
    font-size: 40px;
    
}
.image{
    margin-right: 10px;
    width: 25px;
}
.add{
    width: 25px;
    height: 25px;
    cursor: pointer
}
.btn{
    font-size: 16px;
    font-weight: bold;
    color:blueviolet ;
}
.content {
    margin: 10px;
    flex-wrap: wrap;
    margin-left: 20%;
}
.form-control{
    margin: 5px;
}
.dropdown-center{
    margin-left: 15px;
}
.content input{
    width: 300px;
    border-radius: 10px;
}
.con{
    justify-content: start;
}
.contain{
    width: 5%;
    height: 5%;
    
}
.plus {
    width: 30px; 
    height: 30px;
    background-color: #e8e7ea;
    border-radius: 50%; 
    border: 0.0001px solid ; 
    
    
   
}
.p{
    margin-left: 0.2px;
    margin-right: 1px;
}
.dropdown-center{
    margin-right:10px;
}

@media (max-width: 900px){

.content input{
    width: 200px;
}
.content, h4 {
    margin-left: 100px;
    margin-right: 100px;
}
.dropdown-center{
    margin: 2px !important;
}
}
@media (max-width: 800px) {
    .content, h4 {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    h4 {
        font-size: 30px;
    }
}
</style>