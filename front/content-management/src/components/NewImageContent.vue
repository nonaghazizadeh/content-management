<template>
  <div class="new-doc-content">
    <h3 class="mt-3 doc-title">Create image content</h3>
    <b-row class="doc-content-management">
        <b-col>
        <div class="label-container">
            <label for="title">Enter your title</label>
        </div>
        <b-form-input autoComplete="off" id="title" v-model="title"></b-form-input>
        </b-col>
    </b-row>
    <b-row class="doc-file-input mt-3">
        <b-col>
        <div class="label-container">
            <label for="file">Upload your file</label>
        </div>
            <input 
            autoComplete="off"
            class="form-control" 
            type="file" 
            id="file" 
            ref="inputFile"
            accept=".jpeg,.png,.jpg,.eps,.raw,.cr2,.nef,.orf,.sr2,.tif,.tiff,.gif" 
            @change="handleFileUpload( $event )"
            />
        </b-col>
    </b-row>
    <b-row v-for="i in newFields" :key="i" class="mt-3 new-content-info">
    <b-col sm="1" /><b-col sm="1" />
    <b-col sm="3" class="field-title">
        <div class="label-container">
            <label for="field">Enter your field</label>
        </div>
        <b-form-input
        autoComplete="off" 
        id="field"
        v-model="diffrentFields[i]['field']"
        >
        </b-form-input>
    </b-col>
    <b-col sm="6" class="field-text">
        <div class="label-container">
            <label for="value">Enter your value</label>
        </div>
        <b-form-input 
        autoComplete="off"
        id="value"
        v-model="diffrentFields[i]['value']" 
        >
        </b-form-input>
    </b-col>
    </b-row>
    <div class="mt-4 add-field-button">
        <b-button variant="dark" @click="addNewField()" class="add-attribute-btn">
            add attribute
        </b-button>
        <b-button variant="dark" @click="submitDocContent()">
            submit
        </b-button>
    </div>
    <div id="snackbar" :class="[showSuccessToast ? 'show': '']">New image content added!</div>
    <div id="snackbar" :class="[showFailToast ? 'show': '']">{{errorMessage}}</div>

  </div>
</template>

<script>
import Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";
Vue.use(VueAxios, axios);

export default {
    data(){
        return {
            showSuccessToast:false,
            showFailToast:false,
            errorMessage: '',
            diffrentFields: {
                1: {"field": '', "value": ''},
            },
            newFields: 1,
            title: '',
            file: '',
        }
    },
    watch: {
        showSuccessToast(){
         if(this.showSuccessToast)
             setTimeout(() => this.showSuccessToast = false, 3000); 
        },
        showFailToast(){
            if(this.showFailToast)
             setTimeout(() => this.showFailToast = false, 3000);
        }
     },
  methods: {
      handleFileUpload(event){
        this.file = event.target.files[0];
      },
      addNewField(){
          this.newFields = this.newFields + 1;
          this.diffrentFields[this.newFields] = {"field" : '', "value": ''};
      },
      submitDocContent() {
          let formData = new FormData();
          let api = "http://127.0.0.1:8000/content/create/"
          formData.append('file', this.file);
          formData.append('title', this.title);
          formData.append('file_format', "I");
          for (let [key, value] of Object.entries(this.diffrentFields)) {
            console.log(key)
            formData.append(value['field'], value['value'])
          }
          Vue.axios.post(api, formData, {
           headers: {
            'Authorization': "Token " + localStorage.getItem('token')
           }
          })
            .then(response => {
                this.showSuccessToast = true;
                console.log(response.data)
                this.file = '';
                this.$refs.inputFile.value=null;
                this.title = '';
                this.newFields = 1;
                this.diffrentFields= {
                    1: {"field": '', "value": ''},
                }
                console.log(this.title);
                this.$emit("docAdded");
                this.loading = false;

            }).catch((e) => {
                let obj = e.response.data
                this.errorMessage = obj[Object.keys(obj)[0]][0];
                console.log(this.errorMessage)
                this.showFailToast = true;
                console.error(obj[Object.keys(obj)[0]][0]);
                this.file = '';
                this.$refs.inputFile.value=null;
                this.title = '';
                this.newFields = 1;
                this.diffrentFields= {
                    1: {"field": '', "value": ''},
                }
                this.loading = false;
            })
      }
  }
}
</script>

<style scoped>
.doc-title {
    margin-left: 190px;
}
.doc-content-management{
    margin-left: 190px !important;
    margin-top: 50px !important;
}
.doc-file-input {
    margin-left: 190px !important;
}
.new-doc-content {
    width: 80%;
    height: 100%
}
.add-field-button {
    text-align: right;
}
.delete-field-button {
    margin-left: -20px !important;
}
.field-title {
    margin-right: 25px !important;
    margin-left: 50px !important;
}
.submit-button {
    position: relative;
}
input {
    border-radius: 30px;
    outline: none !important;
}
input:focus {
    box-shadow: inset 0 -1px 0 #ddd;
    outline: none !important;
    border:1px solid #ccc !important;
}
button:focus, button:hover, button:active {
    outline: none !important;
}
.label-container {
    text-align: left;
    margin-left: 8px;
    margin-bottom: 3px;
}
.add-attribute-btn {
    margin-right: 5px;
}

#snackbar {
  visibility: hidden;
  min-width: 250px;
  margin-left: -125px;
  background-color: #333;
  color: #fff;
  text-align: center;
  border-radius: 2px;
  padding: 16px;
  position: fixed;
  z-index: 1;
  left: 50%;
  bottom: 30px;
  font-size: 17px;
}

#snackbar.show {
  visibility: visible;
  -webkit-animation: fadein 0.5s, fadeout 0.5s 2.5s;
  animation: fadein 0.5s, fadeout 0.5s 2.5s;
}

@-webkit-keyframes fadein {
  from {bottom: 0; opacity: 0;} 
  to {bottom: 30px; opacity: 1;}
}

@keyframes fadein {
  from {bottom: 0; opacity: 0;}
  to {bottom: 30px; opacity: 1;}
}

@-webkit-keyframes fadeout {
  from {bottom: 30px; opacity: 1;} 
  to {bottom: 0; opacity: 0;}
}

@keyframes fadeout {
  from {bottom: 30px; opacity: 1;}
  to {bottom: 0; opacity: 0;}
}
</style>