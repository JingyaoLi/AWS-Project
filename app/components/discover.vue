<template>
  <div>
    <Modal v-model="modal" :mask-closable="false" title="Discover">
      <Carousel v-if="modal" dots="none" loop autoplay>
        <!--v-if强制让Carousel在Modal后渲染-->
        <CarouselItem>
          <div class="message">我啊上达到</div>
        </CarouselItem>
        <CarouselItem>
          <div class="message">2asdsadas</div>
        </CarouselItem>
        <CarouselItem>
          <div class="message">3asdsadasd</div>
        </CarouselItem>
        <CarouselItem>
          <div class="message">4asdasdasda</div>
        </CarouselItem>
      </Carousel>
    </Modal>
  </div>
</template>

<script>
import { Modal, Carousel, CarouselItem } from "iview";
import { getDiscover } from "../utils/data";
import { getUserEmail } from "../utils/cognito";
export default {
  components: {
    Modal,
    Carousel,
    CarouselItem
  },
  props: ["show"],
  created() {
    this.modal = this.show;
    getDiscover({
      userEmail: getUserEmail()
    }).then(r => {
      console.log(r.data.body);
    });
  },
  data() {
    return {
      modal: null,
      message: null
    };
  },
  watch: {
    show() {
      this.modal = true;
    }
  }
};
</script>

<style lang="scss" scoped>
.message {
  padding: 3% 0% 3% 0%;
}
</style>
