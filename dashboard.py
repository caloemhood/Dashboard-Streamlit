import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


merged_df = pd.read_csv('all_data.csv')
st.set_page_config(
    page_title="Product Analysis",
)

# Pilihan menu di sidebar
selected = st.sidebar.radio('Select Option', ['Analisis Tren Penjualan', 'Pengaruh Rating Produk dan Penjualan'])
# Menampilkan konten sesuai pilihan di sidebar
if selected == 'Analisis Tren Penjualan':
  # Analisis Tren Penjualan Waktu ke Waktu
# Calculate monthly sales
    monthly_sales = merged_df.groupby(pd.to_datetime(merged_df['sales_x']).dt.to_period('M')).size()

# Plot monthly sales using Streamlit
    st.line_chart(monthly_sales)

# Add title and labels
    st.title('Tren Penjualan Keseluruhan dari Waktu ke Waktu')
    st.xlabel('Tanggal')
    st.ylabel('Total Penjualan')
