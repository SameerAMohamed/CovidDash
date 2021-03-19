import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)  # Start the app

# ---------- Import and clean data (importing csv into pandas)
df = pd.read_csv("owid-covid-data.csv")  # read data into dataframe

df_refined = df[['date', 'continent', 'location', 'total_cases', 'new_cases', 'total_deaths', 'new_deaths',
                 'total_cases_per_million', 'new_cases_per_million']]
df_refined = df_refined.fillna(0)  # Fill all empty cells with 0

df_refined.reset_index(inplace=True)  # Reset index for alignment

# Create a dataframe of all the countries
name_arr = df_refined.location.unique()  # Make an array out of the names
op = dict(zip(name_arr, name_arr))  # Make a dictionary out of the array

# Now for app layout
app.layout = html.Div([

    html.H1("Web Application Dashboards with Dash", style={'text-align': 'center'}),  # title for the webpage header

    dcc.Dropdown(
        id="country_input",
        options=[{'label': x, 'value': x} for x in name_arr],
        value='',
        placeholder='Select a country',
        searchable=True,
        multi=True
    ),
    dcc.Dropdown(
        id="metric_input",
        options=[{'label': 'Total Cases', 'value': 'total_cases'},
                 {'label': 'New Cases', 'value': 'new_cases'},
                 {'label': 'Total Deaths', 'value': 'total_deaths'},
                 {'label': 'New Deaths', 'value': 'new_deaths'},
                 {'label': 'Total Cases Per Million', 'value': 'total_cases_per_million'},
                 {'label': 'New Cases Per Person', 'value': 'new_cases_per_million'}],
        value='',
        placeholder='Select a Metric',
        searchable=True,
        multi=False
    ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='line_graph', figure={})

])


@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='line_graph', component_property='figure')],
    [Input(component_id='country_input', component_property='value'),
     Input(component_id='metric_input', component_property='value')]
)
def update_graph(country_selection, metric_selection):
    if type(country_selection) == str:
        country_selection = [country_selection]

    if country_selection is not None:
        container = "The countries chosen by user were: {}".format(
            country_selection)  # Print a line telling user what happened
    else:
        container = None

    dff = df_refined.copy()  # Make a copy of the dataframe

    dff = dff[dff['location'].isin(country_selection)]  # Only take rows with country selected
    if country_selection is not None:
        fig = px.line(dff, x="date", y=metric_selection, title=f'Instances of COVID in {country_selection}',
                      color='location')
    else:
        fig = None

    return container, fig


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
