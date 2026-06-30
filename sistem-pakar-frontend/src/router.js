import { createRouter, createWebHistory } from 'vue-router';

// Mengimpor komponen dengan jalur relatif
import LandingPage from '@/components/LandingPage.vue'; 
import DiagnosaForm from '@/components/DiagnosaForm.vue'; 
import DaftarPenyakit from '@/components/DaftarPenyakit.vue'; 

// Konfigurasi rute
const routes = [
  {
    path: '/',
    name: 'LandingPage',
    component: LandingPage,  // Mengarah ke komponen LandingPage
  },
  {
    path: '/diagnosa',
    name: 'DiagnosaForm',
    component: DiagnosaForm,  // Mengarah ke komponen DiagnosaForm
  },
  {
    path: '/daftar-penyakit',
    name: 'DaftarPenyakit',
    component: DaftarPenyakit,  // Mengarah ke komponen DaftarPenyakit
  },
];

// Membuat instance router
const router = createRouter({
  history: createWebHistory('/'),
  routes,
});

export default router;
