import Vue from 'vue'
import Router from 'vue-router'

import Toggle from './components/Toggle'
import Relatorio from './components/Relatorio'

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
        { path: '/', component: Toggle },
        { path: '/relatorio', component: Relatorio },
    ]
})