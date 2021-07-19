import Vue from 'vue';
import Router from 'vue-router';
import Ping from '../components/Salario.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Salario',
      component: Ping,
    },
  ],
});
