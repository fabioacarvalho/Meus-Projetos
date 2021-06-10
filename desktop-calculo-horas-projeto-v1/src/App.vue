<template>
  <div id="app">
    <Nav/>
    <Clientes />
    <Dados />
    
  </div>
</template>

<script>
import Clientes from './components/Clientes.vue'
import Dashboard from './components/Dashboard.vue'
import Obras from './components/Obras.vue'
import Usuarios from './components/Usuarios.vue'
import Dados from './components/Dados.vue'
import Header from './components/template/Header.vue'
import Nav from './components/template/Nav.vue'
import Footer from './components/template/Footer.vue'

export default {
  name: 'App',
  components: { Clientes, Dashboard, Obras, Usuarios, Dados, Header, Nav, Footer },
  /* created() {
        this.$http.post('pedidos.json', {
            nome: 'Maria',
            email: 'maria@gmail.com'
        }).then(res => console.log(res))
    } */

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0;
}
</style>
