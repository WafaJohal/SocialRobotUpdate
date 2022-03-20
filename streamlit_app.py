import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode
import pycountry
import altair as alt
import altair_catplot
import seaborn as sns
import matplotlib.pyplot as plt

header_container = st.container()
dataset_container =  st.container()

analysis_container = st.container()

data_anno = pd.read_excel('CrossRef_DataFrame_wAnno_socedu.xlsx', sheet_name = 'compressed')
data_6dim = pd.read_excel('6-dimensions-for-website-2015-08-16.xls',sheet_name='sheet1')


countries = {}
for country in pycountry.countries:
    countries[country.name] = country.alpha_3

data_anno['iso_a3'] = [countries.get(country, 'Unknown code') for country in data_anno['Country']]

data_anno.loc[data_anno['Country']== 'Republic of Korea','iso_a3'] = 'KOR'
data_anno.loc[data_anno['Country']== 'South Korea','iso_a3'] = 'KOR'
data_anno.loc[data_anno['Country']== 'USA','iso_a3'] = 'USA'
data_anno.loc[data_anno['Country']== 'Taiwan','iso_a3'] = 'TWN'
data_anno.loc[data_anno['Country']== 'Czech Rep','iso_a3'] = 'CZE'
data_anno.loc[data_anno['Country']== 'The Netherlands','iso_a3'] = 'NLD'
data_anno.loc[data_anno['Country']== 'Iran','iso_a3'] = 'IRN'
data_anno.loc[data_anno['Country']== 'UK','iso_a3'] = 'GBR'

data_6dim.rename(columns={'ctr':'iso_a3'},inplace=True)
#st.write(data_6dim)

cultural_data = pd.merge(data_anno,data_6dim,on="iso_a3",how='left')

def aggrid_interactive_table(df: pd.DataFrame):
    """Creates an st-aggrid interactive table based on a dataframe.

    Args:
        df (pd.DataFrame]): Source dataframe

    Returns:
        dict: The selected row
    """
    options = GridOptionsBuilder.from_dataframe(
        df, enableRowGroup=True, enableValue=True, enablePivot=True
    )

    options.configure_side_bar()

    options.configure_selection("single")
    selection = AgGrid(
        df,
        enable_enterprise_modules=True,
        gridOptions=options.build(),
        theme="light",
        update_mode=GridUpdateMode.MODEL_CHANGED,
        allow_unsafe_jscode=True,
    )

    return selection

with header_container:
    st.title("Social Robots in Education")
    st.text("""This webpage shows the analysis for Cultural Social robots in Education
    """)

with dataset_container:
    st.header('Loading the dataset')

    selection = aggrid_interactive_table(df=cultural_data)

    if selection:
        st.write("You selected:")
        st.json(selection["selected_rows"])
    

with analysis_container:
    st.header(" Individualism and Nb of Participants")

    fig = sns.catplot(x='students_nb',
            y='idv', 
            data=cultural_data,
            height=4,
            aspect=1.5,
            kind='boxen')
    st.pyplot(fig)

    st.header("Interactive analysis")

    list_of_cultural_dim = data_6dim.columns[2:]
    list_of_soroed_dim = data_anno.columns
    cultural_dim = st.selectbox("Select a Cultural Dimension", list_of_cultural_dim)
    soroed_dim = st.selectbox("Select a Social Robot iin Education Dimension", list_of_soroed_dim)


    fig = sns.catplot(x=soroed_dim,
            y=cultural_dim, 
            data=cultural_data,
            height=4,
            aspect=1.5,
            kind='boxen')
 
    st.pyplot(fig)


st.write()