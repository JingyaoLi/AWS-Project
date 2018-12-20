<template>
    <Input v-model="keyword" class="input" @on-enter="search_" @on-click="search_" search enter-button placeholder="Search" />
</template>

<script>
import { Input , Button} from 'iview';

export default {
    components:{
        Input,
        Button
    },
    data(){
        return {
            keyword:null
        }
    },
    methods:{
        search_(){
            console.log('search for ' + this.keyword);
        }
    }
}
</script>

<style lang="scss" scoped>
    .input{
        text-align: center;
        width: 50%;
        margin: auto;
        margin-top: 10px;
    }
</style>
