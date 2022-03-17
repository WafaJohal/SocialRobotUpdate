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
    st.title("Social Robots in Education")
    st.text("""This webpage shows teh analysis for Cultural Social robots in Education
    """)

st.write()