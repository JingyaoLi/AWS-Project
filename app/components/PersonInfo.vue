<template>
  <div>
    <Modal
      v-model="modal1"
      :mask-closable="false"
      width="600px"
      title="Edit Personal Information"
      @on-ok="updateInfo"
    >
      <Input v-model="name" class="input" size="large" placeholder="Name"/>
      <RadioGroup class="input" v-model="gender">
        <Radio label="male">
          <Icon type="md-male"/>
          <span>Boy</span>
        </Radio>
        <Radio label="female">
          <Icon type="md-female"/>
          <span>Girl</span>
        </Radio>
      </RadioGroup>
      <Input v-model="phone_number" class="input" size="large" placeholder="phone"/>
      <div>
        <Select
          class="input"
          v-model="hobby"
          multiple
          style="width:300px;padding-left:1px"
          placeholder="Select hobbies"
        >
          <Option v-for="item in hobbylist" :value="item.value" :key="item.value">{{ item.label }}</Option>
        </Select>
      </div>
      <DatePicker
        v-model="birthday"
        class="input"
        type="date"
        placeholder="Select birthday"
        style="width:300px;padding-left:1px"
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
  DatePicker,
  Message
} from "iview";

import { getUserEmail } from "../utils/cognito";
import { getUserInfo, updataUserInfo } from "../utils/data";

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
    Message
  },
  created() {
    this.email = getUserEmail();
    console.log(this.email);
    getUserInfo({ email: this.email }).then(r => {
      console.log(r);
      if (r["data"]["body"]["name"]) {
        this.name = r["data"]["body"]["name"];
      }
      if (r["data"]["body"]["gender"]) {
        this.gender = r["data"]["body"]["gender"];
      }
      if (r["data"]["body"]["hobby"]) {
        this.hobby = r["data"]["body"]["hobby"];
      }
      if (r["data"]["body"]["birthday"]) {
        this.birthday = r["data"]["body"]["birthday"];
      }
      if (r["data"]["body"]["phone_number"]) {
        this.phone_number = r["data"]["body"]["phone_number"];
      }
    });
  },
  props: ["show"],
  data() {
    return {
      email: null,
      modal1: this.show,
      name: null,
      gender: null,
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
      hobby: [],
      birthday: null,
      phone_number: null
    };
  },
  methods: {
    updateInfo() {
      let params = {
        email: this.email,
        name: this.name,
        gender: this.gender,
        hobby: this.hobby,
        birthday: this.birthday,
        phone_number: this.phone_number
      };
      updataUserInfo(params).then(r => {
        Message.success({
          content: "Update successfully",
          duration: 3
        });
      });
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
