from flask import Flask, Blueprint, render_template, request, redirect, url_for

from .models import Todo
from . import db
my_view = Blueprint("my_view", __name__)

@my_view.route("/")
def home():
    todo_list = Todo.query.all()    # returns list of objects
    # print(todo_list)
    er_message = request.args.get("er_message", None)
    return render_template("index.html", todo_list = todo_list, er_message=er_message)