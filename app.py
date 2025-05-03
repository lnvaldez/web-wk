from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tareas = []

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        nueva_tarea = {
            "titulo": request.form["titulo"],
            "fecha": request.form["fecha"],
            "descripcion": request.form["descripcion"],
            "email": request.form["email"],
        }
        tareas.append(nueva_tarea)
        return redirect("/")

    return render_template("index.html", tareas=tareas)

if __name__ == "__main__":
    app.run(debug=True)