import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Analyse Avancée", page_icon=":eyeglasses:")

st.markdown("# 📈 Analyse Avancée")

sales = pd.read_csv('superstore.csv', parse_dates=['Ship Date', 'Order Date'])
sales.rename(columns={"Order Date": "Order_Date"}, inplace=True)

# Statistiques descriptives
st.write("## 🔍 Statistiques générales")
st.write(sales.describe())

# Histogramme des ventes
fig_hist = px.histogram(sales, x='Sales', title="Répartition des ventes")
fig_hist.update_traces(hovertemplate="<b>Ventes :</b> %{x} <br><b>Nombre :</b> %{y}")

st.plotly_chart(fig_hist, use_container_width=True)
