from oocana import Context
import pandas as pd
import plotly.express as px


def main(params: dict, context: Context):
    title = params.get("chart_title")
    df = params.get("df")

    if title is None:
        title = "Bar Chart"


    # 使用 Plotly Express 创建柱状图
    fig = px.bar(
        df,
        x="Labels",
        y="Values",
        title=title,
        color="Labels",
        color_discrete_sequence=px.colors.qualitative.Plotly,
    )

    # 显示图表
    fig.show()

    return {"df": df}
