<template>
  <div>
    <Modal
      v-model="modal2"
      :mask-closable="false"
      title="Edit Party Information"
      @on-ok="createParty"
    >
      <Input v-model="name" class="input" size="large" placeholder="Name"/>
      <DatePicker
        v-model="startdatetime"
        class="input"
        type="datetime"
        placeholder="Start date"
        style="width:300px;padding-left:1px"
      ></DatePicker>
      <DatePicker
        v-model="enddatetime"
        class="input"
        type="datetime"
        placeholder="End date"
        style="width:300px;padding-left:1px"
      ></DatePicker>
      <Input v-model="location" class="input" size="large" placeholder="Location"/>
      <Input v-model="discription" class="input" size="large" placeholder="Discription"/>
    </Modal>
  </div>
</template>

<script>
import { getUserEmail } from "../utils/cognito";
import { testApi } from "../utils/data";

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
  TimePicker
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
  },
  props: ["show"],
  data() {
    return {
      modal2: false,
      name: null,
      startdatetime: "2019-01-01T18:00:00.000Z",
      enddatetime: null,
      num: null,
      location: null,
      discription: null,
      email: null,
    };
  },
  watch: {
    show() {
      this.modal2 = true;
    }
  },
  methods: {
    createParty() {
      let param = {
        email: this.email,
        name: this.name,
        startdatetime: this.startdatetime,
        enddatetime: this.enddatetime,
        num: this.num,
        location: this.num,
        discription: this.discription
      };
      console.log(param);
    }
  }
};
</script>

<style lang="scss" scoped>
.input {
  margin: 4px;
}
</style>