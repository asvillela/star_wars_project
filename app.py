from dash import Dash
import dash_bootstrap_components as dbc
import os
from data.util import get_data
from layout import create_layout

PATH_characters = os.path.join(os.getcwd(), "data/characters.csv")
PATH_planets    = os.path.join(os.getcwd(), "data/planets.csv")
PATH_species    = os.path.join(os.getcwd(), "data/species.csv")
PATH_starships  = os.path.join(os.getcwd(), "data/starships.csv")
PATH_vehicles   = os.path.join(os.getcwd(), "data/vehicles.csv")

data = get_data(PATH_characters, PATH_planets, PATH_species, PATH_starships, PATH_vehicles)

app = Dash(__name__, external_stylesheets=[dbc.themes.COSMO])
app.layout = create_layout(app, data)
server = app.server

if __name__ == "__main__":
    app.run_server(debug=True)