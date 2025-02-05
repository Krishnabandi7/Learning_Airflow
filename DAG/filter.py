import pandas as pd
from datetime import datetime

def filter_function():
    print("Apply Filter condition")
    #read file from the location
    df=pd.read_csv("in_file/Athletes_cleaned.csv")
    #filter the data we want
    df= df[df['PersonName'].str.startswith("A")]
    #store the Transformed data in the form of csv file in some location
    df.to_csv("ot_file/Athletes_filtered.csv")
    print("file is cleaned and date is added in file")
