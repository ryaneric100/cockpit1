# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 11:34:24 2023

@author: DCHELD
"""
import plotly.graph_objects as go

# Create the gauge chart
fig = go.Figure(go.Indicator(
    mode="gauge+delta", #♦  mode="gauge+number",
    value=65,
    delta = {'reference': 0,'increasing': {'color': "Black"}},
    domain={'x': [0, 1], 'y': [0, 1]},
    gauge={
        'axis': {'range': [None, 100], 'tickcolor': "darkblue"},
        'bar': {'color': "black", 'thickness': 0.1},  # The needle (set to a thin line to mimic an arrow)
        'steps': [
            {'range': [0, 25], 'color': 'red'},
            {'range': [25, 50], 'color': 'orange'},
            {'range': [50, 75], 'color': 'yellow'},
            {'range': [75, 100], 'color': 'green'}
        ],
        'threshold': {
            'line': {'color': "black", 'width': 2},
            'thickness': 0.75,
            'value': 65
        }
    }
))

# Set the gauge's background to white (or any other color or even transparent if needed)
fig.update_traces(gauge_bgcolor='white')

# Set the layout to remove the plot background color
fig.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    title="Gauge Chart Example"
)

# Show the figure
fig.show()
