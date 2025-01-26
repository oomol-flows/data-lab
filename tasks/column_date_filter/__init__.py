from oocana import Context
import pandas as pd

def main(params: dict, context: Context):
  df = params.get("df")
  start_date = params.get("start_date")
  end_date = params.get("end_date")
  assert df is not None and start_date is not None and end_date is not None, "Missing required parameters"
  name = params.get("column_name")
  df[name] = pd.to_datetime(df[name])
  start_date = pd.to_datetime(start_date)
  end_date = pd.to_datetime(end_date)
  filtered_df_range = df[(df[name] >= start_date) & (df[name] <= end_date)]

  preview_df = filtered_df_range
  preview_df[name] = preview_df[name].dt.strftime('%Y-%m-%d %H:%M:%S')
  context.preview(preview_df)
  return { "df": filtered_df_range }