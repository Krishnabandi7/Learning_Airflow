import os
import pandas as pd
from datetime import datetime

def pre_process():
    print("Before adding date column...")

    # Define absolute paths
    input_path = "in_file/Athletes.csv"
    output_path = "in_file/Athletes_cleaned.csv"

    # Check if the file exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    # Read the CSV file
    df = pd.read_csv(input_path)

    # Add process date column
    df["process_date"] = datetime.today().date()

    # Fill missing values
    df.fillna("", inplace=True)

    # Save the cleaned file
    df.to_csv(output_path, index=False)

    print("✅ File is cleaned and saved successfully.")