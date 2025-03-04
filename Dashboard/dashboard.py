import os
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Load Data
folder_path = "Data"

# Ambil semua file CSV dalam folder
all_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# Gabungkan semua file CSV menjadi satu DataFrame
df_list = [pd.read_csv(os.path.join(folder_path, file)) for file in all_files]
df_AirQuality = pd.concat(df_list, ignore_index=True)

# Ubah format tanggal
df_AirQuality['date'] = pd.to_datetime(df_AirQuality[['year', 'month', 'day', 'hour']])

# Streamlit Dashboard
st.title("🌆 Beijing Air Quality Dashboard 💨")
st.markdown("""
🏙️ **Bagaimana kualitas udara di Beijing saat ini?**  
💨 Apakah polusi meningkat atau menurun dari tahun ke tahun?  
📌 Temukan jawabannya dengan data real dan visualisasi interaktif!
""")

# Sidebar Filter
st.sidebar.header("Filter Data")
selected_year = st.sidebar.selectbox("Pilih Tahun", sorted(df_AirQuality['year'].unique()), index=0)
selected_station = st.sidebar.multiselect("Pilih Stasiun", df_AirQuality['station'].unique(), default=df_AirQuality['station'].unique())

# Filter Data
df_filtered = df_AirQuality[(df_AirQuality['year'] == selected_year) & (df_AirQuality['station'].isin(selected_station))]

# Visualisasi Tren Polutan
st.subheader("Tren Konsentrasi Polutan dari Waktu ke Waktu")
pollutant = st.selectbox("Pilih Polutan", ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3'])

fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(data=df_filtered, x='date', y=pollutant, hue='station', ax=ax)
ax.set_title(f"Tren {pollutant} dari Waktu ke Waktu", fontsize=14)
ax.set_xlabel("Tanggal")
ax.set_ylabel(f"Konsentrasi {pollutant}")
plt.xticks(rotation=45)
st.pyplot(fig)

# Heatmap Korelasi
st.subheader("Korelasi Antara Cuaca dan Polusi Udara")
corr_matrix = df_filtered[['TEMP', 'PRES', 'DEWP', 'PM2.5', 'PM10', 'CO', 'NO2', 'SO2', 'O3']].corr()

fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, ax=ax)
ax.set_title("Heatmap Korelasi Variabel Cuaca dan Polusi Udara", fontsize=14)
st.pyplot(fig)

# Distribusi Polutan di Berbagai Stasiun
st.subheader("Distribusi Polutan di Berbagai Stasiun")

fig, axes = plt.subplots(2, 3, figsize=(24, 16))
polutants = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']

for ax, polutant in zip(axes.flatten(), polutants):
    sns.boxplot(x='station', y=polutant, data=df_filtered, ax=ax)
    ax.set_title(f"Distribusi {polutant} di Berbagai Stasiun", fontsize=14)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, fontsize=10)

st.pyplot(fig)


st.sidebar.header('🌍💨 About Us')
st.sidebar.markdown('👨‍💻 Created by Muhammad Naufal Ilman')
