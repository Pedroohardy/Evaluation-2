import dash
from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import pandas as pd

dash.register_page(__name__, path="/page2", name="Page 2")


df = pd.read_csv("datas/avocado.csv")


colonnes_a_exclure = [
    "Unnamed: 0",
    "4046",
    "4225",
    "4770",
    "Small Bags",
    "Large Bags",
    "XLarge Bags"
]


colonnes_affichees = [col for col in df.columns if col not in colonnes_a_exclure]
df_table = df[colonnes_affichees].copy()


regions = sorted(df["region"].dropna().unique())

layout = dbc.Container(
    [
        dbc.Card(
            [
                dbc.CardHeader(
                    "Affichage des données",
                    style={
                        "backgroundColor": "#38a3d6",
                        "color": "white",
                        "fontWeight": "bold",
                        "fontSize": "24px"
                    }
                ),
                dbc.CardBody(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.Label(
                                            "Sélectionner une région",
                                            style={"color": "white", "fontWeight": "bold"}
                                        ),
                                        dcc.Dropdown(
                                            id="page2-region-dropdown",
                                            options=[{"label": r, "value": r} for r in regions],
                                            value="Albany",
                                            clearable=False
                                        )
                                    ],
                                    xs=12, md=6
                                ),
                                dbc.Col(
                                    [
                                        html.Label(
                                            "Sélectionner un type",
                                            style={"color": "white", "fontWeight": "bold"}
                                        ),
                                        dbc.RadioItems(
                                            id="page2-type-radio",
                                            options=[
                                                {"label": "Tous", "value": "all"},
                                                {"label": "conventional", "value": "conventional"},
                                                {"label": "organic", "value": "organic"}
                                            ],
                                            value="all",
                                            inline=True,
                                            label_style={"color": "white", "marginRight": "12px"}
                                        )
                                    ],
                                    xs=12, md=4
                                ),
                                dbc.Col(
                                    [
                                        html.Br(),
                                        dbc.Badge(
                                            f"Lignes: {len(df_table)}",
                                            id="page2-lines-badge",
                                            pill=True,
                                            style={
                                                "backgroundColor": "#8e2de2",
                                                "fontSize": "14px",
                                                "padding": "10px 14px"
                                            }
                                        )
                                    ],
                                    xs=12, md=2,
                                    className="d-flex align-items-end justify-content-md-end"
                                )
                            ],
                            className="g-3 mb-3 p-3",
                            style={
                                "backgroundColor": "#1f1f1f",
                                "borderRadius": "8px"
                            }
                        ),

                        dash_table.DataTable(
                            id="page2-table",
                            columns=[{"name": col, "id": col} for col in df_table.columns],
                            data=df_table.to_dict("records"),
                            sort_action="native",
                            page_size=10,
                            style_table={"overflowX": "auto"},
                            style_header={
                                "backgroundColor": "#f0f0f0",
                                "fontWeight": "bold"
                            },
                            style_cell={
                                "textAlign": "left",
                                "padding": "8px",
                                "fontSize": "13px"
                            }
                        )
                    ]
                )
            ],
            className="mt-4 shadow"
        )
    ],
    fluid=True
)