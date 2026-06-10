import plotly.express as px
import streamlit as st
import pandas as pd

df = pd.read_csv('vehicles_us.csv')

hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)


build_scatter = st.checkbox('Criar um gráfico de dispersão')

if build_scatter:
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    fig_2 = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig_2, use_container_width=True)
