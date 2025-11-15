from flask import Blueprint, request, render_template

index_bp = Blueprint("index", __name__, )


@index_bp.route("/")
def index():
    if request.headers.get("HX-Request"):
        return render_template("partials/index.html")
    return render_template("index.html")
