import streamlit as st
import pandas as pd
from datetime import datetime
from pathlib import Path

st.set_page_config(page_title='Formulario', page_icon=':bar_chart', layout='centered')


DATA_FILENAME = Path(__file__).parent/'dados/dataset.xlsx'
@st.cache_data
def get_df_data():
    """Grab GDP data from a CSV file.

    This uses caching to avoid having to read the file every time. If we were
    reading from an HTTP endpoint instead of a file, it's a good idea to set
    a maximum age to the cache with the TTL argument: @st.cache_data(ttl='1d')
    """

    # Instead of a CSV on disk, you could read from an HTTP endpoint here too.
    DATA_FILENAME = Path(__file__).parent/'dados/dataset.xlsx'
    df = pd.read_excel(DATA_FILENAME)
    return df
df = get_df_data()

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













