import pandas as pd
import plotly.express as px
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input,Output
avocado=pd.read_csv('/home/leena/Downloads/avocado-updated-2020.csv')
app=dash.Dash()
app.layout=html.Div(children=[
    html.H1(children='Avocado Type Dashboard'),
    dcc.Dropdown(id='type-dropdown',
                 options=[{'label':i,'value':i}
                          for i in avocado['type'].unique()],
                 value='organic'),
    dcc.Graph(id='volume-graph')
])
@app.callback(
    Output(component_id='volume-graph',component_property='figure'),
    Input(component_id='type-dropdown',component_property='value')
)

def update_graph(selected_type):
    filtered_avocado=avocado[avocado['type'] == selected_type]
    line_fig=px.line(filtered_avocado,
                     x='total_volume',y='total_bags',
                     color='geography',
                     title='Avocado Voluume in All Staed in{selected_type}')
    return line_fig

if __name__ == '__main__':
    app.run_server(debug=True)

