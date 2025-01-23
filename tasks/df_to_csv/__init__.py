from typing import Optional
import pandas as pd
from oocana import Context


def main(inputs: dict, context: Context) -> dict:
    df: Optional[pd.DataFrame] = inputs.get("df")
    csv_address: Optional[str] = inputs.get("csv_address")
    name: Optional[str] = inputs.get("name")

    if df is None:
        raise ValueError("df is required")

    # Save DataFrame to CSV
    if csv_address is None:
        csv_address = context.session_dir
    if name is None:
        name = "df"
    csv_address = f"{csv_address}/{name}.csv"

    try:
        df.to_csv(csv_address, index=False)
    except Exception as e:
        raise RuntimeError(f"Failed to save DataFrame to CSV: {e}")

    return {"csv": csv_address}
