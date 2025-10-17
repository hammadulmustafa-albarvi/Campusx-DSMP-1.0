import pandas as pd
import numpy as np
from dash import html, dcc
import seaborn as sns
import dash
import plotly.express as px
import plotly.graph_objs as go


data = px.data.gapminder()
app = dash.Dash()
# app.layout= html.H1(children="My first dashboard",style={'color':'red'})

app.layout=html.Div([
    html.Div(children=[
        html.H2(children='My Dashboard',style={'text-align':'center'})
],style={'border':'1px black solid','float':'right','width':'100%','height':'50px'}),
    html.Div(children=[
        dcc.Graph(id='scatter-plot',
                  figure={
                      'data':[go.Scatter(x=data['pop'],y=data['gdpPercap'],mode='markers')],
                      'layout':go.Layout(title='Scatter Plot')
                      
                  }
                  )
],
             style={'border':'1px black solid','float':'right','width':'49.7%','height':'350px'}),
    html.Div(children=[
        dcc.Graph(id='box-plot',
                  figure={
                      'data':[go.Box(x=data['gdpPercap'])],
                      'layout':go.Layout(title='Box Plot')
                  }
                  )
    ] 
        
        ,style={'border':'1px black solid','float':'right','width':'49.7%','height':'350px'}) 
])

if __name__ == '__main__':
    app.run()