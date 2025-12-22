import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Venda de Veículos nos EUA: dados')

car_data = pd.read_csv('vehicles.csv') # lendo os dados
hist_button = st.button('Criar histograma') # criar um botão

if hist_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    
    # criar um histograma
    hist_fig = px.histogram(
        car_data,
        x="odometer",
        title="Distribuição da Quilometragem"
    )

    st.plotly_chart(hist_fig, use_container_width=True)
    
    #criar gráfico de dispersão
    hist_fig = px.histogram(
        car_data,
        x="odometer",
        title="Distribuição da Quilometragem"
    )

    st.plotly_chart(hist_fig, use_container_width=True)

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
