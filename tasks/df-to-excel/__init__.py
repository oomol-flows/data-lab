from oocana import Context

def main(params: dict, context: Context):
  df = params.get("df")
  save_dir = params.get("save_dir")
  name = params.get("name")
  assert df is not None
  if save_dir is None:
    save_dir = context.session_dir
  if name is None:
    name = "output.xlsx"
  address = f"{save_dir}/{name}"
  df.to_excel(address, index=False)
  return { "address": address }
