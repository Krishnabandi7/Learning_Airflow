import pandas as pd
from datetime import datetime

def filter_function():
    print("Apply Filter condition")
    df=pd.read_csv("in_file/Athletes_cleaned.csv")
    df= df[df['PersonName'].str.startswith("A")]
    df.to_csv("ot_file/Athletes_filtered.csv")
    print("file is cleaned and date is added in file")
