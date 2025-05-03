from flask import Flask
from database.db import db
from routes.tareas_routes import registrar_rutas

def crear_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tareas.db'
    db.init_app(app)

    with app.app_context():
        from models.tarea import Tarea
        db.create_all()

    registrar_rutas(app)
    return app

app = crear_app()

if __name__ == '__main__':
    app.run(debug=True)
