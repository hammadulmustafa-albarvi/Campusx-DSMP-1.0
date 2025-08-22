import streamlit as st 
import pandas as pd
import numpy as np
from helper import * 
import matplotlib.pyplot as plt
import seaborn as sns
startup = pd.read_csv("D:\Campus X\My_projects\investments_VC.csv",encoding='latin1')
investor = pd.read_csv('crunchbase-investments.csv',encoding='latin1')
# df = pd.read_csv('investments_VC.csv', encoding='latin1', engine='python', on_bad_lines='skip')
# df = df.iloc[:49438]

investor.rename(columns={'company_name':'name'},inplace=True)
df = investor.merge(startup,on='name')
df.dropna(subset=['name'],inplace=True)

df.columns = df.columns.str.strip()
st.set_page_config(layout='wide')




df['Country'] = df['country_code'].apply(full_country_name)

df['funding_total_usd'] = df['funding_total_usd'].str.replace(',','').replace(' -   ','0')
df['funding_total_usd'] = df['funding_total_usd'].astype(np.float64)



df['first_funding_at'] = pd.to_datetime(df['first_funding_at'], errors='coerce')






















st.sidebar.title('Startup Data Analysis')

option = st.sidebar.selectbox('Select Option',['Overall Analysis','Startup Analysis','Investor Analysis'])

if option == 'Overall Analysis':
    st.title('Overall Analysis by Country')
    
    
    country = st.selectbox('Select a Country for Analysis',sorted(df['Country'].dropna().unique().tolist()))
    col1,col2,col3 = st.columns(3)
    with col1:
        st.metric('Total Funded Amount in $',str(round(df[df['Country'] == country].groupby('Country')['funding_total_usd'].sum().values[0]/1000000))+" M")

    with col2:
        st.metric('Total Number of Startups',df[df['Country'] == country].groupby('Country')['name'].count().values[0])
        
    
    with col3:
        st.metric('Total Number of Funded Startups',df[(df['Country'] == country) & (df['funding_total_usd']!= 0)].count().values[0])
        
        
    
    
    st.header('')
    
    col6,col7 = st.columns(2)
    with col6:
        st.header('Top 5 Startups')
        top_5 = df[df['Country']==country].groupby('name')['funding_total_usd'].sum().sort_values(ascending=False).head().index.tolist()
        for i in top_5:
            st.markdown(f'- {i}')
    
    
    with col7:
        st.header('Top 5 Startups according to Funding')
        top_5_plot = df[df['Country']==country].groupby('name')['funding_total_usd'].sum().sort_values(ascending=False).head().reset_index()
        fig,ax = plt.subplots()
        ax.bar(top_5_plot['name'],top_5_plot['funding_total_usd'])
        plt.xticks(rotation=90)
        st.pyplot(fig)
        
    
    
    fig,ax = plt.subplots(nrows=1,ncols=2)
    ax[0].pie(df[df['Country'] == country]['market'].value_counts().head(10),labels=df[df['Country'] == country]['market'].value_counts().head(10).index,autopct='%0.1f%%', textprops={'fontsize': 5})
    ax[1].pie(df[df['Country'] == country]['status'].value_counts().head(10),labels=df[df['Country'] == country]['status'].value_counts().head(10).index,autopct='%0.1f%%', textprops={'fontsize': 5})
    ax[0].set_title('Most frequent startup market sectors')
    ax[1].set_title('Status of Startups')
    plt.subplots_adjust(wspace=0.8)
    plt.xticks(fontsize=8)
    st.pyplot(fig)
        
        
        
    col4,col5 = st.columns(2)
    with col5:
        st.header('Cities with the highest funding')
        funding_by_city = df[df['Country']==country].groupby('city')['funding_total_usd'].sum().sort_values(ascending=False).reset_index().head(10)
        fig,ax=plt.subplots()
        ax.bar(funding_by_city['city'],funding_by_city['funding_total_usd'])
        plt.xticks(rotation=90)


        st.pyplot(fig)
        
    
    # col6,col7 = st.columns(2)
    
    with col4:
        st.header('Total funding by Year')
        first_funding = df[df['Country']==country].groupby('first_funding_at')['funding_total_usd'].sum().reset_index()
        fig,ax = plt.subplots()
        ax.scatter(first_funding['first_funding_at'],first_funding['funding_total_usd'])
        plt.yscale('log')
        st.pyplot(fig)
    
    

    
    
    
    
    
    
