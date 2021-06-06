import Vue from 'vue'
import router from 'vue-router'

import Clientes from './components/Clientes.vue'
import Dashboard from './components/Dashboard.vue'
import Fornecedores from './components/Fornecedores.vue'
import Inicio from './components/Inicio.vue'
import NovoPedido from './components/NovoPedido.vue'
import Obras from './components/Obras.vue'
import PedidosRealizados from './components/PedidosRealizados.vue'
import Usuarios from './components/Usuarios.vue'
import Listas from './components/Listas.vue'


Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [{
        name: 'inicio',
        path: '/',
        component: Inicio
    },{
        name: 'Clientes',
        path: '/clientes',
        component: Clientes
    }]
})