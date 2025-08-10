import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title='Startup Analysis',layout='wide')

df  = pd.read_csv("D:\Campus X\Pandas\Streamlit_App\startup_cleaned.csv")
# st.dataframe(df)

# data cleaning
# df['Investors Name'] = df['Investors Name'].fillna('Undisclosed')
df['date'] = pd.to_datetime(df['date'],errors='coerce')
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

def load_investor_details(selected_investor):
    st.title(selected_investor)
    # load recent 5 investments 
    st.subheader('Most recent investments')
    st.dataframe(df[df['investors'].str.contains(selected_investor)].head()[['date','startup','vertical','city','round','amount']])
    
    # biggest investments 
    
    big_series = df[df['investors'].str.contains(' IDG Ventures')].groupby('startup')['amount'].max().sort_values(ascending=False).head()

    col1,col2 = st.columns(2)
    with col1:
        st.subheader('Biggest Investments')
        fig,ax = plt.subplots()
        ax.bar(big_series.index,big_series.values)
        st.pyplot(fig)
    
    with col2:
        st.subheader('Sectors Invested in')
        vertical_series = df[df['investors'].str.contains(selected_investor)].groupby('vertical')['amount'].sum()
        
        fig1,ax1 = plt.subplots()
        ax1.pie(vertical_series,labels=vertical_series.index,autopct="%0.01f%%")
        
        st.pyplot(fig1)


    col5,col3,col4 = st.columns(3)
    
    with col5:
        st.subheader('YOY investment Graph')
        year_series = df[df['investors'].str.contains(selected_investor)].groupby('year')['amount'].sum()
        fig5,ax5 = plt.subplots()
        ax5.plot(year_series.index,year_series.values)
        st.pyplot(fig5)
    
    with col3:
        st.subheader('Rounds invested in')
        round_series =df[df['investors'].str.contains(selected_investor)].groupby('round')['amount'].sum()
        fig3,ax2 =plt.subplots()
        ax2.pie(round_series,labels=round_series.index,autopct='%0.01f%%')
        st.pyplot(fig3)
        
    with col4:
        st.subheader('Cities Invested in')
        city_series = df[df['investors'].str.contains(selected_investor)].groupby('city')['amount'].sum()
        fig4,ax4 = plt.subplots()
        ax4.pie(city_series,labels=city_series.index,autopct='%0.01f%%')
        st.pyplot(fig4)
        
    st.header('Similar Investors')
    s_investor = df[df['investors'].str.contains(selected_investor)]['investors'].values[0]
    for investor in str(s_investor).split(", "):
        st.markdown(f" - {investor}")


    

        
def load_overall_analysis():
    # total invested amount
    st.title('Overall Analysis')
    total_money = round(df['amount'].sum())
    
    max_funding = df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]
     
    
    average_funding = round(df.groupby('startup')['amount'].sum().mean())
     
    total_funded_startup = df['startup'].nunique() 
    
    col1,col2,col3,col4 = st.columns(4)
    
    with col1:
        st.metric('Total',str(total_money)+' Cr')
     
     
    with col2:
        st.metric('Maximum',str(round(max_funding))+' Cr')
        
    with col3:
        st.metric('Average',str(average_funding)+' Cr')
    
    with col4:
        st.metric('Total Startup(funded)',str(total_funded_startup)+' Cr')
    
    
    col5,col6,col7 = st.columns(3)
    with col5:
        st.header('MoM Graph')
        selected_option = st.selectbox('Select Type',['Total','Count'])
        if selected_option == 'Total':
            tmp_df = df.groupby(['year','month'])['amount'].sum().reset_index()
        else:
            tmp_df = df.groupby(['year','month'])['amount'].count().reset_index()
        tmp_df['x_axis'] = tmp_df['month'].astype('str') + '-' + tmp_df['year'].astype('str')
        fig,ax = plt.subplots()
        ax.plot(tmp_df['x_axis'],tmp_df['amount'])
        st.pyplot(fig)
        
    with col6:
        st.header('Sector Analysis')
        option = st.selectbox('Select Type',['Count','Sum'])
        if option == 'Count':
            count_of_sectors_invested = df.groupby('vertical')['amount'].count().sort_values(ascending=False).head(10)
        else:
            count_of_sectors_invested = df.groupby('vertical')['amount'].sum().sort_values(ascending=False).head(20)
        fig1,ax1 = plt.subplots()
        ax1.pie(count_of_sectors_invested,labels=count_of_sectors_invested.index,autopct='%0.01f%%')
        st.pyplot(fig1)
    
    with col7:
        st.header('Type of Funding')
        st.header('')
        round_funding_count  = df.groupby('round')['round'].count().head()
        fig2,ax2 = plt.subplots()
        ax2.pie(round_funding_count,labels=round_funding_count.index,autopct='%0.01f%%')
        st.pyplot(fig2)
        
    col8,col9 = st.columns(2)
    with col8:
        st.header('Total investment on Cities')
        cities_investment = df.groupby(['city'])['amount'].sum().sort_values(ascending=False).head(10)
        fig3,ax3 = plt.subplots()
        ax3.bar(cities_investment.index,cities_investment.values)
        st.pyplot(fig3)
    
    with col9:
        st.header('Top Startups')
        toselect = st.selectbox('Select Type',['Overall','Yearly'])
        if toselect == 'Yearly':
            year = st.selectbox('Select Year',list(df['year'].unique()))
            yearly_data = df[df['year']==year].groupby(['year','startup'])['amount'].sum().sort_values(ascending=False).head(5)
            st.dataframe(yearly_data)
        else:
            overall = df.groupby(['startup'])['amount'].sum().sort_values(ascending=False).head(5)
            st.dataframe(overall)
        
    
    
    
    
def load_startup_details(startup):
    st.header(startup)   
    
    industry_name = df[df['startup']==startup]['vertical'].values[0]
    subindustry_name = df[df['startup']==startup]['subvertical'].values[0]
    location = df[df['startup']==startup]['city'].values[0]
    
    col0,col1,col2 = st.columns(3)
    
    with col0:
        st.subheader('Location')
        st.markdown(f"- #### {location}")
    
    with col1:
        st.subheader('Industry')
        st.markdown(f"- #### {industry_name}")
            
    with col2:
        st.subheader('Sub Industry')
        st.markdown(f"- #### {subindustry_name}")
        
    # st.table(df.head())
    st.header('Funding Round')
    st.dataframe(df[df['startup']==startup].groupby(['investors','date','round'])['amount'].sum().reset_index())
        
        
    st.header('Similar Startups')
    
    vertical = df[df['startup']==startup]['vertical'].values[0]
    subvertical = df[df['startup']==startup]['subvertical'].values[0]
    similar_startups = df[(df['vertical']==vertical) | (df['subvertical']==subvertical)]['startup'].head().values
    for strtups in similar_startups:
        if strtups != startup:
            st.write(strtups)

        
st.sidebar.title('Startup Funding Analysis')

option = st.sidebar.selectbox('Select one',['Overall Analysis','Startup','Investor'])

if option == 'Overall Analysis':
    # btn0 = st.sidebar.button("Show overall Analysis")
    # if btn0:
    load_overall_analysis()
    
elif option == 'Startup':
    startup = st.sidebar.selectbox('Select Startup',sorted(df['startup'].unique().tolist()))
    btn1 = st.sidebar.button('Find Startup Details')
    if btn1:
        load_startup_details(startup)
    
elif option == 'Investor':
    selected_investor = st.sidebar.selectbox('Select Invester',sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Investor Details')
    if btn2:
        load_investor_details(selected_investor)
    # st.title('Inverstor Analysis')