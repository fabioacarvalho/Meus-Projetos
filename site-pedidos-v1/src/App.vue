<template>
  <div id="app">
    <Nav/>
    <Clientes />
    <Dashboard />
    <Fornecedores />
    <Inicio/>
    <NovoPedido/>
    <Obras/>
    <PedidosRealizados/>
    <Usuarios/>
    <Listas/>
    <Header/>

    <Footer/>
  </div>
</template>

<script>
import Clientes from './components/Clientes.vue'
import Dashboard from './components/Dashboard.vue'
import Fornecedores from './components/Fornecedores.vue'
import Inicio from './components/Inicio.vue'
import NovoPedido from './components/NovoPedido.vue'
import Obras from './components/Obras.vue'
import PedidosRealizados from './components/PedidosRealizados.vue'
import Usuarios from './components/Usuarios.vue'
import Listas from './components/Listas.vue'
import Header from './components/template/Header.vue'
import Nav from './components/template/Nav.vue'
import Footer from './components/template/Footer.vue'

export default {
  name: 'App',
  components: { Clientes, Dashboard, Fornecedores, Inicio, NovoPedido, Obras, PedidosRealizados, Usuarios, Listas, Header, Nav, Footer },
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
