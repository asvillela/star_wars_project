# Comparison of pair of vehicles (horizontal bar chart with axis in the middle)
#       by vehicle

from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from .ids import *

def render(app,data):
    def extract_numeric_value(text):
        if isinstance(text, str):
            numeric_part = ''.join(filter(str.isdigit, text))
            return int(numeric_part) if numeric_part else 0
        else:
            return 0

    df_ship = data.loc[data["title"] == "starships", "dfs"].iloc[0]
    df_vehi = data.loc[data["title"] == "vehicles", "dfs"].iloc[0]

    df_vehicles = pd.concat([df_ship, df_vehi], ignore_index=True)
    df_vehicles["vehicle_class"] = df_vehicles["vehicle_class"].str.capitalize()
    df_vehicles["manufacturer"] = df_vehicles["manufacturer"].str.title()
    df_vehicles.drop_duplicates(subset="name", keep='first', inplace=True)
    df_vehicles["length"] = pd.to_numeric(df_vehicles["length"], errors="coerce").fillna(0)
    df_vehicles["cost_in_credits"] = pd.to_numeric(df_vehicles["cost_in_credits"], errors="coerce").fillna(0)
    df_vehicles["max_atmosphering_speed"] = df_vehicles["max_atmosphering_speed"].apply(extract_numeric_value)

    df_vehicles["crew"] = pd.to_numeric(df_vehicles["crew"], errors="coerce").fillna(0)
    df_vehicles["passengers"] = pd.to_numeric(df_vehicles["passengers"], errors="coerce").fillna(0)
    df_vehicles["cargo_capacity"] = pd.to_numeric(df_vehicles["cargo_capacity"], errors="coerce").fillna(0)
    df_vehicles["hyperdrive_rating"] = pd.to_numeric(df_vehicles["hyperdrive_rating"], errors="coerce").fillna(0)

    @app.callback(
        Output(VEHICLE_COST_BARH_CHART, "children"),
        [
            Input(DROPDOWN_VEHICLE_LEFT, "value"),
            Input(DROPDOWN_VEHICLE_RIGHT, "value")
        ]
    )
    def update_vehicle_cost_barh_chart(vehicle1, vehicle2):
        comparison_elements = ['Cost in credits', 'Speed in atmosphere', 'Cargo capacity', 'Hyperdrive rating', 'Length', 'Crew capacity', 'Passengers capacity']

        if df_vehicles[df_vehicles["name"] == vehicle1].empty: vehicle1_values = [0] * 7  # Replace with default values if DataFrame is empty
        else:
            vehicle1_values = pd.to_numeric(df_vehicles[df_vehicles["name"] == vehicle1][['cost_in_credits', 'max_atmosphering_speed', 'cargo_capacity', 'hyperdrive_rating', 'length', 'crew', 'passengers']].values[0])
        if df_vehicles[df_vehicles["name"] == vehicle2].empty: vehicle2_values = [0] * 7  # Replace with default values if DataFrame is empty
        else:
            vehicle2_values = pd.to_numeric(df_vehicles[df_vehicles["name"] == vehicle2][['cost_in_credits', 'max_atmosphering_speed', 'cargo_capacity', 'hyperdrive_rating', 'length', 'crew', 'passengers']].values[0])

        max_cost = max(vehicle1_values[0],vehicle2_values[0],1)
        max_speed = max(vehicle1_values[1],vehicle2_values[1],1)
        max_cargo = max(vehicle1_values[2],vehicle2_values[2],1)
        max_hyperdrive = max((100/max(vehicle1_values[3],0.0001)),(100/max(vehicle2_values[3],0.0001)),1)
        max_length = max(vehicle1_values[4],vehicle2_values[4],1)
        max_crew = max(vehicle1_values[5],vehicle2_values[5],1)
        max_passengers = max(vehicle1_values[6],vehicle2_values[6],1)

        vehicle1_normalized = [
            vehicle1_values[0]/max_cost,
            vehicle1_values[1]/max_speed,
            vehicle1_values[2]/max_cargo,
            0 if vehicle1_values[3] == 0 else (100/vehicle1_values[3])/max_hyperdrive,
            vehicle1_values[4]/max_length,
            vehicle1_values[5]/max_crew,
            vehicle1_values[6]/max_passengers
            ]        

        vehicle2_normalized = [
            vehicle2_values[0]/max_cost,
            vehicle2_values[1]/max_speed,
            vehicle2_values[2]/max_cargo,
            0 if vehicle2_values[3] == 0 else (100/vehicle2_values[3])/max_hyperdrive,
            vehicle2_values[4]/max_length,
            vehicle2_values[5]/max_crew,
            vehicle2_values[6]/max_passengers
            ]

        data = pd.DataFrame()
        data["comp_elem"] = comparison_elements[::-1]
        data["vehicle1"] = vehicle1_normalized[::-1]
        data["vehicle1-"] = -data["vehicle1"]
        data["vehicle2"] = vehicle2_normalized[::-1]
        data["vehicle1_values"] = vehicle1_values[::-1]
        data["vehicle2_values"] = vehicle2_values[::-1]
        

        fig1 = px.bar(
            data,
            y="comp_elem",
            x="vehicle1-",
            orientation="h",
            color="vehicle1",
            color_continuous_scale="Greys",
            opacity=0.8,
            hover_data={"vehicle1_values"}
        )
        fig2 = px.bar(
            data,
            y="comp_elem",
            x="vehicle2",
            orientation="h",
            color="vehicle2",
            # color_continuous_scale="Greys",
            opacity=0.8,
            hover_data={"vehicle2_values"}
        )
        fig = fig1.add_traces(fig2.data)
        fig.update_layout(
            title="Side by side comparison",
            yaxis_title="Comparison Elements",
            xaxis_title="",
            plot_bgcolor='white',
            coloraxis_showscale=False,
        )
        fig.update_traces(
            hovertemplate="%{customdata[0]}"
        )
        return html.Div(dcc.Graph(figure=fig), id="bar_h_chart")
    return html.Div(id=VEHICLE_COST_BARH_CHART)

# clean data. some values are not values
# fix hover. need to show real value, not the normalized
# ideally it'd show the image of the selected vehicles.. but I'd have to get all those images. And I can't even make images work yet.
