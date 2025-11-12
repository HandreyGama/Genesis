import os
from flask import Flask, render_template
from flask import Flask
from src.dataset.data_handler import DataHandler

basedir = os.path.abspath(os.path.dirname(__file__))

CAMINHO_TEMPLATES = os.path.join(basedir,'src','frontend','templates')
CAMINHO_STATIC = os.path.join(basedir,'src','frontend','static')

app = Flask(__name__,
            template_folder=CAMINHO_TEMPLATES,
            static_folder=CAMINHO_STATIC)

CSV_PATH = os.path.join(basedir,'data.csv','PS_2025.02.03_05.09.36.csv')

data_handler = DataHandler()
data_handler.load_planets_from_csv(CSV_PATH)
@app.route("/")
def home():
    lista_planets = data_handler.get_planets()
    lista_planets.sort(key=lambda x: x.calcular_probabilidade_vida(), reverse=True)
    return render_template("index.html", planets=lista_planets)


if __name__ == "__main__":
    app.run(debug=True)