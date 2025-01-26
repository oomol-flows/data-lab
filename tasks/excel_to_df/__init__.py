from oocana import Context
import pandas as pd


def main(params: dict, context: Context):
    xlsx = params.get("xlsx")
    assert xlsx is not None
    df = pd.read_excel(xlsx)
    return {"df": df}
