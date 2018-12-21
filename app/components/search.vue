<template>
    <div>
        <Input v-model="keyword" class="input"  @on-enter="search_" @on-click="search_" placeholder="Search" >
        <Select v-model="type" size="small" slot="prepend" style="width: 80px">
            <Option v-for="(item, index) in cateList" :value="item" :key="index">{{ item }}</Option>
        </Select>
        <Button slot="append" icon="ios-search" @click="search_"></Button>
    </Input>
    </div>
</template>

<script>
import { Input, Button, Select, Option} from 'iview';

export default {
    components:{
        Input,
        Button,
        Select,
        Option
    },
    data(){
        return {
            keyword:null,
            cateList: ['name', 'location', 'category'],
            type: null,
        }
    },
    methods:{
        search_(){
            this.$emit('search_', {
                keyword: this.keyword,
                type: this.type
            })
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
