<script>

</script>

<template>

<div class="footer">
    <div class="d-flex flex-column align-items-center"> 
            <div class="d-flex flex-row">
                <a href="#" style="--i:7"><img class="link user-select-none" :src="'src/assets/Telegram.png'" alt="telegram"></a>
                <a href="#" style="--i:8"><img class="link user-select-none" :src="'src/assets/Vk.png'" alt="vk"></a>
            </div>
            <p class="text">Upfollow</p>
            <hr class="hr">
            <p class="text_FAQ"><a href="#/FAQ">FAQ</a></p>
            <a href="#/"><img class="arrow user-select-none" src="@/assets/arrows.png" alt="arrows"></a>
    </div>
</div>  
</template>

<style scoped>
* {
    margin: 0;
    padding: 0;
    text-decoration: none;
}
a {
    text-decoration: none;
    color: #fff;
}
.footer{    
    background: url('@/assets/back.png'); 
    background-repeat: no-repeat;
    background-size: cover;
    height: 370px;
    width: 100%;
    display: flex;
    justify-content: center;      
    align-content: center;  
    flex-wrap: wrap;
    padding-top: 60px;
}
.link {
    width: 42px;
    height: 42px;
    margin-right: 5px;
    padding: 8px;
    animation: slideLeft 1s ease forwards;
    animation-delay: calc(.1s * var(--i));
}
.text{
    margin: 8px 0;
    font-size: 24px;
    color: white;
}
.hr {
    /* background: #000; */
    height: 2px;
    width: 100%;
}
.logo{
    text-align: center;
    margin: 10px 0px;
    color: white;
    font-size: 24px;
}
.text_FAQ{
    margin: 8px 0;
    font-size: 24px;
    color: white;
    text-align: center;
}

@media (max-width: 400px) {
    .footer{
        padding-top: 30px;
    }
    
}
/* KEYFRAMES ANIMATION */
@keyframes slideLeft {
    0% {
        transform: translateX(100px);
        opacity: 0;
    }

    100% {
        transform: translateX(0);
        opacity: 1;
    }
}
</style>