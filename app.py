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
    brand="Avocado Dashboard",
    color="primary",
    dark=True,
    children=[
        dbc.NavItem(
            dbc.NavLink(page["name"], href=page["path"])
        )
        for page in dash.page_registry.values()
    ],
)

app.layout = html.Div(
    [
        navbar,
        dbc.Container(
            dash.page_container,
            fluid=True,
            className="pt-4"
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