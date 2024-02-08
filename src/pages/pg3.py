import dash
from dash import  html, callback, Output, Input
import dash_bootstrap_components as dbc
from  functions.trading import trading
from  functions.positions import positions
from  functions.portfolio import portfolio
from  functions.allocations import  allocations
from  functions.contributions import contributions
from functions.sql.get_main_portfolio_df import   get_main_portfolio_df


# name of strategy


#strat_name = 'dc_ai_ptf'
strat_name = 'dc_rs_short_ptf'
strat_name = 'swiss_equity_plus_sli_ptf'
max_exposure = 1


#df = get_main_portfolio_df('dc_rs_short_ptf')
df = get_main_portfolio_df(strat_name)

dash.register_page(__name__,
                   path='/portfolio1',
                   name='Portfolio1',
                   title='Portfolio',
                   image='pg3.png',
                   description='Learn all about the heatmap.'
)


layout = html.Div(    
    [
     
   html.Hr(),  
   html.H5('Portfolio xyz') ,
     
 dbc.Card(
    [
        dbc.CardHeader(
            dbc.Tabs(
                [
                    dbc.Tab(label="PORTFOLIO", tab_id="tab-ptf"),
                    dbc.Tab(label="POSITIONS", tab_id="tab-positions"),
                    dbc.Tab(label="ALLOCATIONS", tab_id="tab-allocations"),
                    dbc.Tab(label="CONTRIBUTIONS", tab_id="tab-contributions"),
                    dbc.Tab(label="TRADING", tab_id="tab-trading"),
                    dbc.Tab(label="RANKINGS", tab_id="tab-infos"),
                    dbc.Tab(label="DATA", tab_id="tab-data"),
                ],
                id="card-tabs",
                active_tab="tab-ptf",
            )
        ),
        dbc.CardBody(html.P(id="card-content", className="card-text")),
    ]
    ),
  
 
  ]
)


@callback(
    Output("card-content", "children"), [Input("card-tabs", "active_tab")]
)

def render_content(active_tab):
    if active_tab == 'tab-ptf':
        return portfolio(df)
    elif active_tab == 'tab-positions':
        return positions(df)
    elif active_tab == 'tab-allocations':
        return allocations(df)
    elif active_tab == 'tab-contributions':
        return contributions(df)
    elif active_tab == 'tab-trading':
        return trading(df)
    
    