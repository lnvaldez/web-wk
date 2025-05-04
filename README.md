# 🎯 Objetivos:

- Reorganizar el proyecto con una arquitectura MVC básica
- Separar archivos en:

  - `models/` → definición de `Tarea`
  - `controllers/` → funciones como `crear_tarea`, `eliminar_tarea`, etc.
  - `routes/` → define las rutas y llama a las funciones del controlador
  - `database/` → contiene el objeto `db`

- Dejar `app.py` limpio, solo con configuración y arranque
