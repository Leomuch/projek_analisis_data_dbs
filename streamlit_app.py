import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

# Judul Dashboard
st.title("Dashboard Analisis Penyewaan Sepeda")

# Membaca Dataset
df_day = pd.read_csv("archive/day.csv")

# Menampilkan 5 baris pertama
df_preview = df_day.head()
st.subheader("Preview Dataset")
st.dataframe(df_preview)

# Menampilkan Informasi Dataset
st.subheader("Informasi Dataset")
st.text(str(df_day.info()))

# Mengecek Missing Values
st.subheader("Cek Missing Values")
st.write(df_day.isnull().sum())

# Mengecek Data Duplikat
st.subheader("Cek Data Duplikat")
st.write(f"Jumlah data duplikat: {df_day.duplicated().sum()}")

# Statistik Deskriptif
st.subheader("Statistik Deskriptif")
st.write(df_day.describe())

# Visualisasi Distribusi Data
st.subheader("Distribusi Data")
fig, ax = plt.subplots(figsize=(12, 8))
df_day.hist(figsize=(12, 8), bins=30, ax=ax)
st.pyplot(fig)

# Cleaning Data
df_day['season'] = df_day['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
df_day['weathersit'] = df_day['weathersit'].map({1: 'Clear', 2: 'Cloudy', 3: 'Light Rain/Snow', 4: 'Heavy Rain/Snow'})
df_day['yr'] = df_day['yr'].map({0: '2011', 1: '2012'})
df_day['dteday'] = pd.to_datetime(df_day['dteday'])
df_day.drop(columns=['instant'], inplace=True)
df_day['temp'] = df_day['temp'] * 41
df_day['hum'] = df_day['hum'] * 100

# Visualisasi Pengaruh Cuaca terhadap Penyewaan
st.subheader("Penyewaan Sepeda Berdasarkan Cuaca")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(data=df_day, x="weathersit", y="cnt", ax=ax)
ax.set_title("Penyewaan Sepeda Berdasarkan Cuaca")
st.pyplot(fig)

# Visualisasi Tren Penyewaan Sepeda
st.subheader("Tren Penyewaan Sepeda per Bulan")
df_day['year'] = df_day['dteday'].dt.year
df_day['month'] = df_day['dteday'].dt.month
fig, ax = plt.subplots(figsize=(12, 5))
sns.lineplot(data=df_day, x='month', y='cnt', hue='year', marker="o", ax=ax)
ax.set_title("Tren Penyewaan Sepeda per Bulan")
st.pyplot(fig)

# Korelasi Antar Variabel
st.subheader("Heatmap Korelasi Antar Variabel")
correlation_features = ["temp", "atemp", "hum", "windspeed", "casual", "registered", "cnt"]
correlation_matrix = df_day[correlation_features].corr()
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, ax=ax)
st.pyplot(fig)
