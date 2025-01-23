from cProfile import label
from oocana import Context
import plotly.express as px
import pandas as pd


def main(params: dict, context: Context):
    df = params.get("df")
    title = params.get("chart_title")
    if title is None:
        title = "Pie Chart"

    # 使用 Plotly Express 创建饼图
    fig = px.pie(df, values='Values', names='Labels', title=title)

    fig.show()

    return {"df": df}
