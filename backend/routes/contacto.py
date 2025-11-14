from flask import Blueprint, flash, redirect, request, render_template, url_for
from ..models import Contact
from ..config.config_db import db

contacto_bp = Blueprint("contacto", __name__)

@contacto_bp.route("/contacto", methods=["GET", "POST"])
def contacto():
    if request.method == "POST":
        if request.form.get("antispam"):
            # Home
            return redirect(url_for("index.index"))

        try:

            data = request.form
            print("data:", data)
            new_contact = Contact.from_json(data)
            db.session.add(new_contact)
            db.session.commit()

        except Exception as e:
            print(e)
            flash("Error al enviar el mensaje", "error")

                
        

    
        flash("Mensaje enviado correctamente. ¡Gracias por contactarnos!", "success")
        # Vuelve a /contacto
        return redirect(url_for("contacto.contacto"))

    if request.headers.get("HX-Request"):
        return render_template("partials/contacto.html")
    return render_template("contacto.html")
