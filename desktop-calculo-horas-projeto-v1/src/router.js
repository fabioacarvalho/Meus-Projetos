import Vue from 'vue'
import router from 'vue-router'

import Clientes from './components/Clientes.vue'
import Dashboard from './components/Dashboard.vue'
import Inicio from './components/Inicio.vue'
import Obras from './components/Obras.vue'
import Usuarios from './components/Usuarios.vue'
import Dados from './components/Dados.vue'


Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [{
        name: 'dados',
        path: '/',
        component: Dados
        },{
        name: 'Clientes',
        path: '/clientes',
        component: Clientes
    }]
})