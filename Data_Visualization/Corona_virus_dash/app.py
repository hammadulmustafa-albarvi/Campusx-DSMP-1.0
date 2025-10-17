import numpy as np
import pandas as pd
import plotly.graph_objs as go 
import dash
from dash import html,dcc
import plotly.express as px
from dash import Input, Output



external_stylesheets = [
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]



app = dash.Dash(__name__,external_stylesheets=external_stylesheets)

app.layout = html.H1('Hello World',style={'color':'white'})

patients = pd.read_csv('D:\Campus X\Data Visualization\Corona_virus_dash\IndividualDetails.csv')

total = patients.shape[0]

hospitalized = patients['current_status'].value_counts()[0]

recovered = patients['current_status'].value_counts()[1]

deaths =  patients['current_status'].value_counts()[2]


options = [
    {'label':'All','value':'All'},
    {'label':'Hospitalized','value':'Hospitalized'},
    {'label':'Recovered','value':'Recovered'},
    {'label':'Deceased','value':'Deceased'}
]

app.layout = html.Div([ 
                       html.H1('corona virus pandemic',style={'color':'white','text-align':'center'}),
                       html.Div([
                           
                           html.Div([ 
                               html.Div([
                                   html.Div([
                                       html.H3('Total Cases',className='text-light'),
                                       html.H4(total,className='text-light')
                                       ],className='card-body')
                                   ],className='card bg-danger') 
                               ],className='col-md-3'), 
                           html.Div([  
                               
                               html.Div([
                                   html.Div([
                                       html.H3('Active Cases',className='text-light'),
                                       html.H4(hospitalized,className='text-light')
                                       ],className='card-body')
                                   ],className='card bg-info')
                               
                               ],className='col-md-3'),
                           html.Div([
                               
                               html.Div([
                                   html.Div([
                                       html.H3('Recovered',className='text-light'),
                                       html.H4(recovered,className='text-light')
                                       ],className='card-body')
                                   ],className='card bg-warning')
                               
                               ],className='col-md-3'),
                           html.Div([
                               
                               html.Div([
                                   html.Div([
                                       html.H3('Deaths',className='text-light'),
                                       html.H4(deaths,className='text-light')
                                       ],className='card-body')
                                   ],className='card bg-success')
                               
                               ],className='col-md-3')
                           
                           ],className='row'),
                       html.Div([],className='row'),
                       
                       html.Div([
                           
                           html.Div([
                               
                               html.Div([
                                   
                                   html.Div([
                                       
                                       dcc.Dropdown(id='picker',options=options,value='All'),
                                       
                                       dcc.Graph(id='bar-chart') 
                                       
                                       ],className='card-body')
                                   
                                   ],className='card')
                               
                               ],className='col-md-12')
                           
                           ],className='row')
                       
                       ],className='container')

@app.callback(Output('bar-chart','figure'),[Input('picker','value')])
def update_graph(type):
    if type == 'All':
        patients_bar = patients['detected_state'].value_counts().reset_index() 
        return {
            'data':[go.Bar(x=patients_bar['detected_state'],y=patients_bar['count'])],
            'layout':go.Layout(title='Bar plot')
        }
    else:
        patients_bar1 = patients[patients['current_status']==type]['detected_state'].value_counts().reset_index()
        return {
            'data':[go.Bar(x=patients_bar1['detected_state'],y=patients_bar1['count'])],
            'layout':go.Layout(title='State total count')
        }

if __name__ == '__main__':
  app.run(debug=True)