<template>
    <div class="daftar-penyakit">
      <header class="header">
        <h1>Daftar Penyakit Tanaman Padi</h1>
        <p class="subtitle">Pelajari berbagai penyakit yang dapat menyerang tanaman padi</p>
      </header>
  
      <!-- Daftar Nama Penyakit -->
      <section class="diseases">
        <div class="container">
          <ul class="disease-list">
            <li class="disease-item">
              <h3>Hawar Daun Bakteri</h3>
              <p>Penyakit yang disebabkan oleh bakteri <i>Xanthomonas oryzae</i> dan dapat merusak daun tanaman padi. Penyakit terjadi pada musim hujanatau musim kemarau yang basah, terutama pada
                lahan sawah yang selalu tergenang, dan dipupuk N tinggi (> 250 kg urea /ha)</p>
            </li>
            <li class="disease-item">
              <h3>Blast Pada Daun</h3>
              <p>Blas daun merupakan bercak coklat kehitaman, berbentuk belah ketupat, dengan pusat bercak berwarna putih</p>
            </li>
            <li class="disease-item">
              <h3>Blast Pada Leher</h3>
              <p>blas leher berupa bercak coklat kehitaman pada pangkal leher yang dapat mengakibatkan leher malai tidak mampu menopang malai dan patah </p>
            </li>
            <li class="disease-item">
              <h3>Tungro</h3>
              <p>Tungro disebabkan oleh infeksi dua virus yang berbeda, yaitu Rice <i>Tungro bacilliform virus</i> (RTBV) dan <i>Rice Tungro spherical</i>virus (RTSV)</p>
            </li>
            <li class="disease-item">
              <h3>Bercak Coklat</h3>
              <p>Penyakit ini disebabkan oleh jamur <i>Helmintosporium oryzae</i> pada pertanaman. Bercak coklat dapat menyebabkan kematian tanaman muda dan menurunkan kualitas gabah</p>
            </li>
            <li class="disease-item">
              <h3>Hawar Pelepah</h3>
              <p> Penyakit disebabkan oleh jamur <i>Rhizoctonia solani</i>, dengan gejala awal berupa bercak oval atau bulat berwarna putih pucat pada pelepah</p>
            </li>
            <li class="disease-item">
              <h3>Busuk Batang</h3>
              <p>Busuk batang merupakan penyakit yang menginfeksi bagian tanaman dalam kanopi dan menyebabkan tanaman menjadi mudah rebah</p>
            </li>
            <li class="disease-item">
              <h3>Busuk Pelepah</h3>
              <p>Infeksi terjadi pada pelepah daun paling atas yang menutupi malai muda pada akhir fase bunting. Infeksi berat menyebabkan malai hanya muncul sebagian (tidak berkembang) dan mengerut. Malai yang muncul sebagian hanya dapat menghasilkan sedikit bulir yang berisi</p>
            </li>
            <li class="disease-item">
              <h3>Kerdil Rumput</h3>
              <p> Tanaman yang terinfeksi berat akan menjadi kerdil dengan anakan yang berlebihan, sehingga tampak seperti rumput. Penyakit ini disebabkan oleh virus yang ditularkan oleh wereng coklat, dan tanaman inangnya hanya padi</p>
            </li>
          </ul>
        </div>
      </section>

      <!-- Tombol kembali -->
      <footer class="footer">
        <button class="btn-back" @click="goBack">Kembali ke Halaman Utama</button>
      </footer>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      goBack() {
        // Kembali ke halaman sebelumnya
        this.$router.go(-1);
      },
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
    width: 90%;
    max-width: 1200px;
    margin: 0 auto;
  }
  
  /* Section Header */
  .header {
    background-color: #4CAF50;
    color: white;
    text-align: center;
    padding: 20px 0;
  }
  
  .header h1 {
    margin: 0;
    font-size: 2.5rem;
  }
  
  .subtitle {
    font-size: 1rem;
    margin-top: 10px;
  }
  
  /* Section Penyakit */
  .diseases {
    background-color: #f9f9f9;
    padding: 40px 20px;
  }
  
  .disease-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  
  .disease-item {
    background-color: white;
    margin-bottom: 20px;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease;
  }
  
  .disease-item:hover {
    transform: translateY(-5px);
  }
  
  .disease-item h3 {
    margin-top: 0;
    font-size: 1.5rem;
    color: #4CAF50;
  }
  
  .disease-item p {
    margin: 10px 0 0;
    font-size: 1rem;
    color: #555;
  }
  
  /* Tombol kembali */
  .footer {
    text-align: center;
    margin-top: 20px;
  }
  
  .btn-back {
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    font-size: 1rem;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background 0.3s ease;
  }
  
  .btn-back:hover {
    background-color: #4CAF50;
  }
  </style>
  