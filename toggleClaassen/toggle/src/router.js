import Vue from 'vue'
import Router from 'vue-router'

import Toggle from './components/Toggle'
import Relatorio from './components/Relatorio'
import Cadastro from './components/Cadastro'
import Dashboard from './components/Dashboard'
import Registro from './components/Registro'

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
        { path: '/', component: Toggle },
        { path: '/relatorio', component: Relatorio },
        { path: '/cadastro', component: Cadastro },
        { path: '/dashboard', component: Dashboard },
        { path: '/registro', component: Registro },
    ]
})