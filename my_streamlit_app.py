from os import write
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd

#LAYOUT
st.set_page_config(layout="wide")

#DATA
cars_df= pd.read_csv("https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv")

us_cars = cars_df.loc[cars_df['continent'] == ' US.']
eu_cars = cars_df.loc[cars_df['continent'] == ' Europe.']
jp_cars = cars_df.loc[cars_df['continent'] == ' Japan.']

#VIZ
config = {'displayModeBar': False} # nascondere la barra di plotly


#BANNER HEADER
col1, col2, col3= st.columns([3,1,3])
with col1:
    st.write("")
with col2:
    st.image("https://github.com/ChristianPolito/streamlitTest/blob/main/Fichier%201.png?raw=true")
with col3:
    st.write("")

#INTRO
st.write("Exercise to understand the use of STREAMLIT")
st.write('## EDA on a database with information about cars from US, Europe and Japan')
st.markdown("""---""")
st.write('Below you will find the data at my disposal for the realization of this exercise, in the sidebar you have the possibility to filter the data by country.')

#SIDEBAR RADIO
st.sidebar.image("https://github.com/ChristianPolito/streamlitTest/blob/main/Fichier%201mdpi.png?raw=true")
country = st.sidebar.radio(
     "Select a country:",
     ('All', 'US', 'Europe', 'Japan'))

#DATAFRAME

if country == 'US':
    st.write("You have selected the data for US ")
    st.dataframe(us_cars)   
elif country == 'Europe':
    st.write("You have selected the data for Europe ")
    st.dataframe(eu_cars)   
elif country == 'Japan':
    st.write("You have selected the data for Japan ")
    st.dataframe(jp_cars)
else:
    st.write("You have selected the data for all the countries")
    st.dataframe(cars_df)

st.markdown("""---""")
#DISTRIBUTION VIZ
st.header("Distribution Analysis ")

col1, col2 = st.columns([2,2])

with col1:
    viz_total_cars = px.histogram(cars_df, x = "continent", title="Cars produced by country ").update_layout(xaxis={"dtick":1},bargap=0.2)
    st.plotly_chart(viz_total_cars,config = config, use_container_width = True)


col1, col2 = st.columns([2,2])

with col1:
    viz_year1 = px.box(cars_df, x = "continent", y="year", title="Years of production by continent")
    st.plotly_chart(viz_year1,config = config, use_container_width = True)

with col2:
    if country == 'US':
        viz_year1 = px.histogram(us_cars, x = "year", title="Number of cars produced per year in the US").update_layout(xaxis={"dtick":1},bargap=0.2)
        st.plotly_chart(viz_year1,config = config, use_container_width = True)

    if country == 'Europe':
        viz_year1 = px.histogram(eu_cars, x = "year", title="Number of cars produced per year in Europe").update_layout(xaxis={"dtick":1},bargap=0.2)
        st.plotly_chart(viz_year1,config = config, use_container_width = True)

    if country == 'Japan':
        viz_year1 = px.histogram(jp_cars, x = "year", title="Number of cars produced per year in Japan").update_layout(xaxis={"dtick":1},bargap=0.2)
        st.plotly_chart(viz_year1,config = config, use_container_width = True)

    if country == 'All':
        viz_year1 = px.histogram(cars_df, x = "year", title="Number of cars produced per year").update_layout(xaxis={"dtick":1},bargap=0.2)
        st.plotly_chart(viz_year1,config = config, use_container_width = True)


st.write('The first analysis shows that the US is over-represented with 162 cars.\
The years of production considered range from 1971 to 1983 for all countries with a higher concentration between 1974 and 1981.')
st.markdown("""---""")

#CORRELATION VIZ
st.header("Correlation analysis")

def heatmapgraf(df, tit="Number of cars produced per year"):    
    heat_map = px.imshow(df.corr(), color_continuous_scale='RdBu_r', title=tit)
    return st.plotly_chart(heat_map,config = config, use_container_width = True)

if country == 'US':
    dfheat = us_cars
    heatmapgraf(dfheat, tit="Number of cars produced per year in the US")

if country == 'Europe':
    dfheat = eu_cars
    heatmapgraf(dfheat, tit="Number of cars produced per year in Europe")

if country == 'Japan':
    dfheat = jp_cars
    heatmapgraf(dfheat, tit="Number of cars produced per year in Japan")

if country == 'All':
    dfheat = jp_cars
    heatmapgraf(dfheat, tit="Number of cars produced per year for all the countries")


st.write("It is clear from the correlation heatmap that there is a strong positive correlation between hp and cubic centimeters. There is also a strong negative correlation between time-to-60 and hp.\
The strongest correlations are visible for the US cars while for the European cars the correlations are the same but lose intensity.")

