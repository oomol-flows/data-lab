from oocana import Context

def main(params: dict, context: Context):
  df = params.get("df")
  preview = params.get("preview")
  assert df is not None
  name = params.get("column_name")
  sort_type = params.get("sort_type")
  sorted_df = None
  if sort_type == "Ascending":
    sorted_df = df.sort_values(by=name)
  else:
     sorted_df = df.sort_values(by=name, ascending=False)

  if preview is True:
    context.preview(sorted_df)
  return { "df": sorted_df }