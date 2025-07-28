from flask import Flask, render_template

app = Flask(__name__)

camisetas = [
    {"id": 1, "nombre": "Camiseta básica", "precio": 200, "imagen": "/static/img/playera-personalizada.jpg"},
]

tote_bags = [
    {"id": 1, "nombre": "Tote bag ecológica", "precio": 180, "imagen": "/static/img/totebag.jpg"},
]

tazas = [
    {"id": 1, "nombre": "Taza con diseño", "precio": 120, "imagen": "/static/img/taza-personalizada.jpg"},
]

gorras = [
    {"id": 1, "nombre": "Gorra bordada", "precio": 150, "imagen": "/static/img/gorra-personalizada.jpg"},
]

@app.route("/")
def index():
    return render_template(
        "index.html",
        camisetas=camisetas,
        tote_bags=tote_bags,
        tazas=tazas,
        gorras=gorras
    )

if __name__ == "__main__":
    app.run(debug=True)

