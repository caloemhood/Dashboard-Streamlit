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
    merged_df['order_purchase_timestamp'] = pd.to_datetime(merged_df['order_purchase_timestamp'])
# Calculate monthly sales
    monthly_sales = merged_df.groupby(pd.to_datetime(merged_df['order_purchase_timestamp']).dt.to_period('M')).size()

# Plot monthly sales using Streamlit
    st.line_chart(monthly_sales)

# Add title and labels
    st.title('Tren Penjualan Keseluruhan dari Waktu ke Waktu')
    st.ylabel('Total Penjualan')

# Create scatter plot using Streamlit
st.scatter_chart(merged_df[['review_score', 'sales']])

# Add labels and title
st.ylabel('Jumlah Penjualan')
st.title('Hubungan antara Rating Produk dan Jumlah Penjualan')
