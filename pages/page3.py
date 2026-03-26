import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/page3", name="Page 3")


# Fonction pour lire les fichiers markdown
def lire_md(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


# Lecture des fichiers
texte1 = lire_md("expli1.md")
texte2 = lire_md("expli2.md")
texte3 = lire_md("expli3.md")


layout = dbc.Container(
    [
        dbc.Card(
            [
                dbc.CardHeader(
                    "Explications",
                    style={
                        "backgroundColor": "#38a3d6",
                        "color": "white",
                        "fontWeight": "bold",
                        "fontSize": "24px"
                    }
                ),
                dbc.CardBody(
                    [
                        dcc.Tabs(
                            [
                                dcc.Tab(
                                    label="Explication 1",
                                    children=[dcc.Markdown(texte1)]
                                ),
                                dcc.Tab(
                                    label="Explication 2",
                                    children=[dcc.Markdown(texte2)]
                                ),
                                dcc.Tab(
                                    label="Explication 3",
                                    children=[dcc.Markdown(texte3)]
                                ),
                            ]
                        )
                    ]
                )
            ],
            className="mt-4 shadow"
        )
    ],
    fluid=True
)