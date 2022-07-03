from flask import Blueprint

weatherRoute = Blueprint('weather',__name__)

@weatherRoute.route("/weather")
def home():
    return "<h2>weather route</h2>"