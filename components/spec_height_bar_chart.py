# Species height bar chart (species ordered by avg height)
#     on hover
#       characters of those species
#       hometowns of characters on those species
#       language
#     i'd like a filter that would change the color of selected species in the chart

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from .ids import *

def render(app,data):
    if data.shape[0]==0:
        return html.Div("No data selected", id=SPEC_HEIGHT_BAR_CHART)
    df_spec = data.loc[data["title"] == "species", "dfs"].iloc[0]
    df_spec.sort_values(by=["average_height"], ascending=False, inplace=True)
    df_spec_height = df_spec[pd.to_numeric(df_spec["average_height"], errors='coerce').notnull()]
    df_spec_height["language"].fillna("unknown", inplace=True)
    df_spec_height["homeworld"].fillna("unknown", inplace=True)

    fig = px.bar(
        df_spec_height,
        x = "name",
        y = "average_height",
        hover_data=["language", "homeworld"],
        text_auto=".2s",
        color_discrete_sequence=['#333333'],
    )
    fig.update_traces(
        hovertemplate= "Species: %{x}<br>Avg height: %{y}<br>Language: %{customdata[0]}<br>Home Planet: %{customdata[1]}",
        textposition="outside",
        cliponaxis=False,
        textangle=-45,
        # textfont_color="white"
    ),
    fig.update_xaxes(title=None),
    fig.update_layout(
        title="Average height by species in cm",
        yaxis_title="centimeters",
        xaxis=dict(tickangle=-45),
        plot_bgcolor='white',
        paper_bgcolor="rgba(255, 255, 255, 0.5)"
    )
    return html.Div(dcc.Graph(figure=fig), id=SPEC_HEIGHT_BAR_CHART)

# add images of Pateesa to the left, and Yoda to the right
# ADD RANCOR AND PATEESA TO THE DATABASE
# ADD SARLACC TO THE DATABASE

