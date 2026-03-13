import os
import flask
from src.dataset.data_handler import DataHandler
from src.backend.AiIntegration import Ai

# Raiz do projeto (onde app.py está)
basedir = os.path.abspath(os.path.dirname(__file__))

# Caminhos absolutos corretos
CAMINHO_TEMPLATES = os.path.join(basedir, 'src', 'frontend', 'templates')
CAMINHO_STATIC    = os.path.join(basedir, 'src', 'frontend', 'static')
CSV_PATH          = os.path.join(basedir, 'dataset', 'PS_2025.02.03_05.09.36.csv')

app = flask.Flask(__name__,
            template_folder=CAMINHO_TEMPLATES,
            static_folder=CAMINHO_STATIC)

if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 5000)))

data_handler = DataHandler()
try:
    data_handler.load_planets_from_csv(CSV_PATH)
except Exception as e:
    print(f"Erro ao carregar CSV: {e}")

@app.route("/debug")
def debug():
    import os
    info = {
        "basedir": basedir,
        "template_folder": app.template_folder,
        "template_folder_exists": os.path.exists(app.template_folder),
        "files_in_template_folder": os.listdir(app.template_folder) if os.path.exists(app.template_folder) else "PASTA NÃO EXISTE",
        "cwd": os.getcwd(),
        "listdir_root": os.listdir("/var/task")
    }
    return flask.jsonify(info)

@app.route("/")
def homepage():
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
        if categoria in dashboard:
            # Da pra aumentar o limite se quiser mostrar mais de um card por categoria, talvez seja bom fazer isso depois
            if len(dashboard[categoria]) < 4:
                dashboard[categoria].append(planeta)
        
    return flask.render_template("homepage.html", dashboard=dashboard)


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
    return flask.render_template("planetas.html", dashboard=dashboard)


@app.route("/teste")
def teste():
    return flask.render_template("index.html")


DOWNLOAD_DIRECTORY = os.path.join(basedir, 'dataset')


@app.route('/planetas/download/<filename>')
def download_dataset(filename):
    try:
        return flask.send_from_directory(
            DOWNLOAD_DIRECTORY,
            filename,
            as_attachment=True
        )
    except FileNotFoundError:

        return "Arquivo não encontrado", 404


# app.py

@app.route('/planetas/aboutmore/<nome_planeta>')
def aboutmore(nome_planeta):
    ia = Ai()
    # Note que a IA original está sendo renderizada aqui.
    resposta_ia = ia.PerguntarChat(nome_planeta)

    planeta_changed = data_handler.get_planet_por_nome(nome_planeta)

    # IMPORTANTE: Você precisa USAR SESSÕES para manter o histórico de chat
    # Se você não usar 'session' (importar 'session' do flask), o chat será limpo a cada refresh.
    # Por enquanto, o chat só funciona no frontend com o AJAX, mas se você quiser
    # que o histórico persista após um refresh, a lógica abaixo é necessária:
    # from flask import Flask, session, ...
    # app.config['SECRET_KEY'] = 'uma-chave-secreta' # Chave é necessária para sessões

    # Por enquanto, o código abaixo deve continuar enviando um chat vazio:
    chat_messages = []

    return flask.render_template("about-planet.html", planeta_changed=planeta_changed, resposta_ia=resposta_ia, ia=ia,
                           nome_planeta=nome_planeta, chat_messages=chat_messages)


# =========================================================================
# 💡 NOVA ROTA DE API PARA O CHAT (Retorna JSON)
# =========================================================================
@app.route('/api/chat/<nome_planeta>', methods=['POST'])
def chat_with_ia(nome_planeta):
    # 1. Obter a pergunta do corpo da requisição JSON
    data = flask.request.get_json()
    pergunta_usuario = data.get('pergunta', '').strip()

    if not pergunta_usuario:
        # Se a requisição veio vazia, retorna um erro
        return flask.jsonify({"error": "Nenhuma pergunta fornecida."}), 400

    # 2. Obter o planeta para fornecer contexto à IA
    planeta_changed = data_handler.get_planet_por_nome(nome_planeta)
    if not planeta_changed:
        return flask.jsonify({"error": "Planeta não encontrado."}), 404

    # 3. Chamar a função da IA (Assumindo que Ai.PerguntarSobrePlaneta está disponível)
    try:
        ia = Ai()  # Instanciar a classe de IA

        # Chamada real à IA
        resposta_ia = ia.PerguntarSobrePlaneta(planeta_changed.nome_planeta, pergunta_usuario)

        # 4. Retorna a resposta da IA em formato JSON
        return flask.jsonify({"resposta": resposta_ia})
    except Exception as e:
        # Tratar falhas da IA
        print(f"Erro ao processar a pergunta da IA: {e}")
        return flask.jsonify({"error": "Erro interno ao processar a requisição da IA."}), 500


# =========================================================================


@app.route("/comparar")
def comparar():
    planetas_str = flask.request.args.get('planetas')

    planetas_selecionados = []
    if planetas_str:
        nomes_planetas = planetas_str.split(',')
        for nome in nomes_planetas:
            planeta = data_handler.get_planet_por_nome(nome.strip())
            if planeta:
                planetas_selecionados.append(planeta)

    return flask.render_template("comparar.html", planetas=planetas_selecionados)


@app.route("/espaco")
def espaco():
    todos_planetas = data_handler.get_planets()
    return flask.render_template("lista-exoplanetas.html", lista_planetas=todos_planetas)

