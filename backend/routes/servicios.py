from flask import Blueprint, render_template, request


servicios_bp = Blueprint("servicios", __name__)


@servicios_bp.route("/servicios", methods=["GET", "POST"])
def servicios():
    if request.headers.get("HX-Request"):
        return render_template("partials/servicios.html")
    return render_template("servicios.html")
