<template>
  <div>
    <Modal v-model="modal" :mask-closable="false" title="Discover">
      <Carousel v-if="modal" dots="none" loop autoplay>
        <!--v-if强制让Carousel在Modal后渲染-->
        <CarouselItem v-for="(item, index) in discover" :key="index">
          <div class="message" @click="goto($event, item)">{{item.content}}</div>
        </CarouselItem>
      </Carousel>
    </Modal>
  </div>
</template>

<script>
import { Modal, Carousel, CarouselItem, Button } from "iview";
import { getDiscover } from "../utils/data";
import { getUserEmail } from "../utils/cognito";
export default {
  components: {
    Modal,
    Carousel,
    CarouselItem,
    Button
  },
  props: ["show"],
  created() {
    this.modal = this.show;
    getDiscover({
      userEmail: getUserEmail()
    }).then(r => {
      this.discover = r.data.body;
    });
  },
  data() {
    return {
      modal: null,
      message: null,
      discover: []
    };
  },
  watch: {
    show() {
      this.modal = true;
    }
  },
  methods: {
    goto(event, item) {
      this.$router.push({
        path: "/home/partydetails",
        query: {
          id: item.partyId
        }
      });
      if(this.$route.query.id){
        this.$router.go(0); // 当前二级路由页 刷新
      }
    }
  }
};
</script>

<style lang="scss" scoped>
.message {
  padding: 3% 0% 3% 0%;
}
</style>
