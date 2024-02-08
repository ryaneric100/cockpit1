# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 11:25:18 2023

@author: DCHELD
"""
from dash import Input, Output, html, dcc
import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

options = ['Option 1', 'Option 2', 'Option 3']

dropdown_items = []
for option in options:
    item = dbc.DropdownMenuItem(option, id=option)
    dropdown_items.append(item)

dropdown = dbc.DropdownMenu(
    label="Select an option",
    id="dropdown-menu",
    children=dropdown_items,
)

app.layout = dbc.Container(
    [
        dbc.Row(dbc.Col(dropdown)),
        dbc.Row(dbc.Col(html.Div(id="output-div")))
    ],
    className="mt-4"
)

@app.callback(
    Output("output-div", "children"),
    Input("dropdown-menu", "n_clicks"),
    prevent_initial_call=True
)
def update_output(n_clicks):
    ctx = dash.callback_context
    if ctx.triggered:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        selected_option = button_id
        return f"You selected {selected_option}."
    else:
        return "Please select an option."

if __name__ == '__main__':
    app.run_server(debug=True)