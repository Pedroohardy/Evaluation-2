import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

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


df_left = df[df["region"].isin(regions_principales)].copy()
df_left = (
    df_left.groupby(["Date", "region"], as_index=False)["Total Volume"]
    .sum()
)

fig_left = px.line(
    df_left,
    x="Date",
    y="Total Volume",
    color="region",
    title="Quantités vendues - Régions principales"
)

fig_left.update_layout(
    xaxis_title="Date",
    yaxis_title="Volume total",
    height=420
)

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
                        "fontSize": "24px"
                    }
                ),
                dbc.CardBody(
                    dbc.Row(
                        [
                            dbc.Col(
                                dcc.Graph(
                                    id="page1-graph-left",
                                    figure=fig_left
                                ),
                                width=7
                            ),
                            dbc.Col(
                                [
                                    dbc.Badge(
                                        "Sélectionnez une région :",
                                        className="mb-3 w-100",
                                        style={
                                            "backgroundColor": "#8e2de2",
                                            "color": "white",
                                            "padding": "10px",
                                            "fontSize": "16px"
                                        }
                                    ),
                                    dcc.Dropdown(
                                        id="page1-dropdown",
                                        options=[
                                            {"label": r, "value": r}
                                            for r in regions_dropdown
                                        ],
                                        value="Albany",
                                        clearable=False,
                                        className="mb-3"
                                    ),
                                    dcc.Graph(
                                        id="page1-graph-right"
                                    )
                                ],
                                width=5
                            )
                        ]
                    )
                )
            ],
            className="mt-4 shadow"
        )
    ],
    fluid=True
)