# Starship/Vehicle class competition table
#   filter for manufacturers and vehicle class
#     comparison color-coded table of:
#       cost
#       atmospheric speed
#       cargo capacity
#       hyperdrive rating
#       length
#       crew
#       passangers

from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from .ids import *

def render(app,data):
    df_ship = data.loc[data["title"] == "starships", "dfs"].iloc[0]
    df_vehi = data.loc[data["title"] == "vehicles", "dfs"].iloc[0]

    # df_ship["vehicle_class"] = df_ship["starship_class"]                # it may give an error here, as the column it is copying from has already been dropped
    # df_ship.drop("starship_class", axis=1, inplace=True)                # it may give an error here, as the column it is copying from has already been dropped
    df_vehicles = pd.concat([df_ship, df_vehi], ignore_index=True)
    df_vehicles["vehicle_class"] = df_vehicles["vehicle_class"].str.capitalize()
    df_vehicles["manufacturer"] = df_vehicles["manufacturer"].str.title()
    df_vehicles.drop_duplicates(subset="name", keep='first', inplace=True)

    @app.callback(
        Output(VEHICLE_COMPARISON_TABLE, "children"),
        [
            Input(DROPDOWN_VEHICLE_CLASS, "value"),
            # Input(DROPDOWN_MANUFACTURER, "value")
        ]
    )
    # def update_spec_height_bar_chart(vehicle_classes, manufacturers):
    #     filtered_data = df_vehicles.query("vehicle_class in @vehicle_classes and manufacturer in @manufacturers")
    def update_spec_height_bar_chart(vehicle_classes):
        filtered_data = df_vehicles.query("vehicle_class in @vehicle_classes")
        if filtered_data.shape[0]==0:
            return html.Div("No Data Selected", id=VEHICLE_COMPARISON_TABLE)
        vehicle_comparer_table = filtered_data[['name', 'manufacturer', 'cost_in_credits', 'max_atmosphering_speed', 'cargo_capacity', 'hyperdrive_rating', 'length', 'crew', 'passengers']].set_index("name").T
        vehicle_comparer_table.index = ['Manufacturer', 'Cost in credits', 'Speed in atmosphere', 'Cargo capacity', 'Hyperdrive Rating', 'Length', 'Crew capacity', 'Passengers capacity']
        vehicle_comparer_table.index.set_names("", inplace=True)
        return html.Div(
            [
                html.H6("Vehicle comparer table"),
                dbc.Table.from_dataframe(
                    vehicle_comparer_table,
                    striped=True,
                    bordered=True,
                    hover=True,
                    color="light",
                    index=True,
                ),
            ],
            # fluid=True,
            id=VEHICLE_COMPARISON_TABLE
        )
    return html.Div(id=VEHICLE_COMPARISON_TABLE)


# centralize things
# format numbers as 1,000,000
# clean indexes (remove _s, capitalize)
