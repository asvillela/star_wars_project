from dash import html, dcc, Input, Output
import pandas as pd
from .ids import *

# def select_all_manufacturers(df_vehicles, manufacturers, n):
#     filtered_data = df_vehicles.query("manufacturer in @manufacturers")
#     return sorted(filtered_data["manufacturer"].unique())


def render(app, data):
    df_ship = data.loc[data["title"] == "starships", "dfs"].iloc[0]
    df_vehi = data.loc[data["title"] == "vehicles", "dfs"].iloc[0]

    # df_ship["vehicle_class"] = df_ship["starship_class"]
    # df_ship.drop("starship_class", axis=1, inplace=True)
    df_vehicles = pd.concat([df_ship, df_vehi], ignore_index=True)
    df_vehicles["vehicle_class"] = df_vehicles["vehicle_class"].str.capitalize()
    df_vehicles["manufacturer"] = df_vehicles["manufacturer"].str.title()
    df_vehicles.drop_duplicates(subset="name", keep='first', inplace=True)
    df_vehicles.dropna(subset=["manufacturer"], inplace=True)
    all_manufacturers = df_vehicles["manufacturer"].unique()
    list_manufacturers = [{"label":manufacturer, "value":manufacturer} for manufacturer in all_manufacturers]

    @app.callback(
        Output(DROPDOWN_MANUFACTURER, "value"),
        [
            Input(DROPDOWN_VEHICLE_CLASS, "value"),
            Input(SELECT_ALL_MANUFACTURERS_BUTTON, "n_clicks")
        ]
    )
    def select_all_manufacturers(manufacturers, n):     # this 'manufacturers' don't make sense to me. Should be 'vehicle_class', right?
        if n > 0:
            return sorted(df_vehicles["manufacturer"].unique())
        else:
            filtered_data = df_vehicles.query("manufacturer in @manufacturers")
            return sorted(filtered_data["manufacturer"].unique())

    dropdown = html.Div(
        [
            html.H6("Manufacturer"),
            dcc.Dropdown(
                id = DROPDOWN_MANUFACTURER,
                options = list_manufacturers,
                multi = True,
                style={
                    # "height": "100px",
                    "maxHeight": "100px",
                    "overflowY": "scroll",
                    # "color": "grey",
                    # "background-color": "white"
                }
            ),
            html.Button(
                children=["Select All"],
                className="dropdown-button",
                id=SELECT_ALL_MANUFACTURERS_BUTTON,
                n_clicks=0
            )
        ]
    )
    return dropdown

# maybe open explode manufacturers
# maybe remove 'corp', 'inc', 'corporation', etc
