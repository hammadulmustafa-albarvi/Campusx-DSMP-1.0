import streamlit as st
import numpy as np 
import pandas as pd
import plotly.express as px


df = pd.read_csv('D:\Campus X\Data Visualization\Plotly_project\india.csv')
states = df['State'].unique().tolist()
states.insert(0,'Overall India')

st.set_page_config(layout='wide')






st.sidebar.title('India Map')
selected_state = st.sidebar.selectbox('Select State',states)
primary = st.sidebar.selectbox('Select Primary Parameter', df.columns[5:].to_list())
secondary =st.sidebar.selectbox('Select Secondary Parameter', df.columns[5:].to_list()) 
plot = st.sidebar.button('Plot Graph')

if plot:
    if selected_state == 'Overall India':
        fig = px.scatter_map(df, lat="Latitude", lon="Longitude",size=primary,color=secondary, color_continuous_scale='Inferno',zoom=3,height=600,hover_name='District') 
        st.plotly_chart(fig,use_container_width=True)
    else:
        state = df[df['State']==selected_state]
        fig = px.scatter_map(state, lat="Latitude", lon="Longitude",size=primary,color=secondary, color_continuous_scale='Inferno',zoom=3,height=600,hover_name='District') 
        st.plotly_chart(fig,use_container_width=True)  