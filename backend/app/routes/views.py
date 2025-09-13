from flask import Blueprint

# name, import_name (fixed order)
views = Blueprint("views", __name__)

@views.route("/")
def home():
    return "Homepage...O"
