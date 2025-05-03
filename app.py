from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuracion de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tareas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de datos
class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.String(20), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    email = db.Column(db.String(100), nullable=False)
    completada = db.Column(db.Boolean, default=False)

"""
Creamos las tablas la primera vez que se corre la app.
Usamos "app.app_context()" porque esta línea está fuera de cualquier ruta,
y Flask necesita saber qué aplicación está activa para poder crear la base de datos.
Esto evita el error "RuntimeError: Working outside of application context".
"""

with app.app_context():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
def home():
    tareas = Tarea.query.all()
    return render_template("index.html", tareas=tareas)

@app.route("/crear-tarea", methods=["POST"])
def crear_tarea():
    nueva_tarea = Tarea(
        titulo = request.form["titulo"],
        fecha = request.form["fecha"],
        descripcion = request.form["descripcion"],
        email = request.form["email"]
    )
    db.session.add(nueva_tarea)
    db.session.commit()
    return redirect("/")

@app.route("/eliminar-tarea/<int:id>", methods=["POST"])
def eliminar_tarea(id):
    tarea = Tarea.query.filter_by(id=id).first()
    db.session.delete(tarea)
    db.session.commit()
    return redirect("/")

@app.route("/cambiar-estado/<int:id>", methods=["POST"])
def cambiar_estado(id):
    tarea = Tarea.query.filter_by(id=id).first()
    tarea.completada = not tarea.completada
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)