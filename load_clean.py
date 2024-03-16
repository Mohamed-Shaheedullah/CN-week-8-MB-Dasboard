import pandas as pd
# from ydata_profiling import ProfileReport
import matplotlib.pyplot as plt
import openpyxl
import numpy as np
from flask import current_app  # Import to access the app instance
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Initialize outside of the app context 


filepath_base = "./megabytes_data/"
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Create an empty DataFrame to store all the data
df_all = pd.DataFrame()

for day in days:
    filename = filepath_base + day.lower() + "_graph.xlsx"
    df = pd.read_excel(filename)
    df['Day'] = day  # Assign the day of the week
    df_all = pd.concat([df_all, df])  # Add to the combined DataFrame


## check for duplicates
duplicate_values = df_all.duplicated()
print(duplicate_values.value_counts())
## no dupes

df_all = df_all.dropna(how="any")

df.index.name = 'mb_index' 

df_all.to_excel("mb_all.xlsx")


