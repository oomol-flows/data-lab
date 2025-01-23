from oocana import Context
import pandas as pd
import plotly.express as px


def main(params: dict, context: Context):
    df = params.get("df")
    assert df is not None
    title = params.get("chart_title")
    x_column = params.get("x_column")
    y_column = params.get("y_column")

    if title is None:
        title = "Line Chart"
    if x_column is None:
        x_column = df.columns[0]
    if x_column is None:
        x_column = df.columns[1]

    fig = px.line(
        df,
        x=x_column,
        y=y_column,
        title=title,
        markers=True,
    )

    fig.show()

    return {"df": df}
