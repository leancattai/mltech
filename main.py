# main.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask import send_from_directory
from datetime import datetime
from backend.routes import init_routes
from backend.dev import init_dev_routes
from backend.config.config_db import init_db
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

init_routes(app)
init_dev_routes(app)
init_db(app)




# Ejecución local
if __name__ == "__main__":
    app.run(debug=True)



