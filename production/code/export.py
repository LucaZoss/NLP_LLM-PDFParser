from pathlib import Path
import pandas as pd


def fields_to_csv(extracted_fields: pd.DataFrame,
                  save_path: Path = Path("/Users/lucazosso/Desktop/IE_Course/Hackathon/production/csv_export/predictions_LL_Final.csv")) -> None:
    try:
        print("Attempting to save CSV...")
        print(f"Save Path: {save_path}")
        print("Extracted Fields:")
        print(extracted_fields.head())  # Print first few rows of the DataFrame

        # Ensure the underlyings and strikes are lists
        for col in ["Underlying(s)", "Strike"]:
            extracted_fields[col] = extracted_fields[col].apply(
                lambda x: x if isinstance(x, list) else [x])

        # Desired column order
        desired_order = ["PDF ID", "ISIN", "Issuer", "Currency", "Underlying(s)", "Strike",
                         "Launch Date", "Final Valuation Day",
                         "Maturity", "Cap", "Barrier"]

        # Filter out any columns that are not in the DataFrame
        desired_order = [
            col for col in desired_order if col in extracted_fields.columns]

        # Reorder DataFrame
        extracted_fields = extracted_fields[desired_order]

        # Set index=False to avoid saving the index column
        extracted_fields.to_csv(save_path, index=False)
        print(f"CSV file saved successfully at {save_path}")

        if save_path.exists():
            print(f"File exists at {save_path}")
        else:
            print(f"File not found at {save_path}")
    except Exception as e:
        print(f"Error occurred while saving file: {e}")
