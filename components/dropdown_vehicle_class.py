from dash import html, dcc
# import dash_bootstrap_components as dbc
import pandas as pd
from .ids import *

def render(app, data):
    df_ship = data.loc[data["title"] == "starships", "dfs"].iloc[0]
    df_vehi = data.loc[data["title"] == "vehicles", "dfs"].iloc[0]

    df_ship["vehicle_class"] = df_ship["starship_class"]
    df_ship.drop("starship_class", axis=1, inplace=True)
    df_vehicles = pd.concat([df_ship, df_vehi], ignore_index=True)
    df_vehicles["vehicle_class"] = df_vehicles["vehicle_class"].str.capitalize()
    df_vehicles.drop_duplicates(subset="name", keep='first', inplace=True)

    all_vehicle_class = df_vehicles["vehicle_class"].unique()
    vehicle_class_list = [{"label": vehicle_class, "value": vehicle_class} for vehicle_class in all_vehicle_class]
    return html.Div(
        [
            html.H6("Vehicle class"),
            dcc.Dropdown(
                options=vehicle_class_list,
                placeholder="Choose vehicle class",
                value="Speeder",
                multi=False,
                className="mb-3",
                id=DROPDOWN_VEHICLE_CLASS
            )
        ]
    )