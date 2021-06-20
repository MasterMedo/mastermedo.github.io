---
layout: home
title: home
---

<style>
.moonbox {
  background: #22354f;
  margin 20px;
  overflow: hidden;
  flex: 1;
  align-items: 'center';
  justify-content: center;
}

.moon {
  position: relative;
  left: 0;
  top: 0;
  bottom: 0;
  right: 0;
  margin: 10vw;
  width: 20vw;
  height: 20vw;
  border-radius: 50%;
  background-color: LightGrey;
}

.moon:after {
  position: absolute;
  z-index: 2;
  content: "";
  width: 20vw;
  height: 20vw;
  border-radius: 50%;
  background: transparent;
  box-shadow: -2.1333333333vw 1.6666666667vw 10px rgba(111, 111, 111, 0.3) inset, 0 0 1.3333333333vw 2px #0F0F0F, 0 0 10vw 6.6666666667vw rgba(255, 255, 255, 0.07);
  transform: rotate(70deg);
}

.spot-W {
  margin-top: 8vw;
  margin-left: -1vw;
  height: 3.3333333333vw;
  width: 0.8vw;
}

.spot-NW {
  margin-top: 6.6666666667vw;
  margin-left: 4vw;
  height: 5vw;
  width: 5vw;
}

.spot-N {
  margin-top: 0.5vw;
  margin-left: 6.6666666667vw;
  height: 0.8vw;
  width: 3.3333333333vw;
}

.spot-E {
  margin-top: 6.6666666667vw;
  margin-left: 15vw;
  height: 1.3333333333vw;
  width: 1.3333333333vw;
}

.spot-SE {
  margin-top: 13.2vw;
  margin-left: 11.25vw;
  height: 2.8571428571vw;
  width: 2.8571428571vw;
}

.spot-S {
  margin-top: 19vw;
  margin-left: 6.6666666667vw;
  height: 0.8vw;
  width: 3.3333333333vw;
}

.spot-SW {
  margin-top: 15vw;
  margin-left: 2.5vw;
  height: 1.3333333333vw;
  width: 1.3333333333vw;
}

.spot {
  z-index: 2;
  border-radius: 50%;
  position: absolute;
  background-color: DarkGrey;
  transform: translate(1.6666666667vw);
  box-shadow: 0.4vw 0 0 0 #7F7F7F inset, 0 0 1px 1px #4F4F4F;
}
</style>

<div class='moonbox'>
  <div class='moon'>
    <div class='spot spot-W'></div>
    <div class='spot spot-NW'></div>
    <div class='spot spot-N'></div>
    <div class='spot spot-E'></div>
    <div class='spot spot-SE'></div>
    <div class='spot spot-S'></div>
    <div class='spot spot-SW'></div>
  </div>
</div>
