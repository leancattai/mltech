from flask import render_template, Blueprint, send_from_directory

utils_bp = Blueprint("utils", __name__)


# Página 404
@utils_bp.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

# Archivos robots.txt y sitemap.xml
@utils_bp.route("/robots.txt")
def robots():
    return send_from_directory("static", "robots.txt", mimetype="text/plain")

@utils_bp.route("/sitemap.xml")
def sitemap():
    return send_from_directory("static", "sitemap.xml", mimetype="application/xml")
