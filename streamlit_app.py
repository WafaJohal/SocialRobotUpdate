import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode
import nltk
import re
import pycountry
import altair as alt
import altair_catplot
import seaborn as sns
import matplotlib.pyplot as plt

header_container = st.container()
dataset_container =  st.container()
wordcloud_container = st.container()
analysis_container = st.container()

data_anno = pd.read_excel('CrossRef_DataFrame_wAnno_socedu.xlsx', sheet_name = 'compressed')
data_anno_all = pd.read_excel('CrossRef_DataFrame_wAnno_socedu.xlsx', sheet_name = 'Sheet2')
data_6dim = pd.read_excel('6-dimensions-for-website-2015-08-16.xls',sheet_name='sheet1')


countries = {}
for country in pycountry.countries:
    countries[country.name] = country.alpha_3

data_anno['iso_a3'] = [countries.get(country, 'Unknown code') for country in data_anno['Country']]
data_anno_all['iso_a3'] = [countries.get(country, 'Unknown code') for country in data_anno_all['Country']]

data_anno.loc[data_anno['Country']== 'Republic of Korea','iso_a3'] = 'KOR'
data_anno.loc[data_anno['Country']== 'South Korea','iso_a3'] = 'KOR'
data_anno.loc[data_anno['Country']== 'USA','iso_a3'] = 'USA'
data_anno.loc[data_anno['Country']== 'Taiwan','iso_a3'] = 'TWN'
data_anno.loc[data_anno['Country']== 'Czech Rep','iso_a3'] = 'CZE'
data_anno.loc[data_anno['Country']== 'The Netherlands','iso_a3'] = 'NLD'
data_anno.loc[data_anno['Country']== 'Iran','iso_a3'] = 'IRN'
data_anno.loc[data_anno['Country']== 'UK','iso_a3'] = 'GBR'

data_anno_all.loc[data_anno_all['Country']== 'Republic of Korea','iso_a3'] = 'KOR'
data_anno_all.loc[data_anno_all['Country']== 'South Korea','iso_a3'] = 'KOR'
data_anno_all.loc[data_anno_all['Country']== 'USA','iso_a3'] = 'USA'
data_anno_all.loc[data_anno_all['Country']== 'Taiwan','iso_a3'] = 'TWN'
data_anno_all.loc[data_anno_all['Country']== 'Czech Rep','iso_a3'] = 'CZE'
data_anno_all.loc[data_anno_all['Country']== 'The Netherlands','iso_a3'] = 'NLD'
data_anno_all.loc[data_anno_all['Country']== 'Iran','iso_a3'] = 'IRN'
data_anno_all.loc[data_anno_all['Country']== 'UK','iso_a3'] = 'GBR'

data_6dim.rename(columns={'ctr':'iso_a3'},inplace=True)
#st.write(data_6dim)

cultural_data = pd.merge(data_anno,data_6dim,on="iso_a3",how='left')
data_anno_all = pd.merge(data_anno_all,data_6dim,on="iso_a3",how='left')

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

def get_rows_contains_word(df,colname, word):
    contain_values = df[df[colname].str.lower().str.strip().str.contains(word)]
    return contain_values

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
    
# """ with wordcloud_container:
#     st.header("Wordcloud of keywords used in the dataset")
#     text = " ".join(name for name in data_anno_all.abstractNote)
#     # stop words list
    
#     stop = nltk.corpus.stopwords.words('english')
#     list_of_stop_words = ["paper","robot","robots","study","social","human","interaction",
#     "results","participants","people","using","human-robot","robots.","used","data","present","approach","could","based","two","one","learning","children"]

#     list_of_stop_words = st.multiselect("List of words not included in the wordcloud", list_of_stop_words, list_of_stop_words)

#     stop.extend(list_of_stop_words)

#     data_anno_all['abstractNote'] = \
#     data_anno_all['abstractNote'].map(lambda x: re.sub('[,\.!?]', '', x))# Convert the titles to lowercase
#     data_anno_all['abstractNote'] = \
#     data_anno_all['abstractNote'].map(lambda x: x.lower()) 
   

#     # Create and generate a word cloud imagestr.lower().str.strip():
#     data_anno_all.cleanAbs = data_anno_all.abstractNote.str.lower().str.strip().str.split()
#     data_anno_all['Clean'] = data_anno_all.cleanAbs.apply(lambda x: [w.strip() for w in x if w.strip() not in stop])
#     data_anno_all['Clean'] = pd.DataFrame( data_anno_all['Clean'])

    
#     words = data_anno_all.Clean.tolist()
#     flat_list = [item for sublist in words for item in sublist]
#     wdic = [dict(text = i, value = flat_list.count(i)) for i in set(flat_list)]
    

#     wc = st_wordcloud.visualize(words=wdic,tooltip_data_fields={'text': 'text','value': 'value'} , max_words=100) """


with analysis_container:
    st.header(" Individualism and Nb of Participants")

    fig = sns.catplot(x='students_nb',
            y='idv', 
            data=cultural_data,
            height=4,
            aspect=1.5, palette="Set3", order=[1, 2, 'small', 'class'],
            kind='violin')
    #plt.ylim(0,125)
    fig.set_axis_labels("Number of students in front of the robot", "Individualism")
    st.pyplot(fig)
    print(cultural_data.students_nb.unique())



    st.header(" Individualism and Robot Behavioural Design (Communicative vs functional)")

    fig = sns.catplot(x='Communicative gestures vs functional actions',
            y='idv', 
            data=cultural_data,
            height=4,
            aspect=1.5, palette="Set3", order=['FU', 'CO+FU', 'CO', 'CO+D'],
            kind='violin')
    #plt.ylim(0,125)
    fig.set_axis_labels("Communicative gestures vs functional actions", "Individualism")
    st.pyplot(fig)


    st.header(" Power Index and Robot Behavioural Design (Communicative vs functional)")

    fig = sns.catplot(x='Communicative gestures vs functional actions',
            y='pdi', 
            data=cultural_data,
            height=4,
            aspect=1.5, palette="Set3", order=['FU', 'CO+FU', 'CO', 'CO+D'],
            kind='violin')
    #plt.ylim(0,125)
    fig.set_axis_labels("Communicative gestures vs functional actions", "Power")
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
            aspect=1.5,palette="Set3",
            kind='violin')
 
    st.pyplot(fig)


st.write()