from .contacto import contacto_bp
from .index import index_bp
from .nosotros import nosotros_bp
from .portfolio import portfolio_bp
from .servicios import servicios_bp
from .utils import utils_bp
from flask import Blueprint, Flask

def init_routes(app : Flask):
    app.register_blueprint(contacto_bp)
    app.register_blueprint(index_bp)
    app.register_blueprint(nosotros_bp)
    app.register_blueprint(portfolio_bp)
    app.register_blueprint(servicios_bp)
    app.register_blueprint(utils_bp)