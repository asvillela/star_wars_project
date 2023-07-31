from dash import Dash, html
import dash_bootstrap_components as dbc
import os
from components import spec_height_bar_chart, spec_lifespan_bar_chart, dropdown_manufacturer, dropdown_vehicle_class, vehicle_comparer_table, dropdown_vehicle_left, dropdown_vehicle_right, vehicle_cost_barh_chart

def create_layout(app, data):
    heading1 = html.H1(
        "Star Wars vehicle market",
        className="bg-dark text-white p-2 mb-3"
    )
    heading2 = html.H1(
        "Star Wars curiosities",
        className="bg-dark text-white p-2 mb-3"
    )
    rancor_image_url = os.path.join(os.getcwd(), "assets/images/Pateesa/Rancor.png")
    yoda_image_url = os.path.join(os.getcwd(), "assets/images/Yoda/image_20211118_162549_3512.jpg")
    yoda_dying_image_url = os.path.join(os.getcwd(), "assets/images/Yoda/yoda_dying.jpeg")

    return dbc.Container(
        [
            dbc.Row([
                dbc.Col(heading1)
            ]),
            dbc.Row([
                dbc.Col(dropdown_vehicle_class.render(app, data), lg=12),
                # dbc.Col(dropdown_manufacturer.render(app, data), lg=6)
            ], className="mt-4"),
            dbc.Row([
                dbc.Col(vehicle_comparer_table.render(app, data), lg=12),
            ], className="mt-4"),
            dbc.Row([
                dbc.Col(dropdown_vehicle_left.render(app, data), lg=6),
                dbc.Col(dropdown_vehicle_right.render(app, data), lg=6),
            ], className="mt-4"),
            dbc.Row([
                dbc.Col(vehicle_cost_barh_chart.render(app, data), lg=12),
            ], className="mt-4"),

            dbc.Row([
                dbc.Col(heading2)
            ]),
            dbc.Row([
                dbc.Col(html.Div([
                    html.Img(
                        src=Dash.get_asset_url(app,"images/Pateesa/Rancor.png"),
                        alt="Rancor image",
                        height="400",
                        # width="700",
                    )],style={"textAlign": "left"}),lg=3,
                ),
                dbc.Col(spec_height_bar_chart.render(app, data), lg=8),
                dbc.Col(html.Div([
                    html.Img(
                        src=Dash.get_asset_url(app,"images/Yoda/yoda.png"),
                        alt="Yoda image",
                        height="100",
                        # width=2,
                    )]),lg=1,
                ),
            ],
            className="g-0",
            align="end",
            ),
            dbc.Row([
            ], className="mt-4"),
            dbc.Row([
                dbc.Col(
                    html.Img(
                        src=Dash.get_asset_url(app,"images/Yoda/yoda_dying_cropped.png"),
                        alt="Yoda dying image",
                        height="400",
                    ),lg=6
                ),
                dbc.Col(spec_lifespan_bar_chart.render(app, data), lg=6),
            ],
            className="g-0",
            align="end",

            ),
        ]
    )



