<script>
import axios from 'axios';
import VidComp from './components/MainComponents/VidComp.vue'
import ModelWind from './components/СomponetsForPages/ModelWind.vue';
export default {
    components: {
    VidComp,
    ModelWind,  
    },
    data() {
        return {
            states: [
                {
                    title: `Как создать переменную?`,
                    subscribers: 50,
                    hours: 43,
                    views: 43,
                    answers: 423,
                    language: 'Python',
                    complexity: 'Средне',
                    id: 0,
                    question: false,            
                },
                {
                    title: `Как создать переменную?`,
                    subscribers: 50,
                    hours: 43,
                    views: 43,
                    answers: 423,
                    language: 'C++',
                    complexity: 'Средне',
                    id: 1,
                    question: false,            
                },
                {
                    title: `Как создать переменную?`,
                    subscribers: 45,
                    hours: 0,
                    views: 43,
                    answers: 423,
                    language: 'Асембелер',
                    complexity: 'Средне',
                    id: 2,
                    question: false,                
                },
            ],
            Show: false,
            filters: {
                type: "false",
            },
        }
    },
    mounted() {
        this.loadStates()
        setInterval(() => {
            this.loadStates()
        }, 30000);
    },
    methods: {
        OpenModal() {
            this.Show = !this.Show
        },
        CloseModal(Show) {
            this.Show = false
        },

        async loadStates() {
            let res = await axios.get('/show-states');
            this.states = res.data.all;
        },
        async filtre() {
            if (this.filters.type == 'false') {
                this.filtrs = {
                    filtr: false
                }
            } else {
                this.filtrs = {
                    filtr: true,
                    tag: this.filtr.tag,
                };
            }
            let res = await axios.post('/filtre-states', {
                filters: this.filtrs
            });
            this.quetions = res.data.all;
        }
    }
}
</script>

<template>
<!-- Компонент поиска -->
<h4 class="text">Поиск статьи</h4>

<div class="content d-flex align-items-center">
    <input type="text" class="form-control" placeholder="Название статьи" aria-label="First name">
    <input type="text" class="form-control" placeholder="Автор" aria-label="Last name">
   <!-- селект -->
  <div class="down-menu d-flex align-items-center">
      <div class="dropdown-center">
      <select class="form-select me-2" v-model="filters.type">
        <option value="JavaScript"><img src="./assets/js.jpg" class="image">JavaScript</option>
        <option value="TS"><img :src="'src/assets/js.jpg'" class="image">TS</option>
        <option value="Python"><img src="./assets/js.jpg" class="image">Python</option>
        <option value="PHP"><img src="./assets/js.jpg" class="image">PHP</option>
        <option value="C++"><img src="./assets/js.jpg" class="image">C++</option>
        <option value="Java"><img src="./assets/js.jpg" class="image">Java</option>
        <option value="C#"><img src="./assets/js.jpg" class="image">C#</option>
        <option value="false"><img src="./assets/js.jpg" class="image">Без фильтров</option>
      </select>
      </div>
      <!-- плюсик -->
      <div class="contain" @click="OpenModal" >
        <img src="./assets/add.png" class="add" alt="">
      </div>
      <button class="btn find-btn btn-outline-primary text-dark ms-4" @click="filtre">Отфильровать</button>

      </div>
  </div>




<!-- Див с виджетами -->
<div class="con mt-3" v-for="item in states">
<a :href="`#/StatesItem?id=${item.id}&question=${false}`">
    <vid-comp :item="item" role="button" />
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