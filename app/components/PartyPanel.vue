<template>
  <div>
    <Search></Search>
    <Row>
      <Col span="6" v-for="(item, index) in partylist" :key="index">
        <Card
          class="card"
          title="Party Information"
          icon="ios-options"
          :padding="0"
          shadow
        >
          <CellGroup>
            <Cell title="Party owner" :label="item.owner"/>
            <Cell title="Short discription" :label="item.discription"/>
            <Cell title="Location" :label="item.location"/>
            <Cell title="Time" :label="item.time"/>
            <Cell title="Link" extra="details" @click.native="showPartyDetail($event, item)"/>
          </CellGroup>
        </Card>
      </Col>
    </Row>
    <Button icon="md-add" class="button" type="success" size="large" @click="newParty">New Party</Button>
    <party-info :show="partymodal"></party-info>
  </div>
</template>

<script>
import Search from "./search.vue";
import PartyInfo from "./PartyInfo.vue";
import { Card, Cell, CellGroup, Col, Button, Row } from "iview";

export default {
  components: {
    Search,
    Cell,
    Card,
    CellGroup,
    Col,
    Button,
    Row,
    PartyInfo
  },
  data() {
    return {
      switchValue: null,
      partymodal:false,
      partylist: [
        {
          owner: "29asdsad@qq.com",
          discription: "short discription",
          location: "450 83rd St, Brooklyn, 11201",
          time: "2018-12-31"
        },
        {
          owner: "adasdad",
          discription: "short discription",
          location: "450 83rd St, Brooklyn, 11201",
          time: "2018-12-31"
        },
        {
          owner: "291978313@qq.com",
          discription: "short discription",
          location: "450 83rd St, Brooklyn, 11201",
          time: "2018-12-31"
        },
        {
          owner: "291978313@qq.com",
          discription: "short discription",
          location: "450 83rd St, Brooklyn, 11201",
          time: "2018-12-31"
        },
        {
          owner: "291978313@qq.com",
          discription: "short discription",
          location: "450 83rd St, Brooklyn, 11201",
          time: "2018-12-31"
        },
        {
          owner: "291978313@qq.com",
          discription: "short discription",
          location: "450 83rd St, Brooklyn, 11201",
          time: "2018-12-31"
        },
        {
          owner: "291978313@qq.com",
          discription: "short discription",
          location: "450 83rd St, Brooklyn, 11201",
          time: "2018-12-31"
        }
      ]
    };
  },
  methods:{
      newParty(){
          this.partymodal = !this.partymodal;
      },
      showPartyDetail(event, item){
        this.$router.push({
            path: '/home/partydetails', 
            query: { 
                id: item.owner
            }
        });
      }
  }
};
</script>

<style lang="scss" scoped>
.card {
  margin: 3px;
}
.button{
    margin-left: 45%;
    margin-top: 6px;
}
</style>

