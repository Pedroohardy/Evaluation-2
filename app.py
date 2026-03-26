import dash
import dash_bootstrap_components as dbc
from pages import page1_cb

app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

server = app.server

navbar = dbc.NavbarSimple(
    brand="Avocado Dashboard",
    children=[
        dbc.NavItem(
            dbc.NavLink(page["name"], href=page["path"])
        )
        for page in dash.page_registry.values()
    ],
)

app.layout = dbc.Container(
    [
        navbar,
        dash.page_container
    ],
    fluid=True
)

if __name__ == "__main__":
    app.run(debug=True)