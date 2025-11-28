import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Qt5Agg")
import seaborn
from src.models.Exoplaneta import Exoplaneta
class Charts():
    def __init__(self):
        pass

    def comparacao_planeta_grafico_barras(self,Planetas:list[Exoplaneta]):
        #plt.ylim(100)
        for p in Planetas:
            plt.bar(p.get_nome_planeta,p.calcular_provabilidade_vida())
        plt.title("Comparação de provabilidade de vida")
        plt.show()
        pass