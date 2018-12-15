<template>
    <div>
        <Button type="info" @click="s">Button</Button>
        <Modal v-model="visible" @on-ok="ok" @on-cancel="cancel" title="Test Model">
            <Input prefix="ios-contact" placeholder="Enter name" type="text" v-model="name"/>
            <Rate v-model="star" />
        </Modal>
    </div>
</template>

<script>
import { Button, Modal, Message, Input, Rate } from 'iview';
export default {
    components:{
        Button,
        Modal,
        Message,
        Input,
        Rate
    },
    data(){
        return{
            visible:false,
            name:"",
            star:0
        }
    },
    created(){
        console.log('initial');
    },
    methods:{
        s(){
            this.visible = true;
        },
        ok(){
            console.log('on ok!');
            Message.success('Saved');
            console.log(this.star);
        },
        cancel(){
            Message.warning('Canceled');
            console.log(this.star);
        }
    }
}
</script>
