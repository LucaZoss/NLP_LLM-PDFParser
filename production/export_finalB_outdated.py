from pathlib import Path
import pandas as pd


def fields_to_csv(extracted_fields: pd.DataFrame,
                  save_path: Path = Path("/Users/lucazosso/Desktop/IE_Course/Hackathon/production/csv_export/predictions.csv")) -> None:
    try:
        print("Attempting to save CSV...")
        print(f"Save Path: {save_path}")
        print("Extracted Fields:")
        print(extracted_fields.head())  # Print first few rows of the DataFrame

        # Ensure the underlyings and strikes are lists
        for col in ["Underlying(s)", "Strike"]:
            extracted_fields[col] = extracted_fields[col].apply(
                lambda x: x if isinstance(x, list) else [x])

        # Reshape the underlyings and strikes into separate columns
        for col_prefix in ["Underlying(s)", "Strike"]:
            max_length = max(extracted_fields[col_prefix].apply(len))
            for i in range(max_length):
                extracted_fields[f"{col_prefix}_{
                    i+1}"] = extracted_fields[col_prefix].apply(lambda x: x[i] if i < len(x) else None)

            # Drop the original column
            extracted_fields.drop(col_prefix, axis=1, inplace=True)

        extracted_fields.to_csv(save_path)
        print(f"CSV file saved successfully at {save_path}")

        if save_path.exists():
            print(f"File exists at {save_path}")
        else:
            print(f"File not found at {save_path}")
    except Exception as e:
        print(f"Error occurred while saving file: {e}")
