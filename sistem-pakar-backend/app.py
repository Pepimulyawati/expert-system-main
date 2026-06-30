from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# daftar nama penyakit dan gejala
daftar_penyakit = {
    'P1' : {'nama' : 'Hawar daun bakteri', 'gejala' : ['G1', 'G2', 'G3', 'G4', 'G5']},
    'P2' : {'nama' : 'Blast pada daun', 'gejala' : ['G6', 'G7', 'G8']},
    'P3' : {'nama' : 'Blast pada leher', 'gejala' : ['G9', 'G10']},
    'P4' : {'nama' : 'Tungro', 'gejala' : ['G11', 'G12', 'G13', 'G14', 'G15']},
    'P5' : {'nama' : 'Bercak coklat', 'gejala' : ['G16', 'G17']},
    'P6' : {'nama' : 'Hawar pelepah', 'gejala' : ['G18']},
    'P7' : {'nama' : 'Busuk batang', 'gejala' : ['G19', 'G20', 'G21', 'G22', 'G23']},
    'P8' : {'nama' : 'Busuk pelepah', 'gejala' : ['G24', 'G25', 'G26']},
    'P9' : {'nama' : 'Kerdil rumput', 'gejala' : ['G27', 'G28', 'G29', 'G30', 'G31']}, 
}

gejala = {
    'G1' : {'nama' : 'Daun berwarna hijau kelabu', 'CF_Rule' :0.2},
    'G2' : {'nama' : 'Daun melipat dan menggulung', 'CF_Rule' :0.3},
    'G3' : {'nama' : 'Daun layu dan mati', 'CF_Rule' :0.8},
    'G4' : {'nama' : 'Timbul bercak abu-abu kekuningan pada tepi daun', 'CF_Rule' :0.5},
    'G5' : {'nama' : 'Daun mengering', 'CF_Rule' :0.7},
    'G6' : {'nama' : 'Bercak berbentuk elips, ukuran 2mm - 20 mm', 'CF_Rule' :0.3},
    'G7' : {'nama' : 'Bercak berupa titik jarum atau beberapa mm tetapi belum berbentuk elips', 'CF_Rule' :0.1},
    'G8' : {'nama' : 'Pusat bercak berwarna putih', 'CF_Rule' : 0.5},
    'G9' : {'nama' : 'Seluruh tanaman mati sebelum berbunga', 'CF_Rule' : 1.0},
    'G10' : {'nama' : 'Bercak coklat kehitaman pada pangkal leher malai', 'CF_Rule' : 0.8},
    'G11' : {'nama' : 'Leher malai membusuk', 'CF_Rule' : 0.7},
    'G12' : {'nama' : 'Perubahan warna daun', 'CF_Rule' : 0.3},
    'G13' : {'nama' : 'Tanaman tumbuh kerdil', 'CF_Rule' : 0.6},
    'G14' : {'nama' : 'Jumlah anakan sedikit', 'CF_Rule' : 0.5},
    'G15' : {'nama' : 'Sebagian besar gabah hampa', 'CF_Rule' : 0.8},
    'G16' : {'nama' : 'Daun berwarna coklat dengan titik tengah berwarna kuning pucat, putih kotor', 'CF_Rule' : 0.6},
    'G17' : {'nama' : 'Bercak berbentuk oval sampai bulat berukuran sebesar biji wijen pada permukaan daun, pelepah daun atau pada gabah', 'CF_Rule' : 0.5},
    'G18' : {'nama' : 'Bercak berukuran 1-3 cm', 'CF_Rule' : 0.5},
    'G19' : {'nama' : 'Bercak berwarna kehitam hitaman', 'CF_Rule' : 0.6},
    'G20' : {'nama' : 'Bentuk bercak tidak teratur pada sisi luar pelepah daun dan secara bertahap membesar', 'CF_Rule' : 0.5},
    'G21' : {'nama' : 'Anakan mati', 'CF_Rule' : 0.8},
    'G22' : {'nama' : 'Batang padi menjadi lemah', 'CF_Rule' : 0.6},
    'G23' : {'nama' : 'Tanaman rebah', 'CF_Rule' : 0.8},
    'G24' : {'nama' : 'Noda berbentuk bulat memanjang hingga tidak teratur dengan panjang 0,5 - 1,5 cm', 'CF_Rule' : 0.5},
    'G25' : {'nama' : 'Bercak berwarna abu-abu di tengahnya dan coklat atau coklat abu-abu di pinggirnya', 'CF_Rule' : 0.5},
    'G26' : {'nama' : 'Bercak membesar, bersambung, dan menutupi seluruh pelepah daun', 'CF_Rule' : 0.7},
    'G27' : {'nama' : 'Kerdil dengan anakan yang berlebihan', 'CF_Rule' : 0.6},
    'G28' : {'nama' : 'Tanaman tampak seperti rumput', 'CF_Rule' : 0.3},
    'G29' : {'nama' : 'Daun tanaman padi menjadi sempit, pendek, kaku', 'CF_Rule' : 0.5},
    'G30' : {'nama' : 'Daun berwarna hijau pucat', 'CF_Rule' : 0.2},
    'G31' : {'nama' : 'Terdapat bercak karat', 'CF_Rule' : 0.4},
}

