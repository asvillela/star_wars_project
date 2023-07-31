# Species lifespan bar chart (species ordered by avg lifespan)
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
        return html.Div("No data selected", id=SPEC_LIFESPAN_BAR_CHART)
    df_spec = data.loc[data["title"] == "species", "dfs"].iloc[0]

    df_spec_lifespan = df_spec[pd.to_numeric(df_spec["average_lifespan"], errors='coerce').notnull()]         # filters rows with numeric data in lifespan
    df_spec_lifespan["average_lifespan"] = df_spec_lifespan["average_lifespan"].astype(int)
    df_spec_lifespan.sort_values(by=["average_lifespan"], ascending=True, inplace=True)
    df_spec_lifespan["language"].fillna("unknown", inplace=True)
    df_spec_lifespan["homeworld"].fillna("unknown", inplace=True)

    fig = px.bar(
        df_spec_lifespan,
        x = "name",
        y = "average_lifespan",
        hover_data=["language", "homeworld"],
        text_auto=".2s",
        color_discrete_sequence=['#333333'],
    )
    fig.update_traces(
        hovertemplate = "Species: %{x}<br>Avg lifespan: %{y}<br>Language: %{customdata[0]}<br>Home Planet: %{customdata[1]}",
        textposition="outside",
        cliponaxis=False,
        textangle=-45,
    ),
    fig.update_xaxes(title=None),
    fig.update_layout(
        title="Average lifespan by species",
        yaxis_title="years",
        xaxis=dict(tickangle=-45),
        plot_bgcolor="rgba(0, 0, 0, 0)",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        height=370
    )
    return html.Div(dcc.Graph(figure=fig), id=SPEC_LIFESPAN_BAR_CHART)

# add image of Yoda dying to the right



