# src/app.py
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# INYECCIÓN GLOBAL PARA {{ now.year }}
@app.context_processor
def inject_now():
    return {'now': datetime.now()}

# RUTAS PRINCIPALES
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
    return render_template("contacto.html")

# EJECUCIÓN LOCAL
if __name__ == "__main__":
    app.run(debug=True)