keyakinan_user = {
    "1": 0.0, #Tidak
    "2": 0.2, #Tidak tahu
    "3": 0.4, #sedikit yakin
    "4": 0.6, #cukup yakin
    "5": 0.8, #yakin
    "6": 1.0 #sangat yakin
}

class GejalaTerpilih(BaseModel):
    gejala_terpilih: Dict[str, float]

def hitung_cf(gejala_terpilih: Dict[str, float]) -> Dict[str, float]:
    hasil_cf = {}
    for kode_penyakit, data_penyakit in daftar_penyakit.items():
        cf_penyakit = 0
        for kode_gejala in data_penyakit['gejala']:
            if kode_gejala in gejala_terpilih:
                CF_Rule = gejala[kode_gejala]['CF_Rule']
                keyakinan = gejala_terpilih[kode_gejala]
                CF_gejala = CF_Rule * keyakinan
                cf_penyakit = cf_penyakit + CF_gejala * (1 - abs(cf_penyakit))
        if cf_penyakit > 0:
            hasil_cf[kode_penyakit] = cf_penyakit
    return hasil_cf

@app.post("/diagnosa/")
def diagnosa(gejala_terpilih: GejalaTerpilih):
    for k, v in gejala_terpilih.gejala_terpilih.items():
        if v not in keyakinan_user.values():
            raise HTTPException(status_code=422, detail=f"Nilai keyakinan {v} tidak valid untuk gejala {k}")

    # Hitung CF
    cf_hasil = hitung_cf(gejala_terpilih.gejala_terpilih)
    if not cf_hasil:
        raise HTTPException(status_code=404, detail="Tidak ada penyakit yang cocok berdasarkan gejala yang dipilih")
    
    # Urutkan hasil berdasarkan CF tertinggi
    hasil_urut = sorted(cf_hasil.items(), key=lambda item: item[1], reverse=True)
    
    # Tentukan CF tertinggi dan kumpulkan penyakit dengan CF tertinggi
    cf_tertinggi = hasil_urut[0][1]
    penyakit_terdeteksi = [daftar_penyakit[penyakit]['nama'] for penyakit, cf in hasil_urut if cf == cf_tertinggi]
    
    # Jika lebih dari satu penyakit memiliki CF tertinggi yang sama, tentukan sebagai "Penyakit Belum Tersedia"
    if len(penyakit_terdeteksi) > 1:
        hasil_diagnosis = {
            "Semua Penyakit dan CF": [{"Penyakit": daftar_penyakit[penyakit]['nama'], "CF": cf} for penyakit, cf in hasil_urut],
            "Kesimpulan": "Penyakit Belum Tersedia"
        }
    else:
        penyakit_dan_cf = [
            {"Penyakit": daftar_penyakit[penyakit]['nama'], "CF": cf}
            for penyakit, cf in hasil_urut
        ]
        
        # Hasil diagnosis
        hasil_diagnosis = {
            "Semua Penyakit dan CF": penyakit_dan_cf,
            "Penyakit yang terdeteksi": penyakit_terdeteksi,
            "CF Tertinggi": cf_tertinggi
        }

    return hasil_diagnosis
