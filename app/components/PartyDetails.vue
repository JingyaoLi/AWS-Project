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
          <Button
            v-if="showratebtn"
            icon="ios-star"
            shape="circle"
            @click="showratemodel"
            class="button"
            type="dashed"
            size="small"
            style="margin: 2% 0% 2% 0%"
          >Rate</Button>
          <RateModal :rateV="rateValue" :show="showrate" :partyid="partybody.id"></RateModal>
        </div>
        <div>
          <Select v-model="friend2" style="width:50%;margin-bottom:2px" placeholder="Attend User">
            <Option v-for="(item, index) in friend" :value="item.email" :key="index">{{ item.name }}</Option>
          </Select>
          <Button
            icon="md-checkmark"
            shape="circle"
            @click="follow"
            class="button"
            type="info"
            size="small"
          >Follow</Button>
          <Button
            icon="md-close"
            shape="circle"
            @click="unfollow"
            class="button"
            type="warning"
            size="small"
          >Unfollow</Button>
        </div>
        <Button
          icon="md-add"
          v-if="!join&&!own&&!showratebtn"
          @click="attend"
          class="button"
          type="success"
          size="large"
        >Attend</Button>
        <Button
          icon="md-close"
          v-if="join&&!own&&!showratebtn"
          @click="cancel"
          class="button"
          type="error"
          size="large"
        >Cancel</Button>
        <Button
          icon="md-create"
          v-if="own&&!showratebtn"
          class="button"
          type="info"
          size="large"
          @click="edit"
        >Edit Party</Button>
        <Button
          icon="md-close"
          v-if="own"
          class="button"
          type="error"
          size="large"
          @click="deleted"
        >Delete Party</Button>
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
import {
  getParty,
  attendParty,
  cancelParty,
  followUser,
  unfollowUser,
  deleteParty
} from "../utils/data";
import EditParty from "./EditParty.vue";
import RateModal from "./rateModal.vue";
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
  Select,
  Option
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
    RateModal,
    Message,
    DatePicker,
    Select,
    Option
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
      friend: [],
      friend2: null,
      join: false,
      own: false,
      showrate: false,
      showratebtn: false
    };
  },
  mounted() {
    getParty({
      partyId: this.party,
      userEmail: getUserEmail()
    }).then(r => {
      this.partybody = r["data"]["body"];
      this.own = this.partybody.relation;
      this.join = this.partybody.status;
      this.category = this.partybody.category.toString();
      this.num = this.partybody.maxNumber.toString();
      this.partybody.startTime = new Date(this.partybody.startTime);
      this.partybody.endTime = new Date(this.partybody.endTime);
      if (new Date(this.partybody.endTime) < new Date()) {
        this.showratebtn = true;
        this.rateValue = parseFloat(this.partybody.rate);
      }
      for (let i = 0; i < this.partybody.attendPeople.length; i++) {
        this.friend.push(this.partybody.attendPeople[i]);
      }
      this.createMap();
    });
  },
  methods: {
    edit() {
      this.partymodal = !this.partymodal;
    },
    showratemodel() {
      this.showrate = !this.showrate;
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
        this.join = !this.join;
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
        this.join = !this.join;
      });
    },
    follow() {
      if (!this.friend2) {
        Message.warning({
          content: "Please select a user",
          duration: 3
        });
      } else {
        followUser({
          fromEmail: getUserEmail(),
          toEmail: this.friend2
        }).then(r => {
          Message.success({
            content: r["data"]["body"],
            duration: 3
          });
        });
      }
    },
    unfollow() {
      if (!this.friend2) {
        Message.warning({
          content: "Please select a user",
          duration: 3
        });
      } else {
        unfollowUser({
          fromEmail: getUserEmail(),
          toEmail: this.friend2
        }).then(r => {
          Message.success({
            content: r["data"]["body"],
            duration: 3
          });
        });
      }
    },
    deleted() {
      deleteParty({
        'partyId': this.partybody.id
      }).then(r => {
        Message.success({
          content:'Delete successfully',
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
