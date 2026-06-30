<template>
  <div>
    <h1>Sistem Diagnosa Penyakit Tanaman Padi</h1>

    <!-- Form untuk memilih gejala -->
    <form @submit.prevent="submitDiagnosa">
      <div v-for="(gejala, kode) in gejala" :key="kode" class="gejala-item">
        <label>{{ gejala.nama }}</label>
        <select v-model="gejala_terpilih[kode]" @change="updateConfidence(kode)">
          <option value="0.0">Tidak</option>
          <option value="0.2">Tidak Tahu</option>
          <option value="0.4">Sedikit Yakin</option>
          <option value="0.6">Cukup Yakin</option>
          <option value="0.8">Yakin</option>
          <option value="1.0">Sangat Yakin</option>
        </select>
        <div v-if="gejala_terpilih[kode] !== '0.0'">
          <label>Keyakinan: {{ confidence[kode] }}</label>
        </div>
      </div>

      <button type="submit">Diagnosa</button>
    </form>

<!-- Tampilkan hasil diagnosa -->
<div v-if="hasilDiagnosa.length > 0" class="hasil-diagnosa-box">
  <h2>Hasil Diagnosa</h2>
  <ul>
    <li v-for="(data, index) in hasilDiagnosa" :key="index">
      <span class="diagnosa-penyakit">{{ data.nama_penyakit }}</span> - 
      <span class="diagnosa-cf">{{ data.cf }}%</span>
    </li>
  </ul>
  <h3><b>{{ kesimpulan }}</b></h3>
  </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      gejala: {
        G1: { nama: '1. Daun berwarna hijau kelabu', CF_Rule: 0.2 },
        G2: { nama: '2. Daun melipat dan menggulung', CF_Rule: 0.3 },
        G3: { nama: '3. Daun layu dan mati', CF_Rule: 0.8 },
        G4: { nama: '4. Timbul bercak abu-abu kekuningan pada tepi daun', CF_Rule: 0.5 },
        G5: { nama: '5. Daun mengering', CF_Rule: 0.7 },
        G6: { nama: '6. Bercak berbentuk elips, ukuran 2mm - 20 mm', CF_Rule: 0.3 },
        G7: { nama: '7. Bercak berupa titik jarum atau beberapa mm tetapi belum berbentuk elips', CF_Rule: 0.1 },
        G8: { nama: '8. Pusat bercak berwarna putih', CF_Rule: 0.5 },
        G9: { nama: '9. Seluruh tanaman mati sebelum berbunga', CF_Rule: 1.0 },
        G10: { nama: '10. Bercak coklat kehitaman pada pangkal leher malai', CF_Rule: 0.8 },
        G11: { nama: '11. Leher malai membusuk', CF_Rule: 0.7 },
        G12: { nama: '12. Perubahan warna daun', CF_Rule: 0.3 },
        G13: { nama: '13. Tanaman tumbuh kerdil', CF_Rule: 0.6 },
        G14: { nama: '14. Jumlah anakan sedikit', CF_Rule: 0.5 },
        G15: { nama: '15. Sebagian besar gabah hampa', CF_Rule: 0.8 },
        G16: { nama: '16. Daun berwarna coklat dengan titik tengah berwarna kuning pucat, putih kotor', CF_Rule: 0.6 },
        G17: { nama: '17. Bercak berbentuk oval sampai bulat berukuran sebesar biji wijen pada permukaan daun, pelepah daun atau pada gabah', CF_Rule: 0.5 },
        G18: { nama: '18. Bercak berukuran 1-3 cm', CF_Rule: 0.5 },
        G19: { nama: '19. Bercak berwarna kehitam hitaman', CF_Rule: 0.6 },
        G20: { nama: '20. Bentuk bercak tidak teratur pada sisi luar pelepah daun dan secara bertahap membesar', CF_Rule: 0.5 },
        G21: { nama: '21. Anakan mati', CF_Rule: 0.8 },
        G22: { nama: '22. Batang padi menjadi lemah', CF_Rule: 0.6 },
        G23: { nama: '23. Tanaman rebah', CF_Rule: 0.8 },
        G24: { nama: '24. Noda berbentuk bulat memanjang hingga tidak teratur dengan panjang 0,5 - 1,5 cm', CF_Rule: 0.5 },
        G25: { nama: '25. Bercak berwarna abu-abu di tengahnya dan coklat atau coklat abu-abu di pinggirnya', CF_Rule: 0.5 },
        G26: { nama: '26. Bercak membesar, bersambung, dan menutupi seluruh pelepah daun', CF_Rule: 0.7 },
        G27: { nama: '27. Kerdil dengan anakan yang berlebihan', CF_Rule: 0.6 },
        G28: { nama: '28. Tanaman tampak seperti rumput', CF_Rule: 0.3 },
        G29: { nama: '29. Daun tanaman padi menjadi sempit, pendek, kaku', CF_Rule: 0.5 },
        G30: { nama: '30. Daun berwarna hijau pucat', CF_Rule: 0.2 },
        G31: { nama: '31. Terdapat bercak karat', CF_Rule: 0.4 },
      },
      daftar_penyakit: {
        'P1': { nama: 'Hawar daun bakteri', gejala: ['G1', 'G2', 'G3', 'G4', 'G5'] },
        'P2': { nama: 'Blast pada daun', gejala: ['G6', 'G7', 'G8'] },
        'P3': { nama: 'Blast pada leher', gejala: ['G9', 'G10'] },
        'P4': { nama: 'Tungro', gejala: ['G11', 'G12', 'G13', 'G14', 'G15'] },
        'P5': { nama: 'Bercak coklat', gejala: ['G16', 'G17'] },
        'P6': { nama: 'Hawar pelepah', gejala: ['G18'] },
        'P7': { nama: 'Busuk batang', gejala: ['G19', 'G20', 'G21', 'G22', 'G23'] },
        'P8': { nama: 'Busuk pelepah', gejala: ['G24', 'G25', 'G26'] },
        'P9': { nama: 'Kerdil rumput', gejala: ['G27', 'G28', 'G29', 'G30', 'G31'] },
      },
      gejala_terpilih: {},
      confidence: {},
      hasilDiagnosa: [],
      kesimpulan: "",
    };
  },

  methods: {
    updateConfidence(kode) {
      const yakin = this.gejala_terpilih[kode];
      this.confidence[kode] = yakin === '0.0' ? 'Tidak Tahu' : yakin;
    },

    async submitDiagnosa() {
  try {
    const payload = { gejala_terpilih: {} };
    for (const kode in this.gejala_terpilih) {
      const yakin = parseFloat(this.gejala_terpilih[kode]);
      if (yakin > 0.0) {
        payload.gejala_terpilih[kode] = yakin;
      }
    }

    console.log("Payload:", payload);

    const response = await axios.post("http://127.0.0.1:8000/diagnosa/", payload);
    console.log("Response Data:", response.data);

    if (response.data) {
      // Menyimpan semua penyakit yang terdeteksi
      this.hasilDiagnosa = response.data['Semua Penyakit dan CF'].map(penyakit => ({
        nama_penyakit: penyakit.Penyakit,
        cf: parseFloat((penyakit.CF * 100).toFixed(2)) // Mengonversi CF menjadi angka
      }));

      // Menentukan penyakit dengan CF tertinggi
      const maxCF = Math.max(...this.hasilDiagnosa.map(penyakit => penyakit.cf));

      // Mencari penyakit dengan CF tertinggi
      const penyakitTertinggi = this.hasilDiagnosa.filter(penyakit => penyakit.cf === maxCF);

      // Jika ada lebih dari satu penyakit dengan CF tertinggi yang sama
      if (penyakitTertinggi.length > 1) {
        this.kesimpulan = "Penyakit Belum Tersedia";
      } else {
        // Jika hanya ada satu penyakit dengan CF tertinggi
        this.kesimpulan = `Penyakit yang paling mungkin: ${penyakitTertinggi[0].nama_penyakit} dengan keyakinan ${penyakitTertinggi[0].cf}%`;
      }
    }
  } catch (error) {
    console.error("Error diagnosa:", error);
  }
}

    },
};
</script>

