from oocana import Context
import pandas as pd

def main(params: dict, context: Context):
  df = params.get("df")
  if df is not None:
       context.preview(df)

  return { "df": df }
