from cProfile import label
from oocana import Context
import plotly.express as px
import pandas as pd


def main(params: dict, context: Context):
    df = params.get("df")
    assert df is not None
    title = params.get("chart_title")
    label = params.get("label")
    value = params.get("value")

    if title is None:
        title = "Pie Chart"
    if label is None:
        label = df.columns[0]
    if value is None:
        value = df.columns[1]

    fig = px.pie(df, values=value, names=label, title=title)

    fig.show()

    return {"df": df}