<style scoped>
/* Container utama */
div {
font-family: Arial, sans-serif;
margin: 20px;
padding: 20px;
background-color: #f9f9f9;
border-radius: 8px;
box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Judul utama */
h1 {
font-size: 24px;
font-weight: bold;
text-align: center;
color: #333;
margin-bottom: 20px;
}
/* Form */
form {
display: flex;
flex-direction: column;
gap: 15px;
}

.gejala-item {
display: flex;
flex-direction: column;
gap: 5px;
}

label {
font-size: 16px;
color: #444;
}

select {
padding: 8px;
font-size: 14px;
border: 1px solid #ddd;
border-radius: 4px;
background-color: #fff;
}

select:focus {
border-color: #007bff;
outline: none;
}

button {
padding: 12px 20px;
font-size: 16px;
background-color: #28a745;
color: white;
border: none;
border-radius: 5px;
cursor: pointer;
transition: background-color 0.3s;
margin-top: 20px;
}

button:hover {
background-color: #218838;
}

/* Hasil Diagnosa */
.hasil-diagnosa-box {
margin-top: 30px;
background-color: #bdffae;
padding: 15px;
border-radius: 5px;
box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

h2 {
font-size: 22px;
color: #333;
margin-bottom: 15px;
}

ul {
list-style-type: none;
padding-left: 0;
}

.diagnosa-item {
font-size: 16px;
margin-bottom: 10px;
}

.diagnosa-penyakit {
font-weight: bold;
color: #007bff;
}

.diagnosa-cf {
color: #555;
}

/* Kesimpulan diagnosa */
h3 {
font-size: 18px;
font-weight: normal;
margin-top: 20px;
color: #333;
text-align: center;
}

/* Responsive */
@media (max-width: 600px) {
form {
  padding: 15px;
}

button {
  font-size: 0.9rem;
}

h1 {
  font-size: 1.8rem;
}
}
</style>
