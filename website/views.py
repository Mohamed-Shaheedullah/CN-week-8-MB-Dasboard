from flask import Flask, Blueprint, render_template, request, redirect, url_for
from sqlalchemy.sql import func
from .models import Megabytes
from . import db

my_view = Blueprint("my_view", __name__)

@my_view.route("/")
def home():
    # mega_list = Megabytes.query.all()    # returns list of objects
    total_cost = db.session.query(func.sum(Megabytes.cost)).scalar()
    max_cost = db.session.query(func.max(Megabytes.cost)).scalar()
    # https://stackoverflow.com/questions/1052148/group-by-count-function-in-sqlalchemy
    staff_cost_sums = db.session.query(Megabytes.staff,
                                        func.sum(Megabytes.cost).
                                        label('total_cost')).group_by(Megabytes.staff).all()
    er_message = request.args.get("er_message", None)
    return render_template("index.html", total_cost=total_cost,
                           max_cost=max_cost,
                            staff_cost_sums=staff_cost_sums,
                            er_message=er_message)