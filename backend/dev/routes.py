from flask import Blueprint, render_template
from flask import current_app as app
dev_bp = Blueprint("dev", __name__, url_prefix="/dev")



@dev_bp.route("/dev")

def _gather_routes():
    """
    Recorre app.url_map y construye una lista de rutas legible.
    Ignora static por defecto.
    """
    routes = []
    for rule in app.url_map.iter_rules():
        # ignorar archivos estáticos si querés
        if rule.endpoint == 'static':
            continue

        # filtrar métodos utilitarios
        methods = sorted([m for m in rule.methods if m not in ("HEAD", "OPTIONS")])

        # intentar obtener la docstring de la view function
        view_fn = app.view_functions.get(rule.endpoint)
        doc = ""
        if view_fn and view_fn.__doc__:
            doc = view_fn.__doc__.strip().splitlines()[0]

        routes.append({
            "rule": str(rule),
            "endpoint": rule.endpoint,
            "methods": methods,
            "doc": doc
        })
    # ordenar por regla para mayor claridad
    routes = sorted(routes, key=lambda r: r["rule"])
    return routes