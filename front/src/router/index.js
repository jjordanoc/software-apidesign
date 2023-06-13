import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import LoginView from '../views/LoginView.vue';
// import auth from '../logic/auth';

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,

  },
  {
    path: '/login',
    name: 'Log in',
    component: LoginView,
    meta: { requiresAuth: false }, // Update the meta property
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

// Add a global navigation guard
// router.beforeEach((to, from, next) => {
//   if (to.meta.requiresAuth && !auth.isAuthenticated()) {
//     // Redirect to the login page if authentication is required but user is not authenticated
//     next({ name: 'Log in' });
//   } else {
//     // Continue to the next route
//     next();
//   }
// });

export default router;
