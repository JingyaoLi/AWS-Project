<template>
  <div>
    <Modal v-model="modal" :mask-closable="false" title="Rate" @on-ok="rate">
      <Rate show-text allow-half v-model="rateValue">
        <span style="color: #f5a623">{{ rateValue }}</span>
      </Rate>
      <Input type="text" placeholder="comment" v-model="comment"/>
    </Modal>
  </div>
</template>

<script>
import { Modal, Rate, Input, Message } from "iview";
import { rateParty } from "../utils/data";
import { getUserEmail } from "../utils/cognito";
export default {
  components: {
    Modal,
    Rate,
    Input,
    Message
  },
  props: ["show", "rateV", "partyid"],
  created() {
    this.rateValue = this.rateV;
    this.modal = this.show;
  },
  data() {
    return {
      modal: null,
      rateValue: null,
      comment: ""
    };
  },
  watch: {
    show() {
      this.modal = true;
    },
    rateV(nv) {
      this.rateValue = nv;
    }
  },
  methods: {
    rate() {
      rateParty({
        partyid: this.partyid,
        userEmail: getUserEmail(),
        ratingpoints: this.rateValue,
        ratingreview: !this.comment ? 'no comment' : this.comment
      }).then(r => {
        Message.success({
          content: "Rate Successully",
          duration: 3
        });
      });
    }
  }
};
</script>

<style lang="scss" scoped>
.message {
  padding: 3% 0% 3% 0%;
}
</style>
