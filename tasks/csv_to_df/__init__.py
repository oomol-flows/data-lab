from oocana import Context
import pandas as pd


def main(params: dict, context: Context):
    csv_path = params.get("csv")
    if csv_path is None:
        raise ValueError("csv is required")
    df = pd.read_csv(csv_path)
    return {"df": df}
