from typing import Dict

import pandas as pd

COLUMNS = ["field_1", "field_2"]


def extract_fields(extracted_texts: Dict[str, str]) -> pd.DataFrame:
    fields_df = pd.DataFrame(index=list(extracted_texts), columns=COLUMNS)
    return fields_df
