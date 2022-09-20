<template>
  <div>
    <div class="sidebar">
      <div class="logo-details">
        <span class="logo-name">Content Management</span>
        <span class="logo-icon" @click="logout()">
          <font-awesome-icon icon="fa-solid fa-arrow-right-from-bracket" class="sidebar-icon"/>
        </span>
      </div>
      <ul class="nav-links">
        <li :class="[showDocMenu ? 'showMenu': '']">
          <div class="icon-link">
            <font-awesome-icon icon="fa-solid fa-angle-up" class="sidebar-icon-doc"/>
            <a class="sidebar-item-icon-doc">
              <span>
                <font-awesome-icon icon="fa-solid fa-file" class="sidebar-icon-doc"/>
              </span>
              <span class="link-name">Document</span>
            </a>
            <font-awesome-icon v-if="showDocMenu" icon="fa-solid fa-angle-up" class="arrow" @click="toggleDocSubMenu()"/>
            <font-awesome-icon v-if="!showDocMenu" icon="fa-solid fa-angle-down" class="arrow" @click="toggleDocSubMenu()"/>
          </div>
          <ul class="sub-menu">
            <li><a class="link-name" href="#">Document</a></li>
            <li v-for="content in docContents" :key="content.id" >
              <a @click="openSelectedDocContent(content.id)">{{content.title}}</a>
            </li>
            <li>
              <a>
              <span>
                  <font-awesome-icon icon="fa-solid fa-plus" class="sidebar-icon-add"/>
              </span>
              <span class="add-text" @click="newDoc()">
                add new content
              </span>
              </a>
            </li>
          </ul>
        </li>
        <li :class="[showAudioMenu ? 'showMenu': '']">
          <div class="icon-link">
            <font-awesome-icon icon="fa-solid fa-angle-up" class="sidebar-icon-audio"/>
            <a class="sidebar-item-icon-audio">
              <span>
                <font-awesome-icon icon="fa-solid fa-volume-high" class="sidebar-icon-audio"/>
              </span>              
              <span class="link-name">Audio</span>
            </a>
            <font-awesome-icon v-if="showAudioMenu" icon="fa-solid fa-angle-up" class="arrow" @click="toggleAudioSubMenu()"/>
            <font-awesome-icon v-if="!showAudioMenu" icon="fa-solid fa-angle-down" class="arrow" @click="toggleAudioSubMenu()"/>
          </div>
          <ul class="sub-menu">
            <li><a class="link-name" href="#">Audio</a></li>
            <li v-for="content in audioContents" :key="content.id" >
              <a @click="openSelectedAudioContent(content.id)">{{content.title}}</a>
            </li>
            <li>
              <a>
              <span>
                  <font-awesome-icon icon="fa-solid fa-plus" class="sidebar-icon-add"/>
              </span>
              <span class="add-text" @click="newAudio()">
                add new content
              </span>
              </a>
            </li>
          </ul>
        </li>
        <li :class="[showVideoMenu ? 'showMenu': '']">
          <div class="icon-link">
          <font-awesome-icon icon="fa-solid fa-video" class="sidebar-icon-video"/>
            <a class="sidebar-item-icon-video">
              <span>
                <font-awesome-icon icon="fa-solid fa-video" class="sidebar-icon-video"/>
              </span>
              
              <span class="link-name">Video</span>
            </a>
            <font-awesome-icon v-if="showVideoMenu" icon="fa-solid fa-angle-up" class="arrow" @click="toggleVideoSubMenu()"/>
            <font-awesome-icon v-if="!showVideoMenu" icon="fa-solid fa-angle-down" class="arrow" @click="toggleVideoSubMenu()"/>
          </div>
          <ul class="sub-menu">
            <li><a class="link-name" href="#">Video</a></li>
            <li v-for="content in videoContents" :key="content.id" >
              <a @click="openSelectedVideoContent(content.id)">{{content.title}}</a>
            </li>
            <li>
              <a>
              <span>
                  <font-awesome-icon icon="fa-solid fa-plus" class="sidebar-icon-add"/>
              </span>
              <span class="add-text" @click="newVideo()">
                add new content
              </span>
              </a>
            </li>
          </ul>
        </li>
        <li :class="[showImageMenu ? 'showMenu': '']">
          <div class="icon-link">
            <font-awesome-icon icon="fa-solid fa-angle-up" class="sidebar-icon-doc"/>
            <a class="sidebar-item-icon-image">
              <span>
                <font-awesome-icon icon="fa-solid fa-image" class="sidebar-icon-doc"/>
              </span>
              <span class="link-name">Image</span>
            </a>
            <font-awesome-icon v-if="showImageMenu" icon="fa-solid fa-angle-up" class="arrow" @click="toggleImageSubMenu()"/>
            <font-awesome-icon v-if="!showImageMenu" icon="fa-solid fa-angle-down" class="arrow" @click="toggleImageSubMenu()"/>
          </div>
          <ul class="sub-menu">
            <li><a class="link-name" href="#">Image</a></li>
            <li v-for="content in imageContents" :key="content.id" >
              <a @click="openSelectedImageContent(content.id)">{{content.title}}</a>
            </li>
            <li>
              <a>
              <span>
                  <font-awesome-icon icon="fa-solid fa-plus" class="sidebar-icon-add"/>
              </span>
              <span class="add-text" @click="newImage()">
                add new content
              </span>
              </a>
            </li>
          </ul>
        </li>
      </ul>
    </div>
    <section class="home-section">
      <div class="home-content">
        <new-doc-content 
        v-if="showNewDocPage" 
        @docAdded="refreshMenu()"
        />
        <doc-contet 
        v-if="showDocContent" 
        :title="docTitle" 
        :loading="docLoading"
        :extra="docExtra"
        :file="docFile"
        :attach="docAttachFile"
        :id="docId"
        />
        <new-audio-content
        v-if="showNewAudioPage" 
        @docAdded="refreshMenu()"
        />
        <audio-content
        v-if="showAudioContent"
        :title="audioTitle"
        :loading="audioLoading"
        :extra="audioExtra"
        :file="audioFile"
        :attach="audioAttachFile"
        :id="audioId"
        />
        <new-video-content
        v-if="showNewVideoPage" 
        @docAdded="refreshMenu()"
        />
        <video-content
        v-if="showVideoContent"
        :title="videoTitle"
        :loading="videoLoading"
        :extra="videoExtra"
        :file="videoFile"
        :attach="videoAttachFile"
        :id="videoId"
        />
        <new-image-content
        v-if="showNewImagePage" 
        @docAdded="refreshMenu()"
        />
        <image-content
        v-if="showImageContent"
        :title="imageTitle"
        :loading="imageLoading"
        :extra="imageExtra"
        :file="imageFile"
        :attach="imageAttachFile"
        :id="imageId"
        />
      </div>
    </section>
  </div>
