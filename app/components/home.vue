<template>
    <div>
        <header-menu></header-menu>
    </div>
</template>

<script>
import HeaderMenu from './HeaderMenu.vue';
import { getUserEmail } from "../utils/cognito";

export default {
    components:{
        HeaderMenu
    },
    created(){
        if(!getUserEmail()){
            this.$router.push('/login');
        }
    }
}
</script>
