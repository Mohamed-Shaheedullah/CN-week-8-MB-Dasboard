from . import db
from sqlalchemy.sql import func
import datetime
import pandas as pd
import openpyxl

# this is where database (schema?) is defined

class Megabytes(db.Model):
    mb_index = db.Column(db.Integer, primary_key = True)
    transaction_id = db.Column(db.Integer)
    staff = db.Column(db.String(300))
    transaction_type = db.Column(db.String(300))
    basket = db.Column(db.String(600))
    total_items = db.Column(db.Integer)
    cost = db.Column(db.Float)
    payment_method = db.Column(db.String(300))
    day_of_week = db.Column(db.String(300))


def read_excel_to_database(file_path):
    # Read Excel file (adjust engine if using xlrd)
    df_db = pd.read_excel(file_path, engine='openpyxl')
    df_db.rename(columns={'Unnamed: 0': 'mb_index'}, inplace=True)

    # Iterate over DataFrame rows
    for index, row in df_db.iterrows():
        # Create a new Megabyte instance
        from .models import Megabytes
        megabyte = Megabytes(
            transaction_id = row["Transaction ID"],
            staff = row["Staff"],
            transaction_type = row["Transaction Type"],
            basket = row["Basket"],
            total_items = row["Total Items"],
            cost = row["Cost"],
            payment_method = row["Payment Method"],
            day_of_week = row["Day"]
            )
        # Add and commit to the database
        db.session.add(megabyte)
        db.session.commit()
