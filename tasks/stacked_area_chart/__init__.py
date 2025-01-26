from oocana import Context
import plotly.express as px

def main(params: dict, context: Context):
    df = params.get("df")
    assert df is not None
    title = params.get("chart_title")
    x_column = params.get("x_column")
    y_columns = params.get("y_columns")

    if title is None:
        title = "Stacked Area Chart"
    if x_column is None:
        x_column = df.columns[0]
    if y_columns is None:
        y_columns = df.columns[1:]

    fig = px.area(
        df,
        x=x_column,
        y=y_columns,
        title=title,
        color_discrete_sequence=px.colors.qualitative.Pastel,
    )
    fig.update_layout(title_text=title, title_x=0.5)

    fig.show()
