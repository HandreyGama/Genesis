# Documentação oficial do app Genesis

## Estrutura atual do projeto:
```
.
├── app.py
├── dataset
│   └── PS_2025.02.03_05.09.36.csv
├── docs
│   └── DOCS.md
├── Genesis
├── LICENSE
├── README.md
├── requirements.txt
├── setup.py
└── src
    ├── backend
    │   ├── AiIntegration.py
    │   ├── Charts.py
    │   ├── __init__.py
    │   └── __pycache__
    ├── const
    │   ├── genesis_consts.py
    │   ├── __init__.py
    │   └── __pycache__
    ├── dataset
    │   ├── data_handler.py
    │   ├── __init__.py
    │   └── __pycache__
    ├── frontend
    │   ├── __init__.py
    │   ├── static
    │   │   ├── css
    │   │   │   ├── about-planet.css
    │   │   │   ├── comparar.css
    │   │   │   ├── globals.css
    │   │   │   ├── homepage.css
    │   │   │   ├── lista-exoplanetas.css
    │   │   │   ├── planetas.css
    │   │   │   └── style.css
    │   │   ├── img
    │   │   │   ├── background.png
    │   │   │   ├── Compare.png
    │   │   │   ├── download.png
    │   │   │   ├── GitHub.png
    │   │   │   ├── Info.png
    │   │   │   ├── left.png
    │   │   │   ├── Moon.png
    │   │   │   ├── planetaTerra.gif
    │   │   │   ├── planetaTerra.png
    │   │   │   ├── planets
    │   │   │   │   ├── Kepler-1410 b.png
    │   │   │   │   ├── Kepler-395 c.png
    │   │   │   │   ├── Kepler-452 b.png
    │   │   │   │   ├── LP 791-18 d.png
    │   │   │   │   ├── LP 890-9 c.png
    │   │   │   │   ├── Teegarden's Star b.png
    │   │   │   │   ├── TOI-700 d.png
    │   │   │   │   ├── TRAPPIST-1 d.png
    │   │   │   │   ├── TRAPPIST-1 e.png
    │   │   │   │   ├── TRAPPIST-1 f.png
    │   │   │   │   └── TRAPPIST-1 g.png
    │   │   │   ├── planets_no_shadow
    │   │   │   │   └── img.png
    │   │   │   ├── rigth.png
    │   │   │   ├── Sun.png
    │   │   │   └── world.svg
    │   │   └── js
    │   │       ├── btn_theme.js
    │   │       ├── carrossel.js
    │   │       ├── comparar.js
    │   │       ├── downloadButtom.js
    │   │       └── painelComparar.js
    │   └── templates
    │       ├── about-planet.html
    │       ├── comparar.html
    │       ├── homepage.html
    │       ├── index.html
    │       ├── lista-exoplanetas.html
    │       └── planetas.html
    └── models
        ├── Exoplaneta.py
        ├── __init__.py
        └── __pycache__

21 directories, 59 files
```

## Classes:
* Exoplaneta: classe de dados que possibilita calcular a provabilidade de vida baseado em distribuição normal e função gaussiana
* 
