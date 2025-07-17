# main.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask import send_from_directory
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # necesaria para usar flash messages

# Inyección global para {{ now.year }} y SITE_URL
@app.context_processor
def inject_now():
    return {
        'now': datetime.now(),
        'SITE_URL': os.environ.get("SITE_URL", "http://127.0.0.1:5000")
    }

# Rutas principales con soporte HTMX
@app.route("/")
def index():
    if request.headers.get("HX-Request"):
        return render_template("partials/index.html")
    return render_template("index.html")



@app.route("/servicios")
def servicios():
    if request.headers.get("HX-Request"):
        return render_template("partials/servicios.html")
    return render_template("servicios.html")


@app.route("/portfolio")
def portfolio():
    if request.headers.get("HX-Request"):
        return render_template("partials/portfolio.html")
    return render_template("portfolio.html")


@app.route("/quienes-somos")
def quienes_somos():
    if request.headers.get("HX-Request"):
        return render_template("partials/quienes-somos.html")
    return render_template("quienes-somos.html")


@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    if request.method == "POST":
        if request.form.get("antispam"):
            return redirect(url_for("index"))

        nombre = request.form.get("nombre")
        email = request.form.get("email")
        mensaje = request.form.get("mensaje")

        flash("Mensaje enviado correctamente. ¡Gracias por contactarnos!", "success")
        return redirect(url_for("contacto"))

    if request.headers.get("HX-Request"):
        return render_template("partials/contacto.html")
    return render_template("contacto.html")


# Página 404
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

# Archivos robots.txt y sitemap.xml
@app.route("/robots.txt")
def robots():
    return send_from_directory("static", "robots.txt", mimetype="text/plain")

@app.route("/sitemap.xml")
def sitemap():
    return send_from_directory("static", "sitemap.xml", mimetype="application/xml")

# Ejecución local
if __name__ == "__main__":
    app.run(debug=True)
