<template>
<div>
  <div v-if="loading" class="loader lds-ellipsis"><div></div><div></div><div></div><div></div></div>   

  <div v-else>
    <h1 class="content-title">{{title}}</h1>
    <b-button v-b-modal.modal-1 class="share-btn" variant="dark" @click="getUsers()">
      <a href="#openModal">
        <font-awesome-icon icon="fa-solid fa-arrow-up-from-bracket" class="share-icon"/>
      </a>
    </b-button>
    <div id="openModal" class="modalDialog">
      <div>	
        <a href="#contents" title="Close" class="close">X</a>
        <h2>Share content</h2>
        <p> choose a user to share content with</p>
      <div>
      <div v-if="loadingUsers" class="lds-ellipsis"><div></div><div></div><div></div><div></div></div>   
      <b-form-select class="mt-3" v-if="!loadingUsers" v-model="selected" :options="options" :select-size="4"></b-form-select>
      <div class="mt-3">
      <b-button class="modal-share-btn" variant="dark" @click="share()">
        <a href="#contents">
          share
        </a>
      </b-button>
      </div>
    </div>
      </div>
    </div>
    
    <div>
    <div class="table-container">
      <table>
        <thead>
          <tr>
            <th>field</th>
            <th>value</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(k, v) in extra" :key="k">
            <td class="field-table">{{v}}</td>
            <td class="value-table">{{k}}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <b-button class="content-btn" variant="dark">
        <a target=”_blank” :href="file" download>file</a>
    </b-button>
    <b-button class="att-content-btn" variant="dark">
        <a target=”_blank” :href="attach" download> attachment </a>
    </b-button>
    </div>

  </div>
</div>
</template>

<script>
import Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";
Vue.use(VueAxios, axios);

export default {
    props: {
        loading: Boolean,
        title: String,
        extra: Object,
        file: String,
        attach: String,
        id: String,
    },
    data(){
        return{
          loadingUsers: false,
          options : [],
          selected: '',
        }
    },
    methods: {
      getUsers () {
      this.loadingUsers = true
      let api = "http://127.0.0.1:8000/user/list/" + this.id;
      Vue.axios.get(api, {
        headers: {
          'Authorization': "Token " + localStorage.getItem('token')
        }
      })
      .then(response => {
          this.options = []
          let users = response.data;
          for (let index = 0; index < users.length; index++) {
            this.options.push({
              "value": users[index].id,
              "text": users[index].username
            })
          }
          console.log(this.options)
          this.loadingUsers = false;
      }) 
      },
      share() {
        let api = "http://127.0.0.1:8000/content/share/"
        const data = {
          "user_id" : this.selected,
          "content_id" : this.id
        }
        Vue.axios.post(api,data ,{
        headers: {
          'Authorization': "Token " + localStorage.getItem('token')
        }
      })
      // eslint-disable-next-line no-unused-vars
      .then(response => {
          this.options = []
          this.selected = ''
          this.$router.replace("/contents");
      })    
      }
    }

}
</script>

<style scoped>

.my-class /deep/ .dropdown-menu {
  max-height: 120px;
  overflow-y: auto;
}
.modalDialog {
    position: fixed;
    font-family: Arial, Helvetica, sans-serif;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    background: rgba(0, 0, 0, 0.8);
    z-index: 99999;
    opacity:0;
    -webkit-transition: opacity 400ms ease-in;
    -moz-transition: opacity 400ms ease-in;
    transition: opacity 400ms ease-in;
    pointer-events: none;
}
.modalDialog:target {
    opacity:1;
    pointer-events: auto;
}
.modalDialog > div {
    width: 400px;
    position: relative;
    margin: 10% auto;
    padding: 5px 20px 13px 20px;
    border-radius: 10px;
    background: #fff;
    background: -moz-linear-gradient(#fff, #999);
    background: -webkit-linear-gradient(#fff, #999);
    background: -o-linear-gradient(#fff, #999);
    height: 300px;
}
.close {
    background: #606061;
    color: #FFFFFF;
    line-height: 25px;
    position: absolute;
    right: -12px;
    text-align: center;
    top: -10px;
    width: 24px;
    text-decoration: none;
    font-weight: bold;
    -webkit-border-radius: 12px;
    -moz-border-radius: 12px;
    border-radius: 12px;
    -moz-box-shadow: 1px 1px 3px #000;
    -webkit-box-shadow: 1px 1px 3px #000;
    box-shadow: 1px 1px 3px #000;
}
.close:hover {
    background: #080710;
}
.custom-select {
  width: 200px;
  overflow-x: scroll;
  border-radius: 10px;
  padding: 5px;
  border-color: #080710;
}
.table-container {
  left: 670px;
  position: fixed;
  top:180px;
  height: 350px;
  width: 500px;
  overflow-y: scroll;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.1), 0px 10px 20px rgba(0, 0, 0, 0.05), 0px 20px 20px rgba(0, 0, 0, 0.05), 0px 30px 20px rgba(0, 0, 0, 0.05);
}
table {
  font-family: 'Arial';
  border-collapse: collapse;
  border: 1px solid #eee;
}
table tr:hover {
  background: #f4f4f4;
}
table tr:hover td {
  color: #555;

}
table th {
  position: sticky;
  top: 0;
}
table th, table td {
  color: #999;
  border: 1px solid #eee;
  padding: 12px 35px;
  border-collapse: collapse;
}
table th {
  background: #080710;
  color: #fff;
  text-transform: uppercase;
  font-size: 12px;
}
.field-table {
  width:100px
}
.value-table {
  width: 400px;
}
.content-title {
  margin-left: 110px;
  margin-top: 100px;
  color: #080710;
}
.content-btn {
  top:550px;
  width:104px;
  left: 820px;
  position: fixed;
  background: #080710 !important;
}
.share-btn {
  position: fixed;  
  top:60px;
  left: 1400px;
  background: #080710 !important;

}
.att-content-btn {
  top:550px;
  left: 950px;
  position: fixed;
  background: #080710 !important;
}
.lds-ellipsis {
  display: inline-block;
  position: relative;
  width: 80px;
  height: 20px;
}
.lds-ellipsis div {
  position: absolute;
  top: 10px;
  width: 13px;
  height: 13px;
  border-radius: 50%;
  background: #080710;
  animation-timing-function: cubic-bezier(0, 1, 1, 0);
}
.lds-ellipsis div:nth-child(1) {
  left: 8px;
  animation: lds-ellipsis1 0.6s infinite;
}
.lds-ellipsis div:nth-child(2) {
  left: 8px;
  animation: lds-ellipsis2 0.6s infinite;
}
.lds-ellipsis div:nth-child(3) {
  left: 32px;
  animation: lds-ellipsis2 0.6s infinite;
}
.lds-ellipsis div:nth-child(4) {
  left: 56px;
  animation: lds-ellipsis3 0.6s infinite;
}
@keyframes lds-ellipsis1 {
  0% {
    transform: scale(0);
  }
  100% {
    transform: scale(1);
  }
}
@keyframes lds-ellipsis3 {
  0% {
    transform: scale(1);
  }
  100% {
    transform: scale(0);
  }
}
@keyframes lds-ellipsis2 {
  0% {
    transform: translate(0, 0);
  }
  100% {
    transform: translate(24px, 0);
  }
}
.loader {
  margin-top: 680px;
  margin-left: 550px;
}
a, a:hover{
  color: white;
  text-decoration: none;
}
</style>