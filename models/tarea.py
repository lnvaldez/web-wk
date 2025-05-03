from database.db import db

class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.String(20), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    email = db.Column(db.String(100), nullable=False)
    completada = db.Column(db.Boolean, default=False)
