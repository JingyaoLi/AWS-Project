<template>
  <div>
    <Modal
      v-model="modal2"
      :mask-closable="false"
      title="Edit Party Information"
      @on-ok="createParty"
    >
      <Input v-model="name" class="input" size="large" placeholder="Name"/>
      <Select
        class="input"
        v-model="hobby"
        multiple
        style="width:300px;padding-left:1px"
        placeholder="Categroy"
      >
        <Option v-for="item in hobbylist" :value="item.value" :key="item.value">{{ item.label }}</Option>
      </Select>
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
      <div style="padding-left:6px">
        <span>Number of people:</span>
        <InputNumber class="input" :max="200" :min="0" v-model="num"></InputNumber>
      </div>
      <Input v-model="location" class="input" size="large" placeholder="Location"/>
      <Input v-model="discription" class="input" size="large" placeholder="Discription"/>
    </Modal>
  </div>
</template>

<script>
import { getUserEmail } from "../utils/cognito";
import { createPartyDb } from "../utils/data";

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
    TimePicker,
    Message
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
      startdatetime: null,
      enddatetime: null,
      num: null,
      location: null,
      discription: null,
      email: null,
      hobbylist: [
        {
          value: "Dance",
          label: "Dance"
        },
        {
          value: "Singing",
          label: "Singing"
        },
        {
          value: "Reading",
          label: "Reading"
        },
        {
          value: "Game",
          label: "Game"
        },
        {
          value: "Study",
          label: "Study"
        },
        {
          value: "Sport",
          label: "Sport"
        }
      ],
      hobby: []
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
        hostEmail: this.email,
        name: this.name,
        startTime:this.startdatetime,
        endTime: this.enddatetime,
        maxNumber: this.num,
        address: this.location,
        discription: this.discription,
        category: this.hobby
      };
      createPartyDb(param).then(r => {
        Message.success({
          content: "Create party successfully",
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