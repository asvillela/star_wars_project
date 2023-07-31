from dash import html, dcc
import pandas as pd
from .ids import *

def render(app, data):
    df_ship = data.loc[data["title"] == "starships", "dfs"].iloc[0]
    df_vehi = data.loc[data["title"] == "vehicles", "dfs"].iloc[0]

    df_vehicles = pd.concat([df_ship, df_vehi], ignore_index=True)
    df_vehicles["vehicle_class"] = df_vehicles["vehicle_class"].str.capitalize()
    df_vehicles["manufacturer"] = df_vehicles["manufacturer"].str.title()
    df_vehicles.drop_duplicates(subset="name", keep='first', inplace=True)
    df_vehicles.sort_values(by="name", inplace=True)

    all_vehicles = df_vehicles["name"].unique()
    vehicle_list = [{"label": vehicle, "value": vehicle} for vehicle in all_vehicles]

    dropdown = html.Div(
        [
            html.H6("First vehicle"),
            dcc.Dropdown(
                options = vehicle_list,
                multi = False,
                id = DROPDOWN_VEHICLE_LEFT
            )
        ]
    )
    return dropdown