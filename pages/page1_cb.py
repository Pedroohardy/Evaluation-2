from dash import Input, Output, callback
import pandas as pd
import plotly.express as px

df = pd.read_csv("datas/avocado.csv")
df["Date"] = pd.to_datetime(df["Date"])


@callback(
    Output("page1-graph-right", "figure"),
    Input("page1-dropdown", "value")
)
def update_graph_region(selected_region):
    df_region = df[df["region"] == selected_region].copy()

    df_region = (
        df_region.groupby("Date", as_index=False)["Total Volume"]
        .sum()
    )

    fig = px.line(
        df_region,
        x="Date",
        y="Total Volume",
        title=f"Quantités vendues - {selected_region}"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Volume total",
        height=420
    )

    return fig