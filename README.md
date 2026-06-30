# 🌾 Sistem Pakar Diagnosis Penyakit Tanaman Padi

## 📌 Deskripsi Proyek

**Sistem Pakar Diagnosis Penyakit Tanaman Padi** adalah aplikasi berbasis web yang bertujuan untuk membantu petani atau pengguna dalam **mendiagnosis penyakit pada tanaman padi** berdasarkan gejala yang dialami. Sistem ini meniru cara berpikir seorang pakar dengan memanfaatkan metode Certainty Faktor untuk memberikan hasil diagnosis dan rekomendasi.

Proyek ini dikembangkan sebagai bagian dari **portofolio akademik** dan menerapkan arsitektur **frontend–backend terpisah** menggunakan teknologi modern.

---

## 🎯 Tujuan Sistem

* Membantu pengguna mengenali penyakit tanaman padi sejak dini
* Memberikan hasil diagnosis berdasarkan gejala yang dipilih
* Menyediakan sistem pakar sederhana yang mudah digunakan
* Mengimplementasikan konsep sistem pakar dalam aplikasi web

---

## 🏗️ Arsitektur Sistem

Sistem dibangun dengan konsep **client–server**:

* **Frontend**: Vue.js
  Menyediakan antarmuka pengguna untuk memilih gejala dan menampilkan hasil diagnosis.

* **Backend**: FastAPI (Python)
  Menangani logika sistem pakar, pemrosesan aturan (rules), dan pengembalian hasil diagnosis melalui REST API.

---

## 🛠️ Teknologi yang Digunakan

### Frontend

* Vue.js
* HTML, CSS, JavaScript
* Axios (untuk komunikasi API)

### Backend

* Python
* FastAPI
* Uvicorn

---

## ⚙️ Fitur Utama

* Input gejala penyakit tanaman padi
* Proses inferensi berbasis aturan (rule-based reasoning)
* Menampilkan hasil diagnosis penyakit
* Arsitektur frontend dan backend terpisah

---

## 📂 Struktur Folder (Contoh)

```
project_3/
├── sistem-pakar-frontend/   # Frontend Vue.js
│   ├── src/
│   └── public/
│
├── sistem-pakar-backend/    # Backend FastAPI
│   ├── main.py
│
└── README.md
```

---

## 🚀 Cara Menjalankan Aplikasi

### 1️⃣ Menjalankan Backend (FastAPI)

```bash
cd sistem-pakar-backend
pip install fastapi uvicorn
uvicorn main:app --reload
```

Backend akan berjalan di:

```
http://127.0.0.1:8000
```

---

### 2️⃣ Menjalankan Frontend (Vue.js)

```bash
cd sistem-pakar-frontend
npm install
npm run serve
```

Frontend akan berjalan di:

```
http://localhost:8080
```

---

## 📊 Output Sistem

* Hasil diagnosis penyakit tanaman padi
* Informasi penyakit berdasarkan gejala yang dipilih

---

## 📌 Catatan

* Proyek ini dikembangkan untuk **keperluan pembelajaran dan portofolio**
* Sistem pakar menggunakan pendekatan **rule-based**, bukan machine learning
* Pengembangan lebih lanjut dapat mencakup:

  * Penambahan basis pengetahuan penyakit
  * Penyimpanan data diagnosis
  * Peningkatan tampilan antarmuka

---

## 👤 Author

**Bayyinahtun Dwi Sumatri**
Mahasiswa Ilmu Komputer
Minat: Web Development, Sistem Pakar, dan Kecerdasan Buatan

---

⭐ *Silakan gunakan atau kembangkan proyek ini untuk pembelajaran.*
# expert-system-main
# expert-system-main
# expertsystem
