<script>

</script>

<template>
  <div class="btn-group">
    <button class="btn btn-secondary btn-lg" type="button">
      <img src="../../assets/AI.png" alt="">
    </button>
    <button type="button" class="btn btn-lg btn-secondary dropdown-toggle dropdown-toggle-split"
      data-bs-toggle="dropdown" aria-expanded="false">
      <span class="visually-hidden" style="margin-right: 5px;">Сложность</span>
    </button>
    <ul class="dropdown-menu" style>
      <li><a class="dropdown-item" href="#">Action</a></li>
      <li><a class="dropdown-item" href="#">Actio</a></li>
    </ul>
  </div>
</template>

<style scoped>
.btn-secondary {
  color: black;
  background-color: white;
}

.btn-secondary:hover {
  color: black;
  background-color: white;
}

.btn.show {
  color: black;
  background-color: white;
}

.btn-group {
  border-radius: .3rem;
  box-shadow: 2px 2px 7px 2px rgba(62, 100, 237, 0.6);
}
</style>