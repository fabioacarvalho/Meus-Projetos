import Vue from 'vue'
import axios from 'axios'

Vue.use({
    install(Vue) {
        Vue.prototype.$http = axios.create({
            baseURL: 'https://toggleclaassen-default-rtdb.firebaseio.com/',
            apiKey: "AIzaSyDuaJPoR5I3Cy-oGApyTDih2Vv3oBuyB8o",
            authDomain: "toggleclaassen.firebaseapp.com",
            projectId: "toggleclaassen",
            storageBucket: "toggleclaassen.appspot.com",
            messagingSenderId: "857932733130",
            appId: "1:857932733130:web:c71fcf7da4cc6317a77233",
            measurementId: "G-1HQEYLXG3F"
        })
    }
})