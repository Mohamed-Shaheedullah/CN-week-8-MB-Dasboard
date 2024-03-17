from flask import Flask, Blueprint, render_template, request, redirect, url_for

from .models import Megabytes
from . import db
my_view = Blueprint("my_view", __name__)

@my_view.route("/")
def home():
    mega_list = Megabytes.query.all()    # returns list of objects
    er_message = request.args.get("er_message", None)
    return render_template("index.html", mega_list = mega_list, er_message=er_message)