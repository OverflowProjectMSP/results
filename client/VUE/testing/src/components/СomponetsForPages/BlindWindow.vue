<script>
export default {
    props: {
        title: String,
        Show: Boolean,
    },
    methods: {
        Close() {
            this.$emit('Close', this.Show);
        }
    }
}
</script>

<template>
    <transition name="modal-fade">

        <div class="modal-backdrop">
            <div class="window">
                <p>{{ title }}</p>
                <button @click="Close">
                    <a target="_blank" href="https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley">
                        Ладно...
                    </a>
                </button>
            </div>
        </div>
    </transition>
</template>

<style scoped>
a {
    text-decoration: none;
    color: #fff;
}

.window {
    width: 500px;
    height: 300px;
    border-radius: 30px;
    background-color: #ffffff;
    border: 4px solid #2a2a2a;

    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    gap: 15px;


    font-family: "Rubik", sans-serif;
    user-select: none;

}

p {
    font-weight: 600;
    font-size: 22px;
    text-align: center;
}

button {
    width: 190px;
    height: 50px;
    border-radius: 12px;
    border: none;
    background-color: #4200FF;
    color: #fff;
    cursor: pointer;

    font-weight: 600;
    font-size: 20px;

    transition: all 100ms;

}

button:hover {
    background-color: #2d00aa;
    border-radius: 25px 5px;
    /* box-shadow: inset 3px 3px 0 #2d2d2d,
                inset -3px -3px 0 #2d2d2d; */
}

button:active {
    background-color: #240088;
}

.modal-backdrop {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>