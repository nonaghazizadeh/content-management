<template>
<div class="login-container">
    <div class="background">
        <div class="shape"></div>
        <div class="shape"></div>
    </div>
    <form>
        <h3>Register</h3>

        <label for="username">Username</label>
        <input autoComplete="off" v-model="username" type="text" placeholder="Email or Phone" id="username">

        <label for="password">Password</label>
        <input v-model="password" type="password" placeholder="Password" id="password">
        <p v-if="errorMessage != ''" class="error-message">{{errorMessage}}</p>
        <p :class="[errorMessage ? 'register-link-container-error':'register-link-container']"><span>Have an account? </span><span><router-link to="/login">Login</router-link></span></p>
        <button v-if="!loading" @click="register()" :disabled="loading">
            Register
        </button>
        <button v-if="loading">
            <div class="lds-ellipsis"><div></div><div></div><div></div><div></div></div>   
        </button>
    </form>
</div>

</template>

<script>
import Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";
Vue.use(VueAxios, axios);

export default {
  name: 'RegisterComp',
  data(){
      return{
          username: '',
          password: '',
          loading: false,
          errorMessage: '',
      }
  },
  methods: {
      register(){
            this.loading = true;
            let api = "http://127.0.0.1:8000/user/register/";
            const data = {
                "username" : this.username,
                "password": this.password,
            };
            Vue.axios.post(api, data)
            .then(response => {
                localStorage.removeItem('token');
                localStorage.setItem('token', response.data.token)
                this.loading = false;
                this.$router.replace("/contents");
            }).catch((e) => {
                let obj = e.response.data
                this.errorMessage = obj[Object.keys(obj)[0]][0];
                if (this.errorMessage =="A user with that username already exists.") {
                  this.errorMessage = "Username already exists."
                }
                this.loading = false;
                console.log(this.errorMessage)
            })
        }
  }
}
</script>

<style scoped>
*,
*:before,
*:after{
    padding: 0;
    margin: 0;
    box-sizing: border-box;
}
.error-message{
  color: #fff;
  margin-top: 15px;
  margin-bottom: -20x;
  color: #961540;
}
.login-container{
  background:#080710;
  position:absolute;
  top:0px;
  right:0px;
  bottom:0px;
  left:0px;
}
.background{
    width: 430px;
    height: 520px;
    position: absolute;
    transform: translate(-50%,-50%);
    left: 50%;
    top: 50%;
    background-color: #080710 !important;
}
.background .shape{
    height: 200px;
    width: 200px;
    position: absolute;
    border-radius: 50%;
}
.shape:first-child{
    background: linear-gradient(
        to right,
        #1845ad,
        #b8dffc
    );
    left: -80px;
    top: -80px;
}
.shape:last-child{
    background: linear-gradient(
        to right,
        #961540,
        #fcb8c9
    );
    right: -80px;
    bottom: -80px;
}
form{
    height: 520px;
    width: 400px;
    background-color: rgba(255,255,255,0.13);
    position: absolute;
    transform: translate(-50%,-50%);
    top: 50%;
    left: 50%;
    border-radius: 10px;
    backdrop-filter: blur(10px);
    border: 2px solid rgba(255,255,255,0.1);
    box-shadow: 0 0 40px rgba(8,7,16,0.6);
    padding: 50px 35px;
}
form *{
    font-family: 'Poppins',sans-serif;
    color: #ffffff;
    letter-spacing: 0.5px;
    outline: none;
    border: none;
}
form h3{
    font-size: 32px;
    font-weight: 500;
    line-height: 42px;
    text-align: center;
}

label{
    display: block;
    margin-top: 30px;
    font-size: 16px;
    font-weight: 500;
}
input{
    display: block;
    height: 50px;
    width: 100%;
    background-color: rgba(255,255,255,0.07);
    border-radius: 3px;
    padding: 0 10px;
    margin-top: 8px;
    font-size: 14px;
    font-weight: 300;
}
::placeholder{
    color: #e5e5e5;
}
button{
    margin-top: 20px;
    width: 100%;
    background-color: #ffffff;
    color: #080710;
    padding: 15px 0;
    font-size: 18px;
    font-weight: 600;
    border-radius: 5px;
    cursor: pointer;
}
.social{
  margin-top: 30px;
  display: flex;
}
.register-link-container-error{
    margin-top: 10px;
}
.register-link-container {
  margin-top: 40px;
}
a:hover{
  color: white;
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
</style>
