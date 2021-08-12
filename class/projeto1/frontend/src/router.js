import Vue from 'vue'
import Router from 'vue-router'

import Home from './components/Home'
import Pomodoro from './components/projetos/Pomodoro'
import Dashboard from './components/projetos/Dashboard'
import Table from './components/Table.vue'


Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
        { path: '/', component: Home },
        { path: '/pomodoro', component: Pomodoro },
        { path: '/dashboard', component: Dashboard },
        { path: '/table', component: Table },
    ]
})