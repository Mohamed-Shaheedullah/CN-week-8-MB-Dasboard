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
    from .models import Megabytes, read_excel_to_database 
    with app.app_context():
        db.create_all()
        if app.debug: # REMOVE OR CHANGE WHEN DEPLOY********************
            read_excel_to_database("mb_all.xlsx")

    return app
