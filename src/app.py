import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.LUX], suppress_callback_exceptions=True)  # COSMO  DARKLY
server = app.server


navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href='/')),
        dbc.NavItem(dbc.NavLink("Overview", href="/overview")),
        dbc.DropdownMenu(
            children=[
                #dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem(page["name"], href=page["path"])                 
                for page in dash.page_registry.values()
            ],
            nav=True,
            in_navbar=True,
            label="Portfolios",
        ),
    ],
    brand="dufour cockpit",
    brand_href="#",
    color="dark",
    dark=True,
    fluid=True,
)


def serve_layout():
    layout = dbc.Container([

       dbc.Row([
           navbar
           
           ]), 
       
        dbc.Row(
            [
                dbc.Col(
                    [
                        dash.page_container
                    ] )
            ]
        )

      
    ], fluid=True)
    return layout


app.layout = serve_layout



if __name__ == "__main__":
    app.run(debug=False)











