<template>
  <div>
    <Search @search_="searchParty"></Search>
    <Button icon="md-add" class="button" type="success" size="large" @click="newParty">New Party</Button>
    <Row>
      <Col span="6" v-for="(item, index) in partylist" :key="index">
        <Card class="card" title="Party Information" icon="ios-options" :padding="0" shadow>
          <CellGroup>
            <Cell title="Party name" :label="item.partyName"/>
            <Cell title="Party owner" :label="item.hostEmail"/>
            <Cell title="Short discription" :label="item.discription"/>
            <Cell title="Location" :label="item.placeName"/>
            <Cell title="Start time"/>
            <DatePicker class="picker" type="datetime" disabled v-model="item.startTime" size="small"></DatePicker>
            </Cell>
            <Cell title="End time"/>
            <DatePicker class="picker" type="datetime" disabled v-model="item.endTime" size="small"></DatePicker>
            </Cell>
            <Cell title="Link" extra="details" @click.native="showPartyDetail($event, item)"/>
          </CellGroup>
        </Card>
      </Col>
    </Row>
    <party-info :show="partymodal"></party-info>
  </div>
</template>
<script>
import Search from "./search.vue";
import PartyInfo from "./PartyInfo.vue";
import { Card, Cell, CellGroup, Col, Button, Row, DatePicker, Message } from "iview";
import { DisplayHome, getHostParty, getGuestParty, searchPartyDb } from "../utils/data";
import { getUserEmail } from '../utils/cognito';

export default {
  components: {
    Search,
    Cell,
    Card,
    CellGroup,
    Col,
    Button,
    Row,
    PartyInfo,
    DatePicker,
    Message
  },
  created() {
      this.changerouter(this.$route.query.type);
  },
  data() {
    return {
      switchValue: null,
      partymodal: false,
      partylist: []
    };
  },
  methods: {
    newParty() {
      this.partymodal = !this.partymodal;
    },
    showPartyDetail(event, item) {
      this.$router.push({
        path: "/home/partydetails",
        query: {
          id: item.id
        }
      });
    },
    changerouter(querytype){
      if(querytype){
            if(querytype === 'host'){
              getHostParty({
                  hostEmail: getUserEmail()
                }).then(r=>{
                  this.partylist = this.changeDate(r["data"]["partyLists"]);
                });
            }else{
                getGuestParty({
                  guestEmail: getUserEmail()
                }).then(r => {
                  this.partylist = this.changeDate(r["data"]["partyLists"]);
                });
            }
          }else{
            DisplayHome({
              type: "name",
              keyword: ""
            }).then(r => {
              this.partylist = this.changeDate(r["data"]["partyLists"]);
            });
          }
    },
    searchParty(val){
      if(!val.keyword || !val.type){
        Message.warning({
          content: 'Please enter both keyword and category!',
          duration:3
        });
      }else{
        searchPartyDb(val).then(r=>{
          this.partylist = this.changeDate(r["data"]["partyLists"]);
        });
      }
    },
    changeDate(partylist){
      for(let i = 0; i < partylist.length; i++){
          partylist[i].startTime = new Date(partylist[i].startTime);
          partylist[i].endTime = new Date(partylist[i].endTime);
      }
      return partylist;
    }
  },
  watch:{
     $route(nv, ov){
       this.changerouter(nv.query.type);
     }
  }
};
</script>

<style lang="scss" scoped>
.card {
  margin: 3px;
}
.button {
  margin-left: 45%;
  margin-top: 6px;
}
.picker{
  padding-left: 3%;
}
</style>

