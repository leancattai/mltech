from .routes import dev_bp
from flask import Flask

def init_dev_routes(app : Flask):
    app.register_blueprint(dev_bp)