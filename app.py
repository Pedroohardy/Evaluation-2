import dash
from dash import html
import dash_bootstrap_components as dbc

from pages import page1_cb, page2_cb, page3_cb

app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True
)

server = app.server

navbar = dbc.NavbarSimple(
    brand="Application des M1 MECEN",
    color="info",
    dark=True,
    children=[
        dbc.NavItem(dbc.NavLink("Comparaison entre région", href="/")),
        dbc.NavItem(dbc.NavLink("Affichage des données", href="/page2")),
        dbc.NavItem(dbc.NavLink("Aide en ligne", href="/page3")),
    ],
)

app.layout = html.Div(
    [
        dbc.Container(
            navbar,
            fluid=True,
            className="pt-3"
        ),
        dbc.Container(
            dash.page_container,
            fluid=True
        )
    ],
    style={
        "backgroundImage": "url('/assets/BG.jpg')",
        "backgroundSize": "cover",
        "backgroundPosition": "center",
        "backgroundRepeat": "no-repeat",
        "minHeight": "100vh"
    }
)

if __name__ == "__main__":
    app.run(debug=True)