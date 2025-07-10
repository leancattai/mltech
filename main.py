# main.py
from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # necesaria para usar flash messages

# Inyección global para {{ now.year }}
@app.context_processor
def inject_now():
    return {'now': datetime.now(),
            'SITE_URL': os.environ.get("SITE_URL", "http://127.0.0.1:5000")}

# Rutas principales
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/servicios")
def servicios():
    return render_template("servicios.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/quienes-somos")
def quienes_somos():
    return render_template("quienes-somos.html")

@app.route("/contacto", methods=["GET", "POST"])
def contacto():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        email = request.form.get("email")
        mensaje = request.form.get("mensaje")
        
        # Acá podrías guardar en base de datos, enviar email, etc.
        flash("Mensaje enviado correctamente. ¡Gracias por contactarnos!", "success")
        return redirect(url_for("contacto"))

    return render_template("contacto.html")

# Ejecución local
if __name__ == "__main__":
    app.run(debug=True)
