# 📘 Proyecto: Backend To-Do App (Flask + SQLAlchemy)

Este proyecto enseña cómo construir un backend paso a paso para una aplicación de tareas usando **Flask**, **Jinja2** y **SQLAlchemy**. Cada rama representa una etapa del desarrollo.

---

## 🔰 `01 - Configuración inicial`

🔗 [📦 Descargar esta rama](https://github.com/lnvaldez/web-wk/archive/refs/heads/backend-01-setup.zip)

🎯 Objetivo

- Crear una aplicación Flask mínima
- Mostrar "Hola mundo" en el navegador
- Verificar que Flask esté funcionando correctamente

---

## 🖼️ `02 - Plantillas con Jinja2`

🔗 [📦 Descargar esta rama](https://github.com/lnvaldez/web-wk/archive/refs/heads/backend-02-template.zip)

🎯 Objetivo

- Renderizar una plantilla HTML con `render_template`
- Crear archivo `index.html`
- Usar Jinja2 para mostrar una lista simulada de tareas (mock) con `{% for %}`

---

## 📝 `03 - Manejo de formularios`

🔗 [📦 Descargar esta rama](https://github.com/lnvaldez/web-wk/archive/refs/heads/backend-03-form-handling.zip)

🎯 Objetivo

- Crear un formulario HTML para nuevas tareas
- Enviar datos al servidor con `POST`
- Capturar los datos con `request.form`
- Guardar la tarea en una lista temporal (`tareas = []`)
- Redirigir a `/` luego del envío

---

## 💾 `04 - Conexión con base de datos`

🔗 [📦 Descargar esta rama](https://github.com/lnvaldez/web-wk/archive/refs/heads/backend-04-sqlalchemy.zip)

🎯 Objetivo

- Reemplazar la lista `tareas = []` por una base de datos real
- Usar SQLite con SQLAlchemy
- Crear tabla `Tarea`
- Mostrar todas las tareas en `index.html`
- Insertar nuevas tareas desde el formulario
- Sin editar ni eliminar todavía

---

## 🔁 `05 - CRUD básico con base de datos`

🔗 [📦 Descargar esta rama](https://github.com/lnvaldez/web-wk/archive/refs/heads/backend-05-crud-db.zip)

🎯 Objetivo

- Agregar funcionalidad para eliminar tareas con botón `Eliminar`
- Agregar funcionalidad para marcar tareas como completadas con checkbox
- Actualizar el campo `completada` en la base de datos
- Eliminar usando método `POST`
- No se incluye edición del título

---

## 🧱 `06 - Arquitectura MVC modular`

🔗 [📦 Descargar esta rama](https://github.com/lnvaldez/web-wk/archive/refs/heads/backend-06-mvc.zip)

🎯 Objetivo

- Reorganizar el proyecto con una arquitectura MVC básica
- Separar archivos en:

  - `models/` → definición de `Tarea`
  - `controllers/` → funciones como `crear_tarea`, `eliminar_tarea`, etc.
  - `routes/` → define las rutas y llama a las funciones del controlador
  - `database/` → contiene el objeto `db`

- Dejar `app.py` limpio, solo con configuración y arranque

---

¡Explorá cada rama para avanzar paso a paso en la construcción de tu backend! 💡
