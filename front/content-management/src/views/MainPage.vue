<template>
  <div>
  </div>
</template>

<script>
export default {
  name: 'MainPage',

  created(){
      console.log(localStorage.getItem('token'))
      if (localStorage.getItem('token') == null){
        this.$router.push('/login');
      }
      else {
        this.$router.push('/contents');
      }
  }
}
</script>