from oocana import Context
import plotly.express as px

def main(params: dict, context: Context):
    df = params.get("df")
    assert df is not None

    first_column_name = df.columns[0]
    categories = df.columns[1:]

    fig = px.area(
        df,
        x=first_column_name,
        y=categories,
        title="Stacked Area Chart",
        labels={"value": "Value", "variable": "Category"},
        color_discrete_sequence=px.colors.qualitative.Pastel,
    )

    fig.update_layout(
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.3,
            xanchor="center",
            x=0.5,
        ),
    )

    fig.show()
