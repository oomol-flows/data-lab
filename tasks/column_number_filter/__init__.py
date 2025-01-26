from oocana import Context

def main(params: dict, context: Context):

  df = params.get("df")
  assert df is not None
  name = params.get("column_name")
  min_threshold = params.get("min_threshold")
  max_threshold = params.get("max_threshold")
  preview = params.get("preview")
  filtered_df = df[(df[name] > min_threshold) & (df[name] < max_threshold)]
  if preview is True:
    context.preview(filtered_df)
  return { "df": filtered_df }