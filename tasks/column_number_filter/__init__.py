from oocana import Context

def main(params: dict, context: Context):
    
    df = params.get("df")
    if df is None or df.empty:
        raise ValueError("Input dataframe cannot be None or empty")
        
    name = params.get("column_name")
    if not name or name not in df.columns:
        raise ValueError(f"Invalid column name: {name}")
        
    min_threshold = params.get("min_threshold")
    max_threshold = params.get("max_threshold")
    if min_threshold is None or max_threshold is None:
        raise ValueError("Threshold values cannot be None")
        
    try:
        filtered_df = df[(df[name] > min_threshold) & (df[name] < max_threshold)]
        preview = params.get("preview")
        if preview is True:
            context.preview(filtered_df)
        return { "df": filtered_df }
    except Exception as e:
        raise ValueError(f"Error filtering dataframe: {str(e)}")