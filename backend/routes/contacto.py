from flask import Blueprint, flash, redirect, request, render_template, url_for

contacto_bp = Blueprint("contacto", __name__)

@contacto_bp.route("/contacto", methods=["GET", "POST"])
def contacto():
    if request.method == "POST":
        if request.form.get("antispam"):
            # Home
            return redirect(url_for("index.index"))

        nombre = request.form.get("nombre")
        email = request.form.get("email")
        mensaje = request.form.get("mensaje")

        flash("Mensaje enviado correctamente. ¡Gracias por contactarnos!", "success")
        # Vuelve a /contacto
        return redirect(url_for("contacto.contacto"))

    if request.headers.get("HX-Request"):
        return render_template("partials/contacto.html")
    return render_template("contacto.html")
