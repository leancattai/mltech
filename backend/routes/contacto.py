import os
from flask import Blueprint, flash, redirect, request, render_template, url_for
from ..models import Contact
from ..utils.send_message import send_message_whatsapp
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
            new_contact = Contact.from_json(data)
            db.session.add(new_contact)
            db.session.commit()

        except Exception as e:
            print(e)
            flash("Error al guardar la informacion en base de datos", "error")

        try:

            message = f""" Nuevo mensaje de contacto M&L Tech\n{data.get('name')} con email: {data.get('email')}, telefono: {data.get('telefono')}, quiere consultar sobre {data.get('area_interes')} con presupuesto de {data.get('presupuesto')} y dejo el siguiente mensaje: \n{data.get('message')}\n\nPara o rechazar este pedido ingresar al apartado de back office y darle a Aceptar o Rechazar."""
   
            phone_number_mariano = os.getenv('PHONE_NUMBER_MARIANO')
            phone_number_leandro = os.getenv('PHONE_NUMBER_LEANDRO')

            send_message_whatsapp(phone_number_mariano, message)
            send_message_whatsapp(phone_number_leandro, message)

        except Exception as e:
            print(e)
            flash("Error al enviar el mensaje por WhatsApp", "error")    
        

    
        flash("Mensaje enviado correctamente. ¡Gracias por contactarnos!", "success")
        # Vuelve a /contacto
        return redirect(url_for("contacto.contacto"))

    if request.headers.get("HX-Request"):
        return render_template("partials/contacto.html")
    return render_template("contacto.html")
