import os
from flask import Flask, render_template, send_from_directory
from src.dataset.data_handler import DataHandler

basedir = os.path.abspath(os.path.dirname(__file__))
CAMINHO_TEMPLATES = os.path.join(basedir,'src','frontend','templates')
CAMINHO_STATIC = os.path.join(basedir,'src','frontend','static')
CSV_PATH = os.path.join(basedir,'dataset','PS_2025.02.03_05.09.36.csv')

app = Flask(__name__,
            template_folder=CAMINHO_TEMPLATES,
            static_folder=CAMINHO_STATIC)

data_handler = DataHandler()
data_handler.load_planets_from_csv(CSV_PATH)


@app.route("/")
def homepage():
    return render_template("homepage.html")

dashboard = {}
@app.route("/planetas")
def planetas():
    todos_planetas = data_handler.get_planets()
    todos_planetas.sort(key=lambda x: x.calcular_provabilidade_vida(), reverse=True)
    dashboard = {
        "Semelhante à Terra": [],
        "Promissor": [],
        "Possível": [],
        "Improvavel": []
    }

    for planeta in todos_planetas:
        categoria = planeta.categoria_habitabilidade()
        if categoria in dashboard and len(dashboard[categoria]) < 4:
            dashboard[categoria].append(planeta)
    return render_template("planetas.html", dashboard=dashboard)

@app.route("/teste")
def teste():
    todos_planetas = data_handler.get_planets()
    todos_planetas.sort(key=lambda x: x.calcular_provabilidade_vida(), reverse=True)
    dashboard = {
        "Semelhante à Terra": [],
        "Promissor": [],
        "Possível": [],
        "Improvavel": [],
        "Hostil": [],
        "Incerto": []
    }

    for planeta in todos_planetas:
        categoria = planeta.categoria_habitabilidade()
        if categoria in dashboard and len(dashboard[categoria]) < 4:
            dashboard[categoria].append(planeta)
    return render_template("index.html", dashboard=dashboard)
# IMPOSSIVEL RESPIRAR PELA BOCA COM A LINGUA PRA FORA2


DOWNLOAD_DIRECTORY = os.path.abspath('dataset')
@app.route('/planetas/download/<filename>')
def download_dataset(filename):

    try:
        return send_from_directory(
            DOWNLOAD_DIRECTORY,
            filename,
            as_attachment=True
        )
    except FileNotFoundError:

        return "Arquivo não encontrado", 404

@app.route('/planetas/aboutmore/<nome_planeta>')
def aboutmore(nome_planeta):

    return render_template("about-planet.html")

if __name__ == "__main__":
    app.run(debug=True)