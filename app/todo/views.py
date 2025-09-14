import random
import string
from datetime import datetime

from flask import jsonify, render_template

from . import todo


@todo.route("/")
@todo.route("/index")
def index():
    html = cur_date()
    return render_template("index.html", user=name_generator(), data=html)


@todo.route("/showjson")
def showJSON():
    return jsonify(
        greeting=["hello", "world"],
        date=datetime.today(),
    )


@todo.route("/curdate")
def curDate():
    html = cur_date()
    return html


def cur_date():
    html = ""
    for i in range(10):
        html += f"<b>TODO: {i}</b> </br>"
    html += f"Current date: {datetime.today()}"
    return html


def name_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))
