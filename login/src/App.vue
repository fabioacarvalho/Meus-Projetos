<template>
  <div id="app">
    <Header v-if="Auth" />
    <Auth />
  </div>
</template>

<script>
import Header from './components/template/Header.vue'
import Auth from './components/auth/Auth.vue'

export default {
  name: 'App',
  components: {
    Auth,
    Header,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
</style>
