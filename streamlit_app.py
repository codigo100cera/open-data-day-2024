# Escreva o seu codigo aqui
import streamlit as st
import pandas as pd
import plotly.express as px

from pathlib import Path

st.set_page_config(page_title='Open Data Day 2024', page_icon=':sunglasses:', layout='wide')

st.title('OPEN DATA DAY 2024')
st.subheader('Meu Primeiro Dashboard :sunglasses:')


summary_file = Path() / 'data/processed/summary_recursos_disponiveis.pkl'

df = pd.read_pickle(summary_file)

ano_selecionado = st.sidebar.selectbox('Selecione o ano:', df['Ano'].unique(), index=1)

dados = df[df['Ano'].isin([ano_selecionado])]

with st.expander(f'Recursos Disponíveis para os ODS {ano_selecionado}'):
    st.dataframe(dados, use_container_width=True, hide_index=True)

fig = px.pie(dados, names='Objetivo', values='Valor', title=f'Recursos Disponíveis dos ODS {ano_selecionado}')
st.plotly_chart(fig, use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.plotly_chart(fig, use_container_width=True)

