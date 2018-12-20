<template>
  <div>
    <Modal v-model="modal1" width="600px" title="Edit Personal Info" @on-ok="updateInfo">
      <Input v-model="name" class="input" size="large" placeholder="Name"/>
      <RadioGroup class="input" v-model="gender">
        <Radio label="1">
          <Icon type="md-male"/>
          <span>Boy</span>
        </Radio>
        <Radio label="2">
          <Icon type="md-female"/>
          <span>Girl</span>
        </Radio>
      </RadioGroup>
      <div style="padding-left:6px">
        <span>Age:</span>
        <InputNumber class="input" :max="100" :min="0" v-model="age"></InputNumber>
      </div>
      <Select
        class="input"
        v-model="hobby"
        multiple
        style="width:300px;padding-left:3px"
        placeholder="Select hobbies"
      >
        <Option v-for="item in hobbylist" :value="item.value" :key="item.value">{{ item.label }}</Option>
      </Select>
      <DatePicker
        v-model="birthday"
        class="input"
        type="date"
        placeholder="Select date"
        style="width:300px;padding-left:3px"
      ></DatePicker>
    </Modal>
  </div>
</template>

<script>
import {
  Modal,
  Input,
  Radio,
  RadioGroup,
  Icon,
  InputNumber,
  Select,
  Option,
  DatePicker
} from "iview";

import { getUserEmail } from "../utils/cognito";

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
    DatePicker
  },
  created() {
    this.email = getUserEmail();
  },
  props: ["show"],
  data() {
    return {
      email: null,
      modal1: this.show,
      name: null,
      gender: null,
      age: null,
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
        }
      ],
      hobby: [],
      birthday: null
    };
  },
  methods: {
    updateInfo() {
      let params = {
        email: this.email,
        name: this.name,
        gender: this.gender,
        age: this.age,
        hobby: this.hobby,
        birthday: this.birthday
      };
      console.log(params);
    }
  },
  watch: {
    show() {
      this.modal1 = true;
    }
  }
};
</script>

<style lang="scss" scoped>
.input {
  margin: 4px;
}
</style>
