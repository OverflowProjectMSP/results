<script>

</script>
<template>
  <div class="card mb-3" style="max-width: 300px; margin: auto;">
    <h5 class="title card-title">Программирует на</h5>
    <div class="row g-0">
      <div class="d-flex justify-content-around">
        <img src="../../assets/js.jpg" class=" image img-fluid rounded-start" alt="...">
        <div class="card-body">
          <p class="card-title">JavaScript <br> работатет с <br> файлом index.js</p>
        </div>
      </div>
      <div class="d-flex justify-content-around ">
        <span class="time card-title" type="time">12:53:50</span>
        <button type="button" class="width btn btn-primary ">Стоп</button>
        <button type="button" class="btn btn-primary btn-sm"><img src="../../assets/video-pause-button.png"
            width="25px"></button>
      </div>
    </div>
  </div>
</template>
<style scoped>
.btn {
  margin: 5px;
  font-size: 10px;
}

.image {
  margin: 5px;
  width: 80px;
  height: 80px;
}

.card {
  background-color: #3b82f6;
}

.time {
  margin: 5px;
}

.card-title {
  font-weight: bold;
  font-size: 14px;
}

.title {
  margin: 5px;
}

.width {
  width: 100px;
}
</style>