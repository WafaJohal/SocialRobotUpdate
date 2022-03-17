import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode
import streamlit_wordcloud as st_wordcloud
import nltk
nltk.download('punkt')
nltk.download('stopwords')


header_container = st.container()
wordcloud_container = st.container()
dataset_container =  st.container()

with header_container:
    st.title("HRI Questionnaires")
    st.text("""This webpage is meant to navigate and search for previously used questionnaire in HRI.
    It is based in data from https://zenodo.org/record/5789410#.Ydc98WjMKUk%20%5B1%5D.
    """)

st.write()