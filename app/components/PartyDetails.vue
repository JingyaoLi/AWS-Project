<template>
    <div>
        {{party}}
    </div>
</template>

<script>
import { getUserEmail } from "../utils/cognito";

export default {
    created(){
        if(!getUserEmail()){
            this.$router.push('/home');
        }
        this.party = this.$route.query.id;
    },
    data(){
        return{
            party:null
        }
    }
}
</script>