elif option == 'Startup Analysis':
    
    country = st.sidebar.selectbox('Select Country',sorted(df['Country'].dropna().unique().tolist()))
    startup = st.sidebar.selectbox('Select Startup',sorted(df[df['Country']==country]['name'].values.tolist()))

    st.header(f'{startup} Analysis')


    col1,col2,col3,col4 = st.columns(4)
    
    with col1:
        st.metric('Market',df[df['name']==startup]['market'].values[0])

    with col2:
        st.metric('Total Funding',f'${int((df[df['name']==startup]['funding_total_usd'].values[0])/1000000)} M')

    with col3:
        st.metric('Status',df[df['name']==startup]['status'].values[0])
        
    with col4:
        st.metric('Region',df[df['name']==startup]['region'].values[0])

    st.header('')
    col5,col6=st.columns(2)
    with col5:
        st.header('Funding share by round A to H')
        fig,ax = plt.subplots()
        if df[df['name']==startup][['round_A','round_B','round_C','round_D','round_E','round_F','round_G','round_H']].values[0].sum() != 0:
            ax.pie(df[df['name']==startup][['round_A','round_B','round_C','round_D','round_E','round_F','round_G','round_H']].values[0],labels = df[df['name']==startup][['round_A','round_B','round_C','round_D','round_E','round_F','round_G','round_H']].columns,autopct='%0.1f%%')
            st.pyplot(fig)
        else:
            st.header('No funding Round Data Found')

    with col6:
        st.header('Other Fundings')
        fig,ax=plt.subplots()
        ax.bar(df[df['name']==startup][['seed','venture','equity_crowdfunding','undisclosed','convertible_note','debt_financing','angel','grant','product_crowdfunding']].columns,df[df['name']==startup][['seed','venture','equity_crowdfunding','undisclosed','convertible_note','debt_financing','angel','grant','product_crowdfunding']].values[0])
        plt.xticks(rotation=90)
        st.pyplot(fig)

    st.header('Funding accross Years')
    fig,ax = plt.subplots(figsize = (4,3))
    ax.plot(pd.date_range(df[df['name']==startup]['first_funding_at'].values[0],df[df['name']==startup]['last_funding_at'].values[0],periods=17),df[df['name']==startup][['seed','venture','equity_crowdfunding','undisclosed','convertible_note','debt_financing','angel','grant','product_crowdfunding','round_A','round_B','round_C','round_D','round_E','round_F','round_G','round_H']].values[0])
    plt.xticks(rotation=45)
    st.pyplot(fig)
    
    
    
    
    
    
    
elif option == 'Investor Analysis':
    country = st.sidebar.selectbox('Select Country',sorted(df['Country'].dropna().unique().tolist()))
    investor_name = st.sidebar.selectbox('Select Investor',sorted(df[df['Country']==country]['investor_name'].unique().tolist()))
    st.title(f'{investor_name} Analysis')
    
    col1,col2,col3 = st.columns(3)
    
    with col1:
        try:
            st.metric('Total Invested Money',f'$ {round(df[df['investor_name'] == investor_name]['raised_amount_usd'].sum())/1000000} M')
        except:
            st.write('Data Not Found')
        
    with col2:
        try:
            st.metric('Investor Category',df[df['investor_name'] == investor_name]['investor_category_code'].unique()[0].capitalize())
        
        except:
            st.write('Data Not Found')
        
    with col3:
        
        try:
            st.metric('Investor origin',df[df['investor_name'] == investor_name]['investor_city'].unique()[0].capitalize())
        
        except:
            st.write('Data Not Found')
            
    
    st.header('')
            

    
    # with col4:
    st.header('Investment in Years in USD')
    fig,ax = plt.subplots(figsize=(18,6))
    sns.lineplot(df[df['investor_name'] == investor_name],x='funded_at',y='raised_amount_usd',ax=ax)
    plt.xticks(rotation=55)
    st.pyplot(fig)
    
    
    st.header('')
    col4,col5,col6 = st.columns(3)
    
    
    with col4:
        
        st.header('Funding Round Type')
        try:
            fig,ax = plt.subplots()
            plt.pie(df[df['investor_name'] == investor_name]['funding_round_type'].value_counts().values,labels=df[df['investor_name'] == investor_name]['funding_round_type'].value_counts().index,autopct='%0.1f%%')
            st.pyplot(fig) 

        except:
            st.header('Data Not Found')
            
    with col5:
        st.header('Funded Companies')
        
        try:
            fig,ax = plt.subplots()
            plt.pie(df[df['investor_name'] == investor_name]['name'].value_counts().values,labels=df[df['investor_name'] == investor_name]['name'].value_counts().index,autopct='%0.1f%%')
            st.pyplot(fig)
        except:
            st.header('Data Not Found')

    with col6:
        st.header('Invested Category')
        try:
            fig,ax = plt.subplots()
            plt.pie(df[df['investor_name'] == investor_name]['investor_category_code'].value_counts().values,labels=df[df['investor_name'] == investor_name]['investor_category_code'].value_counts().index,autopct='%0.1f%%')
            st.pyplot(fig)
        except:
            st.header('Data Not Found')