</template>

<script>
import Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";
Vue.use(VueAxios, axios);

import NewDocContent from './NewDocContent.vue'
import DocContet from './DocContent.vue'
import NewAudioContent from './NewAudioContent.vue';
import AudioContent from './AudioContent.vue';
import NewVideoContent from './NewVideoContent.vue';
import VideoContent from './VideoContent.vue';
import NewImageContent from './NewImageContent.vue';
import ImageContent from './ImageContent.vue';

export default {
  components: {
    NewDocContent,
    DocContet,
    NewAudioContent,
    AudioContent,
    NewVideoContent,
    VideoContent,
    NewImageContent,
    ImageContent,
  },
  created() {
    this.getAllContents();
  },
  data(){
    return {
      showDocMenu: false,
      showAudioMenu: false,
      showVideoMenu:false,
      showImageMenu: false,

      contents : [],
      loading:false,

      showNewDocPage: false,
      showDocContent: false,
      showNewAudioPage: false,
      showAudioContent: false,
      showNewVideoPage: false,
      showVideoContent: false,
      showNewImagePage:false,
      showImageContent:false,

      docLoading: false,
      docTitle: '',
      docExtra: {},
      docFile: '',
      docAttachFile : '',
      docId: '',

      audioLoading: false,
      audioTitle: '',
      audioExtra: {},
      audioFile: '',
      audioAttachFile : '',
      audioId: '',

      videoLoading: false,
      videoTitle: '',
      videoExtra: {},
      videoFile: '',
      videoAttachFile : '',
      videoId: '',

      imageLoading: false,
      imageTitle: '',
      imageExtra: {},
      imageFile: '',
      imageAttachFile : '',
      imageId: '',
    }
  },
  computed: {
    docContents() {
      return this.contents.filter(item => item.file_format === 'D')
    },
    audioContents() {
      return this.contents.filter(item => item.file_format === 'A')
    },
    videoContents() {
      return this.contents.filter(item => item.file_format === 'V')
    },
    imageContents() {
      return this.contents.filter(item => item.file_format === 'I')
    },
  },
  methods: {
    toggleDocSubMenu(){
      this.showDocMenu = ~this.showDocMenu;
    },
    toggleAudioSubMenu(){
      this.showAudioMenu = ~this.showAudioMenu;
    },
    toggleVideoSubMenu(){
      this.showVideoMenu = ~this.showVideoMenu;
    },
    toggleImageSubMenu(){
      this.showImageMenu = ~this.showImageMenu;
    },
    newDoc(){
      this.showNewDocPage = true;
      this.showDocContent = false;
      this.showNewAudioPage = false;
      this.showAudioContent = false;
      this.showNewVideoPage = false;
      this.showVideoContent = false;
      this.showImageContent = false;
      this.showNewImagePage = false;
    },
    newAudio(){
      this.showNewAudioPage = true;
      this.showNewDocPage = false;
      this.showDocContent = false;
      this.showAudioContent = false;
      this.showNewVideoPage = false;
      this.showVideoContent = false;
      this.showImageContent = false;
      this.showNewImagePage = false;
    },
    newVideo() {
      this.showNewVideoPage = true;
      this.showNewAudioPage = false;
      this.showNewDocPage = false;
      this.showDocContent = false;
      this.showAudioContent = false;
      this.showVideoContent = false;
      this.showImageContent = false;
      this.showNewImagePage = false;
    },
    newImage(){
      this.showNewImagePage = true;
      this.showNewVideoPage = false;
      this.showNewAudioPage = false;
      this.showNewDocPage = false;
      this.showDocContent = false;
      this.showAudioContent = false;
      this.showVideoContent = false;
      this.showImageContent = false;
    },
    refreshMenu(){
      this.getAllContents();
    },
    logout(){
      console.log(localStorage.getItem('token'));
      localStorage.removeItem('token');
      console.log(localStorage.getItem('token'));
      this.$router.push('/login');
    },
    getAllContents(){
      this.loading = true;
      let api = "http://127.0.0.1:8000/content/list/";
      Vue.axios.get(api, {
        headers: {
          'Authorization': "Token " + localStorage.getItem('token')
        }
      })
      .then(response => {
          this.contents = response.data;
          this.loading = false;
      }) 
    },
    openSelectedDocContent(id) {
      this.showDocContent = true;
      this.showNewDocPage = false;
      this.showNewAudioPage = false;
      this.showAudioContent = false;
      this.showVideoContent = false;
      this.showNewVideoPage = false;
      this.showImageContent = false;
      this.showNewImagePage = false;

      this.docLoading = true;
      let api = "http://127.0.0.1:8000/content/retrieve/"+id;
      Vue.axios.get(api, {
        headers: {
          'Authorization': "Token " + localStorage.getItem('token')
        }
      })
      .then(response => {
        this.docTitle = response.data.title;
        this.docFile = response.data.file;
        this.docAttachFile = response.data.attach_file;
        this.docExtra = response.data.extra;
        this.docId = response.data.id;
        this.docLoading = false;
      }) 
    },
    openSelectedAudioContent(id) {
      this.showAudioContent = true;
      this.showNewAudioPage = false;
      this.showDocContent = false;
      this.showNewDocPage = false;
      this.showVideoContent = false;
      this.showNewVideoPage = false;
      this.showImageContent = false;
      this.showNewImagePage = false;

      this.audioLoading = true;
      let api = "http://127.0.0.1:8000/content/retrieve/"+id;
      Vue.axios.get(api, {
        headers: {
          'Authorization': "Token " + localStorage.getItem('token')
        }
      })
      .then(response => {
        this.audioTitle = response.data.title;
        this.audioFile = response.data.file;
        this.audioAttachFile = response.data.attach_file;
        this.audioExtra = response.data.extra;
        this.audioId = response.data.id;
        this.audioLoading = false;
      }) 
    },
    openSelectedVideoContent(id) {
      this.showVideoContent = true;
      this.showAudioContent = false;
      this.showNewAudioPage = false;
      this.showDocContent = false;
      this.showNewDocPage = false;
      this.showNewVideoPage = false;
      this.showImageContent = false;
      this.showNewImagePage = false;

      this.videoLoading = true;
      let api = "http://127.0.0.1:8000/content/retrieve/"+id;
      Vue.axios.get(api, {
        headers: {
          'Authorization': "Token " + localStorage.getItem('token')
        }
      })
      .then(response => {
        this.videoTitle = response.data.title;
        this.videoFile = response.data.file;
        this.videoAttachFile = response.data.attach_file;
        this.videoExtra = response.data.extra;
        this.videoId = response.data.id;
        this.videoLoading = false;
      }) 
    },
    openSelectedImageContent(id) {
      this.showImageContent = true;
      this.showAudioContent = false;
      this.showNewAudioPage = false;
      this.showDocContent = false;
      this.showNewDocPage = false;
      this.showVideoContent = false;
      this.showNewVideoPage = false;
      this.showNewImagePage = false;

      this.imageLoading = true;
      let api = "http://127.0.0.1:8000/content/retrieve/"+id;
      Vue.axios.get(api, {
        headers: {
          'Authorization': "Token " + localStorage.getItem('token')
        }
      })
      .then(response => {
        this.imageTitle = response.data.title;
        this.imageFile = response.data.file;
        this.imageAttachFile = response.data.attach_file;
        this.imageExtra = response.data.extra;
        this.imageId = response.data.id;
        this.imageLoading = false;
      }) 
    },
    }
}
</script>

