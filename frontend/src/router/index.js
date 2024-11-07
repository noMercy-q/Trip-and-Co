import {createRouter, createWebHistory} from 'vue-router'
import MainPage from '../components/main-page'
import AuthForm from "@/components/auth-form.vue";
import store from "@/store";
// import store from "@/store";
const routes = [
  {
    path: '/',
    name: 'Main',
    component: MainPage
  },
  {
    path: '/trips/:id',
    name: 'TripDetail',
    component: MainPage,
    props: true,
  },
  {
    path: '/auth',
    name: 'Auth',
    component: AuthForm,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  const isAuthenticated = store.getters.isAuthenticated;

  if (!isAuthenticated && to.path !== '/auth') {
    next('/auth'); // Перенаправляем на Auth, если токена нет
  } else if (isAuthenticated && to.path === '/auth') {
    next('/main'); // Перенаправляем на Main, если токен есть и пытаемся зайти на Auth
  } else {
    next(); // Разрешаем переход
  }
});

export default router
