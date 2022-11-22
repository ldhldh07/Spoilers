<template>
  <div class="text-nowrap">
    <div id="warning-banner">
      <p id="warning-words" class="fs-4">NING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING</p>
      <div id="warning-block" class="d-flex flex-column justify-content-center align-items-center">
        <h1 id="warning-title">스포일러 주의</h1>
        <h2 id="warning-content">이 사이트는 특정 스토리나 설정에 대한 스포일러를 포함하고 있습니다</h2>
      </div>
      <p id="warning-words" class="text-nowrap fs-4">RNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING</p>
    </div>
    <!-- <div id="intro">
      <div class="d-flex">
      <p id="logo">Spoilers</p>
      <p>에 오신 걸 환영합니다!</p>
      </div>
      <p>영화를 보실 시간이 없나요?</p>
      <p>자신만 모르는 영화가 이야깃거리가 되고 있나요?</p>
      <p>Spoilers에서 모든 스포일러를 확인하세요!</p>
      <p>쉽고 빠르게, 원하는 영화의 모든 정보를 확인하실 수 있습니다.</p>
    </div> -->
  </div>
</template>
  
<script>

</script>

<style>
#warning-banner{
  position: absolute;
  width: 100vw;
  left: 0px;
  top: 25vh
}

#warning-block {
  color: white;
  background-color: rgb(255, 44, 44);
  height: auto;
  padding: 3rem;
}

#warning-words{
  color: rgb(229, 44, 44);
  overflow: hidden;
  margin-top: 0.5rem;
  margin-bottom: 0.5rem;
}

#warning-title{
  font-size: 4vw;
  margin-bottom: 3vw;
}
#warning-content{
  font-size: 2vw;
}

#intro{
  position: absolute;
  top: warning-words
}
</style>
  