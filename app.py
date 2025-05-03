from flask import Flask, render_template

app = Flask(__name__)

tareas = [
    {
        "titulo": "Comprar lechuga",
        "fecha": "2025-05-05",
        "descripcion": "Ir al super y comprar lechuga",
        "email": "lucas@ejemplo.com",
    },
    {
        "titulo": "Estudiar Flask",
        "fecha": "2025-05-06",
        "descripcion": "Nde tavyyyyy",
        "email": "lucas@ejemplo.com",
    },
]

@app.route("/")
def home():
    return render_template("index.html", tareas=tareas)

if __name__ == "__main__":
    app.run(debug=True)