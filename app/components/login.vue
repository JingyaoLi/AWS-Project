<template>
  <div>
    <Modal v-model="modal1" width="360px" :mask-closable="false" :closable="false">
      <p slot="header" style="color:black;text-align:center">
        <span>Login to Let's Go Party</span>
      </p>
      <div style="text-align:center">
        <Input
          v-model="name"
          class="input"
          size="large"
          placeholder="Your Name"
          v-show="signup_footer"
        />
        <Input v-model="email" class="input" size="large" placeholder="Email"/>
        <Input
          v-model="password"
          class="input"
          size="large"
          type="password"
          placeholder="password"
        />
        <Input
          v-model="phonenumber"
          class="input"
          size="large"
          type="text"
          placeholder="phone number"
          v-show="signup_footer"
        />
        <RadioGroup class="input" v-model="gender" v-show="signup_footer">
          <Radio label="male">
            <Icon type="md-male"/>
            <span>Boy</span>
          </Radio>
          <Radio label="female">
            <Icon type="md-female"/>
            <span>Girl</span>
          </Radio>
        </RadioGroup>
        <Input
          v-model="confirmation"
          class="input"
          size="large"
          placeholder="confirmation code"
          v-show="confir"
        />
      </div>
      <div slot="footer" v-show="signup_footer">
        <Button
          class="button"
          type="primary"
          size="large"
          long
          :loading="modal_loading1"
          @click="signup"
        >Sign up</Button>
        <Button
          class="button"
          type="primary"
          size="large"
          long
          :loading="modal_loading2"
          @click="switch_"
        >Already Have Account? Login</Button>
        <Button
          class="button"
          type="primary"
          size="large"
          long
          :loading="modal_loading2"
          @click="confirm"
          v-show="confirbtn"
        >Confirm</Button>
      </div>
      <div slot="footer" v-show="login_footer">
        <Button
          class="button"
          type="primary"
          size="large"
          long
          :loading="modal_loading1"
          @click="signin"
        >Sign in</Button>
        <Button
          class="button"
          type="primary"
          size="large"
          long
          :loading="modal_loading2"
          @click="switch_"
        >No Account ? Signup</Button>
      </div>
    </Modal>
  </div>
</template>

<script>
import {
  Register,
  Confrim,
  Signin,
  getCurrentUser,
  getUserEmail
} from "../utils/cognito";
import { Modal, Icon, Button, Input, Message, RadioGroup, Radio } from "iview";
import { SignUpDb } from "../utils/data";

export default {
  components: {
    Modal,
    Icon,
    Button,
    Input,
    Message,
    RadioGroup,
    Radio
  },
  created() {
    getCurrentUser()
      .then(r => {
        this.$router.push("/home");
      })
      .catch(j => {
        Message.warning({
          content: "Please Login",
          duration: 3
        });
      });
  },
  data() {
    return {
      modal1: true,
      modal_loading1: false,
      modal_loading2: false,
      signup_footer: true,
      login_footer: false,
      name: null,
      email: null,
      password: null,
      confirmation: null,
      confir: false,
      confirbtn: false,
      phonenumber: null,
      gender: null
    };
  },
  methods: {
    switch_() {
      this.modal_loading2 = true;
      this.signup_footer = !this.signup_footer;
      this.login_footer = !this.login_footer;
      this.modal_loading2 = false;
    },
    signup() {
      if (!this.name || !this.name || !this.name) {
        Message.warning({
          content: "please enter your info completely",
          duration: 3
        });
        return;
      }
      const param = {
        name: this.name,
        email: this.email,
        password: this.password
      };
      Register(param)
        .then(r => {
          Message.success({
            content: r,
            duration: 3
          });
          SignUpDb({
            userName: this.name,
            userEmail: this.email,
            phone_number:this.phonenumber,
            gender: this.gender
          }).then(r=>{
            Message.success({
              content: r.data.body,
              duration:3
            });
          });
          this.confir = true;
          this.confirbtn = true;
        })
        .catch(j => {
          Message.error({
            content: j,
            duration: 5
          });
        });
    },
    confirm() {
      if (!this.confirmation) {
        Message.warning({
          content: "please enter your confirmation code",
          duration: 3
        });
        return;
      }
      Confrim(this.email, this.confirmation)
        .then(r => {
          Message.success({
            content: r,
            duration: 3
          });
          this.confir = false;
          this.confirbtn = false;
          this.switch_();
        })
        .catch(j => {
          Message.error({
            content: j,
            duration: 5
          });
        });
    },
    signin() {
      if (!this.email || !this.password) {
        Message.warning({
          content: "please enter your info completely",
          duration: 3
        });
        return;
      }
      const param = {
        email: this.email,
        password: this.password
      };
      Signin(param)
        .then(r => {
          Message.success({
            content: r,
            duration: 3
          });
          this.$router.push("/home");
        })
        .catch(j => {
          Message.error({
            content: j,
            duration: 5
          });
        });
    }
  }
};
</script>

<style lang="scss" scoped>
.button {
  margin: 2px;
}
.input {
  margin: 2px;
}
</style>

