from oocana import Context
import pandas as pd
import plotly.express as px


def main(params: dict, context: Context):
    df = params.get("df")
    title = params.get("chart_title")

    if title is None:
        title = "Line Chart"


    # 使用 Plotly Express 创建柱状图
    fig = px.line(
        df,
        x="Labels",
        y="Values",
        title=title,
        markers=True ,
    )

    fig.show()

    return {"df": df}
