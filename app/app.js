import Vue from 'vue';
import VueRouter from 'vue-router';
import axios from 'axios';
import App from './app.vue';
import test from './components/test.vue';
import login from './components/login.vue';
import home from './components/home.vue';
import 'iview/dist/styles/iview.css';
import { locale } from 'iview';
import lang from 'iview/dist/locale/en-US';
locale(lang);

Vue.prototype.$axios = axios;

Vue.use(VueRouter);

const router = new VueRouter({
    routes: [
        { path: '/', component: App },
        { path: '/test', component: test },
        { path: '/login', component: login },
        { path: '/home', component: home }
    ]
});

new Vue({
    el: '#app',
    router,
    render: h => h(App),
});