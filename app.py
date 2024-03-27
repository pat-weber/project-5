import streamlit as st
import pandas as pd
import plotly_express as px

st.header('Quilometragem de carros usados')

car_data = pd.read_csv('/Users/User/Documents/DS/project-5/vehicles.csv')

hist_button = st.button('Criar histograma') # criar um botão
     
if hist_button: # se o botão for clicado
         # escrever uma mensagem
         st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
         
         # criar um histograma
         fig = px.histogram(car_data, x="odometer")
     
         # exibir um gráfico Plotly interativo
         st.plotly_chart(fig, use_container_width=True)

graph_button = st.button('Criar gráfico de dispersão') # criar um botão

if graph_button: # se o botão for clicado
         # escrever uma mensagem
         st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
         
         # criar um gráfico de dispersão
         fig = px.scatter(car_data, x="odometer", y="price")
     
         # exibir um gráfico Plotly interativo
         st.plotly_chart(fig, use_container_width=True)
