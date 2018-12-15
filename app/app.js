import Vue from 'vue';
import VueRouter from 'vue-router';
import axios from 'axios';
import App from './app.vue';
import test from './components/test.vue';
import 'iview/dist/styles/iview.css';
import { locale } from 'iview'; 
import lang from 'iview/dist/locale/en-US';
locale(lang);

Vue.prototype.$axios = axios;

Vue.use(VueRouter);
// Vue.use(iView, { locale });

const router = new VueRouter({
    routes: [
        { path: '/login', component: test }
    ]
});

new Vue({
    el: '#app',
    router,
    render: h => h(App),
});