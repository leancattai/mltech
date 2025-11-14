from flask import Blueprint, request, render_template


nosotros_bp = Blueprint("nosotros", __name__)


@nosotros_bp.route("/quienes-somos", methods=["GET", "POST"])
def quienes_somos():
    if request.headers.get("HX-Request"):
        return render_template("partials/quienes-somos.html")
    return render_template("quienes-somos.html")

