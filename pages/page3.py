import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/page3", name="Page 3")


def lire_md(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


texte1 = lire_md("expli1.md")
texte2 = lire_md("expli2.md")
texte3 = lire_md("expli3.md")


layout = dbc.Container(
    [
        dbc.Card(
            [
                # HEADER
                dbc.CardHeader(
                    "PRÉSENTATION DE DASH",
                    style={
                        "backgroundColor": "#38a3d6",
                        "color": "white",
                        "fontWeight": "bold",
                        "fontSize": "22px",
                        "textTransform": "uppercase"
                    }
                ),

                # BODY NOIR
                dbc.CardBody(
                    [
                        html.Div(
                            [
                                dcc.Tabs(
                                    value="tab-1",
                                    children=[

                                        # ONGLET 1
                                        dcc.Tab(
                                            label="Accueil",
                                            value="tab-1",
                                            children=[
                                                dcc.Markdown(
                                                    texte1,
                                                    style={
                                                        "padding": "25px",
                                                        "color": "white"
                                                    }
                                                )
                                            ],
                                            style={
                                                "backgroundColor": "#222",
                                                "color": "white"
                                            },
                                            selected_style={
                                                "backgroundColor": "#38a3d6",
                                                "color": "white"
                                            }
                                        ),

                                        # ONGLET 2
                                        dcc.Tab(
                                            label="Layout",
                                            value="tab-2",
                                            children=[
                                                dcc.Markdown(
                                                    texte2,
                                                    style={
                                                        "padding": "25px",
                                                        "color": "white"
                                                    }
                                                )
                                            ],
                                            style={
                                                "backgroundColor": "#222",
                                                "color": "white"
                                            },
                                            selected_style={
                                                "backgroundColor": "#38a3d6",
                                                "color": "white"
                                            }
                                        ),

                                        # ONGLET 3
                                        dcc.Tab(
                                            label="CallBack",
                                            value="tab-3",
                                            children=[
                                                dcc.Markdown(
                                                    texte3,
                                                    style={
                                                        "padding": "25px",
                                                        "color": "white"
                                                    }
                                                )
                                            ],
                                            style={
                                                "backgroundColor": "#222",
                                                "color": "white"
                                            },
                                            selected_style={
                                                "backgroundColor": "#38a3d6",
                                                "color": "white"
                                            }
                                        ),
                                    ],
                                    colors={
                                        "border": "#222",
                                        "primary": "#38a3d6",
                                        "background": "#222"
                                    }
                                )
                            ],
                            style={
                                "backgroundColor": "#222",
                                "borderRadius": "8px"
                            }
                        )
                    ],
                    style={"backgroundColor": "#222"}
                )
            ],
            className="mt-4 shadow",
            style={
                "border": "2px solid #333",
                "borderRadius": "10px"
            }
        )
    ],
    fluid=True,
    className="py-4"
)