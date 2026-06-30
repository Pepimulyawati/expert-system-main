<template>
    <div id="landing-page">
    <!-- Menambahkan Navbar -->
    <AppNavbar />

    <!-- Header Section -->
    <header id="header" class="header">
      <title>Sistem Pakar</title>
      <div class="container">
        <h1 class="title">Selamat Datang di Sistem Pakar Diagnosis Penyakit Tanaman Padi</h1>
        <p class="subtitle">Solusi cerdas untuk membantu keputusan Anda</p>
        <button class="btn" @click="startExpertSystem">Mulai Analisis</button>
      </div>
    </header>

    <!-- About Section -->
    <section id="about" class="about">
      <div class="container">
        <h2>Tentang Sistem Pakar</h2>
        <p>
          Sistem pakar ini dirancang untuk memenuhi tugas akhir mata kuliah sistem pakar.
        </p>
      </div>
    </section>

    <!-- Features Section -->
    <section id="features" class="features">
      <div class="container">
        <h2>Fitur Utama</h2>
        <div class="feature-items">
          <div class="feature">
            <h3>Analisis Cepat</h3>
            <p>Hasil analisis ditampilkan dalam hitungan detik.</p>
          </div>
          <div class="feature">
            <h3>Kecerdasan Buatan</h3>
            <p>Memanfaatkan teknologi AI untuk hasil lebih akurat.</p>
          </div>
          <div class="feature">
            <h3>Data Terpercaya</h3>
            <p>Berbasis data yang dikumpulkan dari sumber terpercaya.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Footer Section -->
    <footer id="footer" class="footer">
      <div class="container">
        <p>&copy; 2024 Sistem Pakar. Oleh Bayyinahtun Dwi Sumatri dan Kumala Dewi</p>
        <p>
          Hubungi kami melalui email: 
          <a href="mailto:bynthdwi@gmail.com" class="email-link" target="_blank">bynthdwi@gmail.com</a>
        </p>
      </div>
    </footer>
  </div>
</template>

<script>

import AppNavbar from './AppNavbar.vue';
import { useRouter } from 'vue-router';

export default {
  components: {
    AppNavbar,
  },
  setup() {
    const router = useRouter();

    // Fungsi untuk mengarahkan ke halaman diagnosa
    const startExpertSystem = () => {
      router.push('/diagnosa');
    };

    // Fungsi untuk mengarahkan ke daftar penyakit
    const goToDiseases = () => {
      router.push('/daftar-penyakit');
    };

    return {
      startExpertSystem,
      goToDiseases, // Mengembalikan fungsi goToDiseases
    };
  },
};
</script>


<style scoped>
/* Global Styles */
body {
  margin: 0;
  font-family: Arial, sans-serif;
  line-height: 1.6;
}

.container {
  width: 80%;
  margin: 0 auto;
  text-align: center;
}

/* Header Section */
.header {
  background-color: #4CAF50;
  color: white;
  text-align: center;
  padding: 5rem 1rem;
}

.header .container {
  margin-top: 2rem; 
}

.header .title {
  font-size: 2rem; 
  margin-bottom: 1rem;
}

.header .subtitle {
  font-size: 1.2rem; 
  margin-bottom: 2rem;
}

.header .btn {
  background-color: white;
  color: #4CAF50;
  border: none;
  padding: 0.8rem 1.5rem;
  font-size: 1rem;
  font-weight: bold;
  border-radius: 5px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.header .btn:hover {
  background-color: #45a049;
  color: white;
}

/* About Section */
.about {
  background-color: #ffffff;
  padding: 4rem 1rem; 
  text-align: center;
}

.about .container {
  max-width: 800px;
  margin: 0 auto;
}

.about h2 {
  font-size: 2.5rem;
  color: #333;
  margin-bottom: 1.5rem;
  font-weight: bold;
}

.about p {
  font-size: 1.2rem;
  color: #555;
  line-height: 1.8;
}

/* Features Section */
.features {
  background-color: #f9f9f9;
  padding: 4rem 1rem;
  text-align: center;
}

.features .container {
  max-width: 1200px;
  margin: 0 auto;
}

.features h2 {
  font-size: 2.5rem;
  color: #333;
  margin-bottom: 2rem;
  font-weight: bold;
}

.feature-items {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 2rem;
}

.feature {
  background-color: white;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  padding: 2rem;
  width: 100%;
  max-width: 300px;
  text-align: center;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.feature:hover {
  transform: translateY(-10px); 
  box-shadow: 0 8px 12px rgba(0, 0, 0, 0.15);
}

.feature h3 {
  font-size: 1.5rem;
  color: #4CAF50;
  margin-bottom: 1rem;
}

.feature p {
  font-size: 1rem;
  color: #555;
  line-height: 1.6;
}


/* Footer Section */
.footer {
  background-color: #333;
  color: #f9f9f9;
  padding: 2rem 1rem;
  text-align: center;
}

.footer .container {
  max-width: 1200px;
  margin: 0 auto;
}

.footer p {
  font-size: 1rem;
  margin: 0.5rem 0;
}

.footer a {
  color: #4CAF50;
  text-decoration: none;
  font-weight: bold;
}
.footer a:hover {
  text-decoration: underline;
}
</style>
