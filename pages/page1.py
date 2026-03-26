import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go

dash.register_page(__name__, path="/", name="Page 1")

df = pd.read_csv("datas/avocado.csv")
df["Date"] = pd.to_datetime(df["Date"])

regions_principales = [
    "MidSouth",
    "Northeast",
    "SouthCentral",
    "Southeast",
    "TotalUS",
    "West"
]

regions_dropdown = sorted(df["region"].dropna().unique())


def figure_gauche_vide():
    fig = go.Figure()

    for region in regions_principales:
        fig.add_trace(
            go.Scatter(
                x=[],
                y=[],
                mode="lines",
                name=region
            )
        )

    fig.update_layout(
        title="Quantités vendues - Régions principales",
        xaxis_title="Date",
        yaxis_title="Volume total",
        height=420,
        margin=dict(l=20, r=20, t=50, b=20),
        template="plotly_white"
    )
    return fig


def figure_droite_vide(region="Albany"):
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=[],
            y=[],
            mode="lines",
            name=region
        )
    )

    fig.update_layout(
        title=f"Quantités vendues - {region}",
        xaxis_title="Date",
        yaxis_title="Volume total",
        height=420,
        margin=dict(l=20, r=20, t=50, b=20),
        template="plotly_white"
    )
    return fig


layout = dbc.Container(
    [
        dbc.Card(
            [
                dbc.CardHeader(
                    "Quantités vendues (Total Volume)",
                    style={
                        "backgroundColor": "#38a3d6",
                        "color": "white",
                        "fontWeight": "bold",
                        "fontSize": "28px"
                    }
                ),
                dbc.CardBody(
                    dbc.Row(
                        [
                            dbc.Col(
                                dcc.Graph(
                                    id="page1-graph-global",
                                    figure=figure_gauche_vide()
                                ),
                                width=7
                            ),
                            dbc.Col(
                                [
                                    dbc.Badge(
                                        "Sélectionnez une région:",
                                        color="primary",
                                        className="mb-3 w-100",
                                        style={
                                            "fontSize": "16px",
                                            "padding": "10px",
                                            "backgroundColor": "#8e2de2"
                                        }
                                    ),
                                    dcc.Dropdown(
                                        id="page1-region-dropdown",
                                        options=[
                                            {"label": r, "value": r}
                                            for r in regions_dropdown
                                        ],
                                        value="Albany",
                                        clearable=False,
                                        className="mb-3"
                                    ),
                                    dcc.Graph(
                                        id="page1-graph-region",
                                        figure=figure_droite_vide("Albany")
                                    )
                                ],
                                width=5
                            )
                        ],
                        className="g-3"
                    )
                )
            ],
            className="mt-4 shadow"
        )
    ],
    fluid=True
)