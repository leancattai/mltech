from ..config.config_db import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(30), nullable=False)
    empresa = db.Column(db.String(255), nullable=False)
    area_interes = db.Column(db.String(255), nullable=False)
    presupuesto = db.Column(db.String(255), nullable=False)
    message = db.Column(db.Text, nullable=False)
    is_read = db.Column(db.Boolean, default=False)

    def to_json(self):
        return {
            'name': self.name,
            'email': self.email,
            'telefono': self.telefono,
            'empresa': self.empresa,
            'area_interes': self.area_interes,
            'presupuesto': self.presupuesto,
            'message': self.message
        }
    
    def from_json(data):
        return Contact(
            name=data.get('name'),
            email=data.get('email'),
            telefono=data.get('telefono'),
            empresa=data.get('empresa'),
            area_interes=data.get('area_interes'),
            presupuesto=data.get('presupuesto'),
            message=data.get('message')
        )
    
    def __repr__(self):
        return '<Contact %r>' % self.id