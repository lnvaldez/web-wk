from models.tarea import Tarea
from database.db import db
from flask import request, redirect, render_template

def obtener_tareas():
    tareas = Tarea.query.all()
    return render_template("index.html", tareas=tareas)

def crear_tarea():
    nueva_tarea = Tarea(
        titulo=request.form["titulo"],
        fecha=request.form["fecha"],
        descripcion=request.form["descripcion"],
        email=request.form["email"]
    )
    db.session.add(nueva_tarea)
    db.session.commit()
    return redirect("/")

def eliminar_tarea(id):
    tarea = Tarea.query.filter_by(id=id).first()
    db.session.delete(tarea)
    db.session.commit()
    return redirect("/")

def cambiar_estado(id):
    tarea = Tarea.query.filter_by(id=id).first()
    tarea.completada = not tarea.completada
    db.session.commit()
    return redirect("/")