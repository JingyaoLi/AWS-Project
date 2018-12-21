<template>
  <div>
    <Modal
      v-model="modal2"
      :mask-closable="false"
      title="Edit Party Information"
      @on-ok="updateParty"
    >
      <Input v-model="partybody.partyName" class="input" size="large" placeholder="Name"/>
      <DatePicker
        v-model="partybody.startTime"
        class="input"
        type="datetime"
        placeholder="Start date"
        style="width:300px;padding-left:1px"
      ></DatePicker>
      <DatePicker
        v-model="partybody.endTime"
        class="input"
        type="datetime"
        placeholder="End date"
        style="width:300px;padding-left:1px"
      ></DatePicker>
      <Input v-model="partybody.address" class="input" size="large" placeholder="Location"/>
      <Input v-model="partybody.discription" class="input" size="large" placeholder="Discription"/>
    </Modal>
  </div>
</template>

<script>
import { getUserEmail } from "../utils/cognito";
import { updatePartyDb } from "../utils/data";

import {
  Modal,
  Input,
  Radio,
  RadioGroup,
  Icon,
  InputNumber,
  Select,
  Option,
  DatePicker,
  TimePicker,
  Message
} from "iview";

export default {
  components: {
    Modal,
    Input,
    RadioGroup,
    Radio,
    Icon,
    InputNumber,
    Select,
    Option,
    DatePicker,
    TimePicker
  },
  created() {
    this.modal2 = this.show;
    this.email = getUserEmail();
    this.partybody = this.party;
    this.partybody.startTime = new Date(this.partybody.startTime);
    this.partybody.endTime = new Date(this.partybody.endTime);
  },
  props: ["show", "party"],
  data() {
    return {
      modal2: false,
      email: null,
      partybody: null
    };
  },
  watch: {
    show() {
      this.modal2 = true;
    },
    party() {
      this.partybody = this.party;
    }
  },
  methods: {
    updateParty() { // new Date(this.partybody.startTime - this.partybody.startTime.getTimezoneOffset() * 60000),
      let param = {
        partyId: this.partybody.id,
        hostEmail: this.partybody.hostEmail,
        name: this.partybody.partyName,
        startTime: this.partybody.startTime,
        endTime: this.partybody.endTime,
        address: this.partybody.address,
        discription: this.partybody.discription
      }
      updatePartyDb(param).then(r => {
        Message.success({
          content: 'update successfully!',
          duration: 3
        });
      });
    }
  }
};
</script>

<style lang="scss" scoped>
.input {
  margin: 4px;
}
</style>