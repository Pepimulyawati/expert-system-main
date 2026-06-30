/* eslint-disable vue/multi-word-component-names */

<template>
    <nav class="navbar">
      <div class="container">
        <ul class="nav-links">
          <li><a href="#header">Beranda</a></li>
          <li><a href="#about">Tentang</a></li>
          <li><a href="#features">Fitur Utama</a></li>
          <li><a @click.prevent="goToDiseases">Daftar Penyakit</a></li>
          <li><a href="#footer">Kontak</a></li>
        </ul>
      </div>
    </nav>
  </template>
  
  <script>
  export default {
    methods: {
      goToDiseases() {
        // Mengarahkan ke halaman daftar penyakit menggunakan router
        this.$router.push('/daftar-penyakit');
      }
    }
  }
  </script>
  
  <style scoped>
  /* Global styles untuk navbar */
  .navbar {
  background-color: #333;
  position: sticky;
  top: 0;
  z-index: 1000;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.container {
  display: flex;
  justify-content: center;
}
  
.nav-links {
  list-style: none;
  display: flex;
  gap: 2rem;
  margin: 0;
  padding: 0;
}
  
.nav-links li {
  position: relative;
}

.nav-links a {
  text-decoration: none;
  color: white;
  font-weight: bold;
  font-size: 1.1rem;
  transition: color 0.3s ease, transform 0.3s ease;
}
  
.nav-links a:active {
  color: #2E7D32;
}

  /* Responsivitas: navbar pada perangkat kecil */
  @media (max-width: 768px) {
  .nav-links {
    display: none;
  }
  .navbar {
    position: relative;
  }


  .nav-links li::after {
  content: '';
  display: block;
  width: 0;
  height: 2px;
  background: #4CAF50;
  transition: width 0.3s;
  margin: auto;
}
.nav-links li:hover::after {
  width: 100%;
}

}

  </style>

  