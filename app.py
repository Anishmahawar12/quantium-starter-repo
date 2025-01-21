import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from dash.dependencies import Input, Output

# Generate synthetic 3D data (or replace with actual data)
x, y, z = np.mgrid[-50:50:25j, -50:50:25j, -50:50:25j]
values = np.sqrt(x**2 + y**2 + z**2) + np.sin(x) + np.cos(y)

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, "/assets/styles.css"])

# App layout
app.layout = html.Div(
    className="container",
    children=[
        html.H1("Interactive 3D Isosurface Visualization", className="header-title"),
        dcc.Slider(
            id="iso-slider",
            min=values.min(),
            max=values.max(),
            step=0.5,
            value=(values.min() + values.max()) / 2,
            marks={int(i): f"{int(i)}" for i in np.linspace(values.min(), values.max(), 5)},
            tooltip={"placement": "bottom", "always_visible": True},
        ),
        html.Div(
            className="graph-container",
            children=[
                html.Div("Explore 3D Data", className="graph-title"),
                dcc.Graph(id="3d-graph"),
            ],
        ),
    ],
)

# Callback for updating the 3D graph
@app.callback(
    Output("3d-graph", "figure"),
    Input("iso-slider", "value"),
)
def update_3d_graph(iso_value):
    fig = go.Figure()

    # Add isosurface
    fig.add_trace(
        go.Isosurface(
            x=x.flatten(),
            y=y.flatten(),
            z=z.flatten(),
            value=values.flatten(),
            isomin=iso_value - 0.5,
            isomax=iso_value + 0.5,
            surface_count=5,  # Number of layers
            colorscale="Viridis",  # Attractive colors
            caps=dict(x_show=False, y_show=False, z_show=False),
        )
    )

    # Customize layout
    fig.update_layout(
        scene=dict(
            xaxis=dict(title="X-axis", backgroundcolor="#12131c", gridcolor="#2f2f2f"),
            yaxis=dict(title="Y-axis", backgroundcolor="#12131c", gridcolor="#2f2f2f"),
            zaxis=dict(title="Z-axis", backgroundcolor="#12131c", gridcolor="#2f2f2f"),
        ),
        paper_bgcolor="#1e2130",  # Background
        font=dict(color="#ffffff"),  # Text color
        title="Interactive 3D Isosurface Visualization",
    )

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
