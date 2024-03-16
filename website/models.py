from . import db
from sqlalchemy.sql import func
import datetime

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

