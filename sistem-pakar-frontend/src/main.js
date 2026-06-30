import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // Mengimpor router

// Membuat aplikasi Vue dan menggunakannya dengan router
createApp(App)
  .use(router) // Menambahkan router ke aplikasi
  .mount('#app'); // Me-mount aplikasi di elemen dengan id "app"
