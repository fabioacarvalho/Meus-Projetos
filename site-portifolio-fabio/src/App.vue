<template>
  <div id="app">
    <Header id="header" />
    <Sobre id="sobre" />
  </div>
</template>

<script>
import Header from './components/Header.vue'
import Sobre from './components/Sobre.vue'

export default {
  name: 'App',
  components: { Header, Sobre }
}
</script>

<style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    
    display: grid;
    grid-auto-columns: 100%;
    grid-auto-rows: 1fr 1fr;
    grid-template-areas: 
      "header"
      "sobre"
    
    ;
  }

  #header {
    height: 100%;
    grid-area: header;
  }

  #sobre {
    height: 100%;
    grid-area: sobre;
  }
  
  @media(max-width: 700px) {
        #app {
          display: grid;
          grid-auto-columns: 100%;
          grid-auto-rows: 1fr 1fr;
          grid-template-areas: 
            "header"
            "sobre"
    
    ;
        }
    }


</style>
