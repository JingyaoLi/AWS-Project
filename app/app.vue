<template>
  <div>
    <router-view></router-view>
  </div>
</template>

<script>
import { getCurrentUser } from './utils/cognito';
import { Message } from "iview";
export default {
  name: "app",
  components: {
     
  },
  created() {
    getCurrentUser()
      .then(r => {
        // this.$router.push('/home');
      })
      .catch(j => {
        this.$router.push('/login');
      });
  }
};
</script>
