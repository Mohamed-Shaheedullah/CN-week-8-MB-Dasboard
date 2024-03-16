import pandas as pd
from ydata_profiling import ProfileReport
import openpyxl
import numpy as np

df1 = pd.read_excel(r"./megabytes_data/wednesday_graph.xlsx")


# profile = ProfileReport(df1, title="Monday Profile")

# profile.to_file('monday_report_ydata.html')


df1 = df1.dropna(how="any")


df1 = df1.drop(columns=["Unnamed: 0"])


# print(df1.info())

# print(df1.describe())

print(df1["Payment Method"].value_counts())
# print(df1.groupby("Payment Method").sum("Cost"))


# total_payments = df1.groupby('Payment Method')['Cost'].sum()
# print(total_payments)
