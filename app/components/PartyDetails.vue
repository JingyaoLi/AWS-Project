<template>
  <div>
    <Col span="12">
      <Card class="content" style="min-height: 800px">
        <CellGroup>
          <Cell class="cell" :label="partybody.partyName">
            <label>
              <Icon type="ios-beer"/>Party Name
            </label>
          </Cell>
          <Cell class="cell" :label="partybody.hostEmail">
            <label>
              <Icon type="ios-man"/>Party Owner
            </label>
          </Cell>
          <Cell class="cell" :label="category">
            <label>
              <Icon type="ios-options"/>Category
            </label>
          </Cell>
          <Cell class="cell">
            <label>
              <Icon type="md-alarm"/>Start time:
              <DatePicker
                type="datetime"
                disabled
                v-model="partybody.startTime"
                style="width: 200px"
              ></DatePicker>
            </label>
          </Cell>
          <Cell class="cell">
            <label>
              <Icon type="md-alarm"/>End time:
              <DatePicker type="datetime" disabled v-model="partybody.endTime" style="width: 200px"></DatePicker>
            </label>
          </Cell>
          <Cell class="cell" :label="partybody.placeName">
            <label>
              <Icon type="ios-pin-outline"/>Place:
            </label>
          </Cell>
          <Cell class="cell" :label="partybody.address">
            <label>
              <Icon type="ios-pin"/>Location:
            </label>
          </Cell>
          <Cell class="cell" :label="num">
            <label>
              <Icon type="ios-people"/>Number Limitation
            </label>
          </Cell>
          <Cell class="cell" :label="partybody.discription">
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
        <Button icon="md-add" @click="attend" class="button" type="success" size="large">Attend</Button>
        <Button icon="md-close" @click="cancel" class="button" type="error" size="large">Cancel</Button>
        <Button icon="md-create" class="button" type="info" size="large" @click="edit">Edit Party</Button>
        <edit-party :show="partymodal" :party="partybody"></edit-party>
      </Card>
    </Col>
    <Col span="12">
      <Card class="content">
        <div style="min-height: 763px">
          <Icon type="ios-map"/>Map
          <div id="googleMap" style="width:100%;height:750px;"></div>
        </div>
      </Card>
    </Col>
  </div>
</template>

<script>
import { getUserEmail } from "../utils/cognito";
import { getParty, attendParty, cancelParty, rateParty } from "../utils/data";
import EditParty from "./EditParty.vue";
import {
  Col,
  Card,
  Icon,
  Cell,
  CellGroup,
  Button,
  Rate,
  Message,
  DatePicker,
  Row
} from "iview";
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
    Message,
    DatePicker,
    Row
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
      rateValue: 0,
      partybody: {},
      category: null,
      num: null,
      lag: 39.983245,
      lng: 116.315509
    };
  },
  mounted() {
    getParty({
      partyId: this.party,
      userEmail: getUserEmail()
    }).then(r => {
      this.partybody = r["data"]["body"];
      this.category = this.partybody.category.toString();
      this.num = this.partybody.maxNumber.toString();
      if (this.partybody.rate) {
        this.rateValue = this.partybody.rate;
      }
      this.createMap();
    });
  },
  methods: {
    edit() {
      this.partymodal = !this.partymodal;
    },
    rate() {
      rateParty({
        partyid: this.partybody.id,
        userEmail: getUserEmail(),
        ratingpoints: this.rateValue,
        ratingreview: "N/A"
      }).then(r => {
        Message.success({
          content: "Rate Successully",
          duration: 3
        });
      });
    },
    attend() {
      attendParty({
        partyId: this.partybody.id,
        userEmail: getUserEmail()
      }).then(r => {
        Message.success({
          content: "Attend Successully",
          duration: 3
        });
      });
    },
    cancel() {
      cancelParty({
        partyId: this.partybody.id,
        userEmail: getUserEmail()
      }).then(r => {
        Message.success({
          content: "Cancel Successully",
          duration: 3
        });
      });
    },
    createMap() {
      this.initialize();
    },
    initialize() {
      let myCenter = new google.maps.LatLng(
        parseFloat(this.partybody.lat),
        parseFloat(this.partybody.lng)
      );
      var mapProp = {
        center: myCenter,
        zoom: 15,
        mapTypeId: google.maps.MapTypeId.ROADMAP
      };

      var map = new google.maps.Map(
        document.getElementById("googleMap"),
        mapProp
      );

      var marker = new google.maps.Marker({
        position: myCenter,
        title: "Click to zoom"
      });

      marker.setMap(map);

      // Zoom to 9 when clicking on marker
      google.maps.event.addListener(marker, "click", function() {
        map.setZoom(15);
        map.setCenter(marker.getPosition());
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
  padding: 2%;
}
</style>
