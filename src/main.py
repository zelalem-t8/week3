from src.data_load import load_data
import pandas as pd
import os

if __name__ == "__main__":
    file_path = "data/MachineLearningRating_v3.txt"
    data = load_data(file_path)

    # Clean numeric strings with commas
    for col in data.columns:
        if data[col].dtype == 'object':
            # Remove thousand-separators and spaces
            data[col] = data[col].str.replace(',', '', regex=False)
            data[col] = data[col].str.strip()
            # Try converting to number
            try:
                data[col] = pd.to_numeric(data[col])
            except:
                continue  # Leave as string if conversion fails

    # Save cleaned data as Parquet
    parquet_path = "data/model_input.parquet"
    data.to_parquet(parquet_path, index=False)

    if not data.empty:
        print("✅ Data loaded and saved to Parquet:")
        print(data.head())
    else:
        print("⚠️ No data loaded.")
