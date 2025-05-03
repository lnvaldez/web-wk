from controllers import tareas_controller

def registrar_rutas(app):
    app.add_url_rule("/", view_func=tareas_controller.obtener_tareas, methods=["GET"])
    app.add_url_rule("/crear-tarea", view_func=tareas_controller.crear_tarea, methods=["POST"])
    app.add_url_rule("/eliminar-tarea/<int:id>", view_func=tareas_controller.eliminar_tarea, methods=["POST"])
    app.add_url_rule("/cambiar-estado/<int:id>", view_func=tareas_controller.cambiar_estado, methods=["POST"])