<style scoped>
.contents-container {
  position:absolute;
  top:0px;
  right:0px;
  bottom:0px;
  left:0px;
}
.contents-sidebar{
  background-color: #080710 ;
  height: 100%;
  overflow-y: scroll;
}
.content-container{
  background-color: rgba(255,255,255,0.13); ;
  height: 100%;
  overflow-y: scroll;
}
.content-title{
  height: 80px;
  margin-top: 10px;
  color: white;
  text-align: left;
  border-radius: 10px;
  backdrop-filter: blur(10px);
  border-bottom: 2px solid rgba(255,255,255,0.1);
  box-shadow: 0 0 40px rgba(8,7,16,0.6);
  padding: 8px;
  background-color: rgba(255,255,255,0.13);
}
.category-title {
  color: #961540;
  font-size: 20px;
  padding-top: 10px;
}
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap");
.sidebar {
  background: #080710;
  width: 350px;
  position:absolute;
  top:0px;
  right:0px;
  bottom:0px;
  left:0px;
  height: 100%;
  overflow-y: scroll;
}
.sidebar .logo-details {
  height: 80px;
  width: 100%;
  min-width: 78px;
  display: flex;
  align-items: center;
  font-size: 32px;
  text-align: center;
  line-height: 50px;
}
.sidebar .logo-details i {
  font-size: 30px;
  color: #fff;
  height: 50px;
  min-width: 78px;
  text-align: center;
  line-height: 50px;
}
.sidebar .logo-details .logo-name {
  font-size: 22px;
  color: #fff;
  font-weight: 600;
  transition: 0.3s ease;
  transition-delay: 0.1s;
  margin-left: 30px;
}
.sidebar .nav-links {
  height: 100%;
  margin-left: -70px;
  overflow: auto;
}
.arrow{
  margin-right: 30px;
  color: white  !important;
}
.sidebar .nav-links::-webkit-scrollbar {
  display: none;
}
.sidebar .nav-links li {
  position: relative;
  list-style: none;
  transition: all 0.4s ease;
}
.sidebar .nav-links li:hover {
  background: #1b1b31;
}
.sidebar .nav-links li:hover .sub-menu.blank {
  top: 50%;
  transform: translateY(-50%);
}
.sidebar .nav-links li.showMenu i.arrow {
  transform: rotate(-180deg);
}
.sidebar .nav-links li.showMenu .sub-menu {
  display: block;
}
.sidebar .nav-links li .icon-link {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.sidebar .nav-links li i {
  height: 50px;
  min-width: 78px;
  text-align: center;
  line-height: 50px;
  color: #fff;
  font-size: 20px;
  cursor: pointer;
  transition: all 0.3s ease;
}
.sidebar .nav-links li a {
  display: flex;
  align-items: center;
  text-decoration: none;
}
.sidebar .nav-links li a .link-name {
  font-size: 20px;
  font-weight: 400;
  color: #fff;
  transition: all 0.4s ease;
}
.sidebar .nav-links li .sub-menu {
  padding: 6px 6px 14px 80px;
  display: none;
}
.sidebar .nav-links li .sub-menu.blank {
  opacity: 0;
  pointer-events: none;
  padding: 3px 20px 6px 16px;
}
.sidebar .nav-links li .sub-menu a {
  color: #fff;
  font-size: 18px;
  padding: 5px 0;
  white-space: nwrap;
  opacity: 0.6;
  transition: all 0.3 ease;
}
.sidebar .nav-links li .sub-menu a:hover {
  opacity: 1;
}
.sidebar .nav-links li .sub-menu .link-name {
  display: none;
}
.home-section {
  position: absolute;
  background: 	#dddee0;
  height: 100vh;
  left: 350px;
  top: 0px;
  width: calc(100% - 350px);
  transition: all 0.5s ease;
  overflow-y: scroll;
}
.home-section .home-content {
  height: 60px;
  display: flex;
  align-items: center;
}
.home-section .home-content .bx-menu {
  color: #11101d;
  font-size: 35px;
  margin: 0 35px;
  cursor: pointer;
}
.home-section .home-content .text {
  color: #11101d;
  font-size: 26px;
  font-weight: 600;
}
a:hover {
  cursor: pointer;
}
.arrow:hover {
  cursor: pointer;
}
.sidebar-icon-doc {
  color: white;
  margin-right: 30px;
}
.sidebar-item-icon-doc {
  margin-left: -100px;
  margin-top: 10px;
  margin-bottom: 10px;
}
.sidebar-icon-audio {
  color: white;
  margin-right: 27px;
}
.sidebar-item-icon-audio {
  margin-left: -140px;
  margin-top: 10px;
  margin-bottom: 10px;
}
.sidebar-icon-video {
  color: white;
  margin-right: 28px;
}
.sidebar-item-icon-video {
  margin-left: -150px;
  margin-top: 10px;
  margin-bottom: 10px;
}
.sidebar-item-icon-image{
    margin-left: -145px;
  margin-top: 10px;
  margin-bottom: 10px;
}
.sidebar-icon-add {
  color: white; 
  opacity: 1;
  cursor: pointer; 
}
.add-sidebar-section{
  text-align: left;
  margin-top: 10px;
}
.add-text {
  margin-left: 10px;
  color: #fff; 
  opacity: 1;
  cursor: pointer; 
}
.add-sidebar-section:hover {
  opacity: 1; 
}
.logo-icon {
  margin-left: 40px;
  font-size: 20px;
}
.sidebar-icon {
  color: white;
  margin-left: 14px;
}
.sidebar-icon:hover {
  cursor: pointer;
}
</style>