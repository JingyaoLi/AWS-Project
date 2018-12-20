<template>
    <div>
        Home 界面
    </div>
</template>

<script>
import { getUserEmail } from "../utils/cognito";

export default {
    created(){
        if(!getUserEmail()){
            this.$router.push('/login');
        }
    }
}
</script>
