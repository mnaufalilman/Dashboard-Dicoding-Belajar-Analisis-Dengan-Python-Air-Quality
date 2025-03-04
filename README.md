# 🌍💨 Streamlit Dashboard Pemantauan Kualitas Udara  

Proyek ini adalah aplikasi **Streamlit** yang digunakan untuk memantau dan menganalisis kualitas udara berdasarkan data historis.  

## 📌 Fitur Utama  
✅ **Filter Data** berdasarkan tahun dan stasiun pemantauan  
✅ **Visualisasi Tren** untuk melihat perubahan polutan seiring waktu  
✅ **Heatmap Korelasi** antara faktor cuaca dan polutan udara  
✅ **Boxplot Distribusi** untuk membandingkan kualitas udara di berbagai stasiun

## 📊 Visualisasi
Beberapa grafik yang tersedia dalam dashboard ini:

1️⃣ **Tren Konsentrasi Polutan**
📈 Menampilkan perubahan kadar polutan (PM2.5, PM10, SO2, NO2, CO, O3) dari waktu ke waktu.

2️⃣ **Heatmap Korelasi**
🔥 Menunjukkan hubungan antara variabel cuaca (TEMP, PRES, DEWP) dan tingkat polusi udara.

3️⃣ **Distribusi Polutan di Berbagai Stasiun**
📊 Boxplot untuk membandingkan kualitas udara antar stasiun pemantauan.



## 📦 Instalasi Dependencies
Sebelum menjalankan aplikasi, instal semua dependencies yang dibutuhkan:
```sh
pip install -r requirements.txt
```

## 🚀 Cara Menjalankan  
Pastikan **Python** dan **Streamlit** sudah terinstal, lalu jalankan:  
```sh
streamlit run dashboard.py
```

