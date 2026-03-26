from dash import Input, Output, callback
import pandas as pd


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


@callback(
    Output("page2-table", "data"),
    Output("page2-lines-badge", "children"),
    Input("page2-region-dropdown", "value"),
    Input("page2-type-radio", "value")
)
def update_table(selected_region, selected_type):
    df_filtre = df.copy()

  
    if selected_region is not None:
        df_filtre = df_filtre[df_filtre["region"] == selected_region]

   
    if selected_type != "all":
        df_filtre = df_filtre[df_filtre["type"] == selected_type]

    
    df_filtre = df_filtre[colonnes_affichees]

  
    badge_text = f"Lignes: {len(df_filtre)}"

    return df_filtre.to_dict("records"), badge_text