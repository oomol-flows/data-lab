from oocana import Context


def main(params: dict, context: Context):

    df = params.get("df")
    preview = params.get("preview")
    assert df is not None
    column_name = params.get("column_name")
    new_df = df
    if column_name is not None:
        new_df = df.drop(columns=[column_name])
    if preview is True:
        context.preview(new_df)
    return {"df": new_df}

