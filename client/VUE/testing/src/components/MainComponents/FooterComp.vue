<script>

</script>

<template>
    <footer class="help_end">

        <div class="support">
            <h2 class="contact_us">Свяжитесь с нами:</h2>

            <div class="social_media">
                <a target="_blank" href="https://vk.com/javascript_forum" style="--i:5;"><i class='bx bxl-vk'></i></a>
                <a target="_blank" href="https://discord.com/channels/1070066941177368677/1070092178690416830"
                    style="--i:7;"><i class='bx bxl-discord-alt'></i></a>
                <a target="_blank" class="telegram" href="https://t.me/js_universe" style="--i:8;"><i
                        class='bx bxl-telegram'></i></a>
            </div>

        </div>


        <div class="image_above">
            <img class="image_above_number_two" src="../../assets/Vector_9.png" alt="Error image">
        </div>

        <div class="team">
            <div class="self_deference_content">
                <p class="self_deference">©️ Разработано составом OWERFLOW</p>
            </div>
        </div>

    </footer>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,300;0,400;0,500;1,500&display=swap');


* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    list-style: none;
    text-decoration: none;
}

html {
    scroll-behavior: smooth
}

.help_end {
    max-width: 100%;
    padding-bottom: 10px;
    background-color: #75A3ED;
    height: 270px;
    padding: 0 10px;
    margin: 0 auto;
    border-radius: 10px 10px 0px 0px;

}

.support {
    text-align: center;
}

.contact_us {
    font-size: 24px;
    font-weight: 400;
    color: #fff;
    padding-top: 10px;
    margin-bottom: 10px;
}

.self_deference {
    font-size: 20px;
    font-weight: 300;
    color: #fff;
    margin: 0px;
}

.social_media a {
    display: inline-flex;
    justify-content: center;
    align-items: center;
    width: 40px;
    height: 40px;
    background: transparent;
    border: 3px solid #fff;
    border-radius: 50%;
    font-size: 20px;
    color: #fff;
    text-decoration: none;
    margin-left: 10px;
    opacity: 0;
    animation: slideLeft 1s ease forwards;
    animation-delay: calc(.2s * var(--i));

}

.social_media a:hover {
    background: #0ef;
    color: #1f242d;
    box-shadow: 0 0 20px #0ef;
}

.image_above_number_two {
    max-width: 98vw;
    max-height: 80%;
    padding: 0;
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