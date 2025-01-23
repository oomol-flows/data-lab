from oocana import Context
import plotly.express as px


def main(params: dict, context: Context):
    title = params.get("chart_title")
    df = params.get("df")
    assert df is not None
    x_column = params.get("x_column")
    y_column = params.get("y_column")

    if title is None:
        title = "Bar Chart"
    if x_column is None:
        x_column = df.columns[0] 
    if y_column is None:
        y_column = df.columns[1]


    fig = px.bar(
        df,
        x=x_column,
        y=x_column,
        title=title,
        color=x_column,
        color_discrete_sequence=px.colors.qualitative.Plotly,
    )

    fig.show()

    return {"df": df}
