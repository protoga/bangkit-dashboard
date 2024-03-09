"""Dislaimer! Saya mohon maaf tidak membuat bagian datetime dan metric karena pada dataset yang
saya ambil tidak menggunakan kolom waktu, terimakasih atas pengertiannya."""

import pandas as pd #mengimport library pandas
import matplotlib.pyplot as plt #mengimport library matplotlib.pyplot
import seaborn as sns #mengimport library seaborn
import streamlit as st #mengimport library streamlit
from babel.numbers import format_currency #mengimport fungsi format_currency dari library babel.numbers
from notebook import * #mengimport semua fungsi yang ada di file notebook.py
sns.set(style='dark') #mengatur style seaborn

"""def create_sum_seller_city(df):
    sum_seller_city_df = df.groupby("seller_city").quantity_x.sum().sort_values(ascending=False).reset_index()
    return sum_seller_city_df"""

#Header of the dashboard
st.header("Dashboard of Global Sales PT. Gabriel's ") #membuat header

st.subheader("Horizontal Bar Chart") #membuat subheader
 
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(50, 20)) #membuat 2 plot dalam 1 baris
 
top = sd_v1.head(5) #variabel top menampung 5 data teratas dari sd_v1
bottom = sd_v1.tail(5) #variabel bottom menampung 5 data terbawah dari sd_v1
top2 = sd_v2.head(5) #variabel top2 menampung 5 data teratas dari sd_v2
bottom2 = sd_v2.tail(5) #variabel bottom2 menampung 5 data terbawah dari sd_v2

combine = pd.concat([top, bottom]) #menggabungkan variabel top dan bottom
combine2 = pd.concat([top2, bottom2]) #menggabungkan variabel top2 dan bottom2

sns.barplot(x="Total Sales", y="Kota", data=combine, palette="Blues_r", ax=ax[0]) #membuat barplot dengan sumbu x adalah Total Sales dan sumbu y adalah Kota
ax[0].set_ylabel("Kota", fontsize=40) #mengatur label sumbu y
ax[0].set_xlabel("Total Sales", fontsize=40) #mengatur label sumbu x
ax[0].set_title("Total Sales berdasarkan Kota", loc="center", fontsize=70) #mengatur judul plot
ax[0].tick_params(axis='y', labelsize=50) #mengatur ukuran label sumbu y
ax[0].tick_params(axis='x', labelsize=50) #mengatur ukuran label sumbu x
for index, value in enumerate(combine['Total Sales']): #membuat label pada barplot
  ax[0].text(value, index, str(value), fontsize= 40) 

sns.barplot(x="TotalSales", y="Negara", data=combine2, palette="Greens_r", ax=ax[1]) #membuat barplot dengan sumbu x adalah TotalSales dan sumbu y adalah Negara
ax[1].set_ylabel("Negara", fontsize=40) #mengatur label sumbu y
ax[1].set_xlabel("Total Sales", loc="center", fontsize=40) #mengatur label sumbu x
ax[1].invert_xaxis() #membalikkan sumbu x
ax[1].yaxis.set_label_position("right") #mengatur posisi label sumbu y
ax[1].yaxis.tick_right() #mengatur posisi label sumbu y
ax[1].set_title("Total Sales berdasarkan Negara", loc="center", fontsize=70) #mengatur judul plot
ax[1].tick_params(axis='y', labelsize=50) #mengatur ukuran label sumbu y
ax[1].tick_params(axis='x', labelsize=50) #mengatur ukuran label sumbu x
for index, value in enumerate(combine2['TotalSales']): #membuat label pada barplot
  ax[1].text(value, index, str(value), fontsize= 40)
st.pyplot(fig) #menampilkan plot

st.subheader("Vertikal Bar Chart") #membuat subheader
 
col1, col2 = st.columns(2) #membuat 2 kolom
 
with col1: #membuat plot pada kolom pertama
    fig, ax = plt.subplots(figsize=(20, 30)) #membuat plot dengan ukuran 20x30
 
    sns.barplot(y="Kota", x="Total Sales", data=combine.sort_values(by="Kota", ascending=False), palette="Blues_r", ax=ax, order=combine["Kota"], orient= 'h') #membuat barplot dengan sumbu y adalah Kota dan sumbu x adalah Total Sales
    ax.set_title("Total Sales berdasarkan Kota", loc="center", fontsize=50) #mengatur judul plot
    ax.set_ylabel("Kota", fontsize=40) #mengatur label sumbu y
    ax.set_xlabel("Total Sales", loc="center", fontsize=40) #mengatur label sumbu x
    ax.tick_params(axis='x', labelsize=30) #mengatur ukuran label sumbu x
    ax.tick_params(axis='y', labelsize=30) #mengatur ukuran label sumbu y
    st.pyplot(fig) #menampilkan plot
 
with col2: #membuat plot pada kolom kedua
    fig, ax = plt.subplots(figsize=(20, 26.8)) #membuat plot dengan ukuran 20x26.8
    sns.barplot(y="Negara", x="TotalSales", data=combine2.sort_values(by="Negara", ascending=False), palette="Greens_r", ax=ax, order=combine2["Negara"], orient= 'h') #membuat barplot dengan sumbu y adalah Negara dan sumbu x adalah TotalSales
    ax.set_title("Total Sales berdasarkan Negara", loc="center", fontsize=50) #mengatur judul plot
    ax.set_ylabel("Negara", fontsize=40) #mengatur label sumbu y
    ax.set_xlabel("Total Sales", loc="center", fontsize=40) #mengatur label sumbu x
    ax.tick_params(axis='x', labelsize=30) #mengatur ukuran label sumbu x
    ax.tick_params(axis='y', labelsize=30) #mengatur ukuran label sumbu y
    st.pyplot(fig) #menampilkan plot
 
fig, ax = plt.subplots(figsize=(20, 10)) #membuat plot dengan ukuran 20x10
sns.barplot(x="Total Sales", y="Kota", data=combine.sort_values(by="Kota", ascending=False), palette="Greys_r", ax=ax, order=combine["Kota"], orient= 'h') #membuat barplot dengan sumbu x adalah Total Sales dan sumbu y adalah Kota
ax.set_title("Number of Customer by States", loc="center", fontsize=30) #mengatur judul plot
ax.set_ylabel("Kota", fontsize=30) #mengatur label sumbu y
ax.set_xlabel("Total Sales", fontsize=30) #mengatur label sumbu x
ax.tick_params(axis='y', labelsize=20) #mengatur ukuran label sumbu y
ax.tick_params(axis='x', labelsize=15) #mengatur ukuran label sumbu x

st.pyplot(fig) #menampilkan plot

st.caption('Copyright (c) Bangkit Acadeny 2024 by Gabriel Somoal')