# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 08:57:49 2023

@author: DCHELD
"""
import plotly.graph_objects as go



def get_gauge_from_allocation():

    # w_min,w_max,w_act,file_name
    
    val = 50
    vmin = 20
    vmax = 80
    d = vmax - vmin
    s = d/4

    # Create the gauge chart
    fig = go.Figure(go.Indicator(
        mode="gauge", #♦  mode="gauge+number", "gauge+delta"
        value=val,
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [vmin, vmax], 'tickcolor': "darkblue"},
            'bar': {'color': "black", 'thickness': 0.1},  # The needle (set to a thin line to mimic an arrow)
            'steps': [
                {'range': [vmin, vmin + s], 'color': '#f44336'},
                {'range': [vmin + s, vmin + 2*s], 'color': 'orange'},
                {'range': [vmin + 2*s, vmin + 3*s], 'color': '#ffd966'},
                {'range': [vmin + 3*s, vmax], 'color': '#6aa84f'}
            ],
            'threshold': {
                'line': {'color': "black", 'width': 1},
                'thickness': 0.75,
                'value': val
            }
        }
    ))
    
    # Set the gauge's background to white (or any other color or even transparent if needed)
    fig.update_traces(gauge_bgcolor='white')
    
    # Set the layout to remove the plot background color
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        #title="Gauge Chart Example"
    )
    
    # Show the figure
    #fig.show()
    
    return fig