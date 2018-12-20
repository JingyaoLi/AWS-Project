<template>
  <div>
    <Search></Search>
    <Row>
      <Col span="6" v-for="(item, index) in partylist" :key="index">
        <Card class="card" title="Party Information" icon="ios-options" :padding="0" shadow>
          <CellGroup>
            <Cell title="Party name" :label="item.partyName"/>
            <Cell title="Party owner" :label="item.hostEmail"/>
            <Cell title="Short discription" :label="item.discription"/>
            <Cell title="Location" :label="item.placeName"/>
            <Cell title="start time" :label="item.startTime"/>
            <Cell title="end time" :label="item.endTime"/>
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
import { DisplayHome } from "../utils/data";

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
  created() {
    let param = {
      type: "name",
      keyword: ""
    };
    DisplayHome(param).then(r => {
      this.partylist = r["data"]["partyLists"];
    });
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
</style>

