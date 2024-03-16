from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from .models import Megabytes  # gives rise to circular import
import pandas as pd
import openpyxl

# from .load_clean import read_excel_to_database, db  # Import your functions 

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    db.init_app(app)
    from .views import my_view
    app.register_blueprint(my_view)
    from .models import Megabytes
    with app.app_context():
        db.create_all()
        read_excel_to_database("mb_all.xlsx")
    return app

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
