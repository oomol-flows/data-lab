from oocana import Context
import pandas as pd


def main(params: dict, context: Context):
    csv = params.get("csv")
    assert csv is not None
    df = pd.read_csv(csv)
    return {"df": df}
