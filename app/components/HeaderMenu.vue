<template>
  <div>
    <Menu mode="horizontal" :theme="theme" active-name="1">
      <MenuItem name="1" @click.native="toHome">
        <Icon type="md-home"/>Home
      </MenuItem>
      <MenuItem name="2" @click.native="myInfo">
        <Icon type="md-person"/>Me
      </MenuItem>
      <Submenu name="3">
        <template slot="title">
          <Icon type="ios-stats"/>My Parities
        </template>
        <MenuItem name="1-1" @click.native="toHost">
          <Icon type="ios-contact"/>Host
        </MenuItem>
        <MenuItem name="2-1" @click.native="toGuest">
          <Icon type="md-contacts"/>Guest
        </MenuItem>
      </Submenu>
    </Menu>
    <person-info :show="personmodal"></person-info>
  </div>
</template>

<script>
import { Menu, MenuItem, Icon, Submenu, MenuGroup } from "iview";
import PersonInfo from "./PersonInfo.vue";

export default {
  components: {
    Menu,
    MenuItem,
    Icon,
    Submenu,
    MenuGroup,
    PersonInfo
  },
  data() {
    return {
      theme: "dark",
      personmodal: false
    };
  },
  methods: {
    myInfo() {
      this.personmodal = !this.personmodal;
    },
    toHome() {
      this.$router.push("/home");
    },
    toHost() {
      this.$router.push({
        path: "/home",
        query: {
          type: "host"
        }
      });
    },
    toGuest() {
      this.$router.push({
        path: "/home",
        query: {
          type: "guest"
        }
      });
    }
  }
};
</script>
