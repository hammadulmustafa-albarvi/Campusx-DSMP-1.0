import plotly.graph_objects as go
import pandas as pd
from dash import html,dcc,Input,Output
import dash
import numpy as np

external_stylesheets = [
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]

def age_groups(x):
  x=float(x)
  if 0<x<10:
    return f'0-9'
  elif 10<=x<19:
    return f'10-19' 
  elif 20<=x<29:
    return f'20-29'
  elif 30<=x<39:
    return f'30-39'
  elif 40<=x<49:
    return f'40-49'
  elif 50<=x<59:
    return f'50-59'
  elif 60<=x<69:
    return f'60-69'
  elif 70<=x<79:
    return f'70-79'
  elif x>=80:
    return f'>=80'
  else:
    return f'missing'


df = pd.read_csv('D:\Campus X\Data Visualization\Practice\Dash_corona\IndividualDetails.csv')
total_cases = df.shape[0]
recovered = df[df['current_status']=='Recovered'].shape[0]
hospitalized = df[df['current_status']=='Hospitalized'].shape[0]
deceased = df[df['current_status']=='Deceased'].shape[0]

df['age'] = df['age'].replace(np.nan,0).replace('28-35',0).astype(int)
df['age_groups'] = df['age'].apply(age_groups)


df['diagnosed_date'] = pd.to_datetime(df['diagnosed_date'])
data = df.groupby('diagnosed_date')['id'].count().reset_index()




app = dash.Dash(external_stylesheets=external_stylesheets)


options = [
    
    {'label':'All','value':'All'},
    {'label':'Hospitalized','value':'Hospitalized'},
    {'label':'Recovered','value':'Recovered'},
    {'label':'Deceased','value':'Deceased'}
    
    
]


app.layout=html.Div([
    
    

        
        html.H1('Corona pandemic Analysis',style={'color':'white','text-align':'center'}),
        

    
    html.Div([
        
        html.Div([
            
            html.Div([
                
                html.Div([
                    
                    html.H2('Total Cases',style={'color':'white'}),
                    html.H3(total_cases,style={'color':'white'}),
                    
                    ],className='card-body')
                
                ],className='card bg-danger')
            
            ],className='col-md-3'),
        
        html.Div([
            
            html.Div([
                
                html.Div([
                    
                    html.H2('Active',style={'color':'white'}),
                    html.H3(hospitalized,style={'color':'white'}),
                    
                    ],className='card-body')
                
                ],className='card bg-info')
            
            ],className='col-md-3'),
        
        html.Div([
            
            html.Div([
                
                html.Div([
                    
                    html.H2('Recovered',style={'color':'white'}),
                    html.H3(recovered,style={'color':'white'}),
                    
                    ],className='card-body')
                
                ],className='card bg-warning')
            
            ],className='col-md-3'),
        
        html.Div([
            
            html.Div([
                
                html.Div([
                    
                    html.H2('Deaths',style={'color':'white'}),
                    html.H3(deceased,style={'color':'white'}),
                    
                    ],className='card-body')
                
                ],className='card bg-success')
            
            ],className='col-md-3'),
        
        ],className='row'),
    
    
    
    html.H1(""),
    
    html.Div([
        
        html.Div([
            
            html.Div([
                
                html.Div([
                    
                    dcc.Graph(id='pie',figure={
                        
                        'data':[go.Pie(values=df['age_groups'].value_counts(),labels=df['age_groups'].value_counts().index)],
                        'layout':go.Layout(title=('Age Distribution'))
                    })
                    
                    ],className='card-body')
                
                ],className='card')
            
            ],className='col-md-6'),
                html.Div([
            
            html.Div([
                
                html.Div([
                    
                    dcc.Graph(id='line',figure={
                        
                        'data':[go.Line(x=data['diagnosed_date'],y=data['id'])],
                        'layout':go.Layout(title=('Day by Day Analysis'))
                    })
                    
                    ],className='card-body')
                
                ],className='card')
            
            ],className='col-md-6')
        
        ],className='row'),
    
    
    
    
    html.H1(""),
    html.Div([
    html.Div([  
        
                    html.Div([
                
                html.Div([
                    
                    dcc.Dropdown(id='picker',value='All',options=options),
                    dcc.Graph(id='bar')
                    
                    ],className='card-body')
                
                ],className='card')
            
            ],className='col-md-12'),
        
        ],className='row')
    
    
    
    ],className='container')


@app.callback(Output('bar','figure'),[Input('picker','value')])
def create_graph(option):
    if option == 'All':
        all_patients = df['detected_state'].value_counts().reset_index()
        return {
            'data':[go.Bar(x=all_patients['detected_state'],y=all_patients['count'])]
        }
    else:
        all_patients = df[df['current_status']==option]['detected_state'].value_counts().reset_index()
        return {
            'data':[go.Bar(x=all_patients['detected_state'],y=all_patients['count'])]
        }
    



if __name__ == '__main__':
    app.run(debug=True)