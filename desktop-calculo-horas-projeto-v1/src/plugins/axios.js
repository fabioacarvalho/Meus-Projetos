import Vue from 'vue'
import axios from 'axios'

Vue.use({
    install(Vue) {
        /* Vue.prototype.$http = axios.create({
            baseURL: 'https://pedidos-fabio-default-rtdb.firebaseio.com/'
        }), */
        Vue.prototype.$http = axios.create({
            baseURL: 'https://cadastro-clientes-obras-default-rtdb.firebaseio.com/'
        }),    
        Vue.prototype.$apitempodosporjetos = axios.create({
            baseURL: 'https://tempodosprojetos-default-rtdb.firebaseio.com/'
        })    

    }
})