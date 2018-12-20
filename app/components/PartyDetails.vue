<template>
  <div>
    <Col span="12">
      <Card class="content" style="min-height: 800px">
        <CellGroup>
          <Cell class="cell" label="NYU tandon">
            <label>
              <Icon type="ios-beer"/>Party Name
            </label>
          </Cell>
          <Cell class="cell" label="291978313@qq.com">
            <label>
              <Icon type="ios-man"/>Hosted By User Name
            </label>
          </Cell>
          <Cell class="cell" label="Dance Game">
            <label>
              <Icon type="ios-options"/>Category
            </label>
          </Cell>
          <Cell class="cell" label="2018-12-12">
            <label>
              <Icon type="md-alarm"/>Time:
            </label>
          </Cell>
          <Cell class="cell" label="bay ridge">
            <label>
              <Icon type="ios-pin"/>Location:
            </label>
          </Cell>
          <Cell class="cell" label="30">
            <label>
              <Icon type="ios-people"/>Number Limitation
            </label>
          </Cell>
          <Cell class="cell" label="ASSP">
            <label>
              <Icon type="ios-paper"/>Discription :
            </label>
          </Cell>
        </CellGroup>
        <div>
          <Rate show-text allow-half v-model="rateValue" @on-change="rate">
            <span style="color: #f5a623">{{ rateValue }}</span>
          </Rate>
        </div>
        <Button icon="md-add" class="button" type="success" size="large">Attend</Button>
        <Button icon="md-close" class="button" type="error" size="large">Cancel</Button>
        <Button icon="md-create" class="button" type="info" size="large" @click="edit">Edit Party</Button>
        <edit-party :show="partymodal"></edit-party>
      </Card>
    </Col>
    <Col span="12">
      <Card class="content">
        <div style="min-height: 400px">
          <Icon type="ios-map"/>Map
        </div>
      </Card>
    </Col>
  </div>
</template>

<script>
import { getUserEmail } from "../utils/cognito";
import EditParty from "./EditParty.vue";
import { Col, Card, Icon, Cell, CellGroup, Button, Rate, Message } from "iview";
export default {
  components: {
    Col,
    Card,
    Icon,
    Cell,
    CellGroup,
    Button,
    EditParty,
    Rate,
    Message
  },
  created() {
    if (!getUserEmail()) {
      this.$router.push("/home");
    }
    this.party = this.$route.query.id;
  },
  data() {
    return {
      party: null,
      partymodal: false,
      rateValue: 3.4
    };
  },
  methods: {
    edit() {
      this.partymodal = !this.partymodal;
    },
    rate(){
        Message.success({
            content: 'Rate Successully',
            duration: 3
        });
    }
  }
};
</script>

<style lang="scss">
.content {
  margin: 2%;
}
.cell {
  padding: 3%;
}
</style>
