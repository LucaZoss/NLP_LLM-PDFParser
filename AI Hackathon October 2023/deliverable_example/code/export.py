from pathlib import Path

import pandas as pd


def fields_to_csv(extracted_fields: pd.DataFrame, save_path: Path = Path("./predictions.csv")) -> None:
    extracted_fields.to_csv(save_path)
