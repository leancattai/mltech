from flask import Blueprint, render_template, request


portfolio_bp = Blueprint("portfolio", __name__)

@portfolio_bp.route("/portfolio", methods=["GET", "POST"])
def portfolio():
    if request.headers.get("HX-Request"):
        return render_template("partials/portfolio.html")
    return render_template("portfolio.html")
