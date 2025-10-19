import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title='Formulario', page_icon=':bar_chart', layout='centered')


import os

path = os.path.join(os.getcwd(), 'dados', 'dataset.xlsx')
df = pd.read_excel(path)

with st.expander('Clique aqui para ver os dados'):
    st.dataframe(df, hide_index=True)

dic = {}

if 'keep' not in st.session_state:
    st.session_state.keep = []

with st.container():
    st.markdown('# Formulário')
    for col in df.columns.tolist():
        if col == 'Carimbo de data/hora':
            dic[col] = datetime.now()
            #dic[col] = pd.to_datetime(dic[col])
        else:
            dic[col] = st.selectbox(f'{col}: ', options=df[col].unique())
    #st.session_state.keep.append(dic)
    if st.button('Adicionar ao banco de dados'):
        st.session_state.keep.append(dic)
        st.dataframe(st.session_state.keep)




