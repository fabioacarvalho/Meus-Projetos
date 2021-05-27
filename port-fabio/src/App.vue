<template>
  <div id="app">
    <Header />
    <Capa />
    <Abstract />
  </div>
</template>

<script>
import Header from './components/Header.vue'
import Capa from './components/Capa.vue'
import Abstract from './components/Abstract.vue'

export default {
  name: 'App',
  components: {
    Header,
    Capa,
    Abstract
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
  margin-top: 60px;
}
</style>
