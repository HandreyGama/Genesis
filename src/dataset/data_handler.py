import pandas as pd

from src.models.Exoplaneta import Exoplaneta
from src.const.genesis_consts import DatasetColumns

class DataHandler:
    COLUMN_MAP = {
        DatasetColumns.pl_name.value: "nome_planeta",
        DatasetColumns.hostname.value: "hostname_planeta",
        DatasetColumns.sy_snum.value: "estrelas_numero",
        DatasetColumns.sy_pnum.value: "planetas_numero",
        DatasetColumns.pl_orbper.value: "periodo_orbita_dias",
        DatasetColumns.pl_rade.value: "raio_planeta",
        DatasetColumns.pl_bmasse.value: "massa_planeta",
        DatasetColumns.pl_insol.value: "insolacao_planeta",
        DatasetColumns.pl_eqt.value: "temperatura_equilibrio_planeta",
        DatasetColumns.sy_dist.value: "distancia_planeta",
        DatasetColumns.st_logg.value: "gravidade_planeta",
        DatasetColumns.disc_year.value: "ano_descoberta"
    }

    def __init__(self):
        self.planetas = []

    def load_planets_from_csv(self, csv_path):
        print(f"Carregando dados de {csv_path}")
        try:
            df = pd.read_csv(csv_path, comment="#", low_memory=False)
        except FileNotFoundError:
            print(f"Arquivo não encontrado: {csv_path}")
            return

        colunas_csv = df.columns
        colunas_enum = [col.value for col in DatasetColumns]
        colunas_faltando = []

        print("\nVerificando colunas do Enum no CSV...")
        for col_enum in colunas_enum:
            if col_enum not in colunas_csv:
                colunas_faltando.append(col_enum)

        if colunas_faltando:
            print(f"[AVISO] As seguintes colunas do Enum não foram encontradas no CSV:")
            for col in colunas_faltando:
                print(f"  - {col}")
            print("Elas serão preenchidas com 'NA' (dados ausentes).\n")
        else:
            print("[SUCESSO] Todas as colunas do Enum estão presentes no CSV.\n")
    
        colunas_necessarias = [col.value for col in DatasetColumns]
        for col in colunas_necessarias:
            if col not in df.columns:
                print(f"Aviso: Coluna esperada '{col}' não encontrada no CSV. Será preenchida com NA.")
                df[col] = pd.NA

        df_filtrados = df[colunas_necessarias].copy()
        df_renomeado = df_filtrados.rename(columns=self.COLUMN_MAP)
        df_limpo = df_renomeado.fillna(0.0)
        self.planetas = []
        for _, row in df_limpo.iterrows():
            print(row.to_dict())
            try:
                planeta = Exoplaneta(**row.to_dict())
                self.planetas.append(planeta)
            except Exception as e:
                print(f"Erro ao processar a linha: {e}")
                      
        print(f"Foram carregados {len(self.planetas)} planetas.")
                
    def get_planets(self):
        return self
                    
if __name__ == "__main__":
    print("data handler")
    caminho_csv = "C:\\Users\\andre\PycharmProjects\Genesis\dataset\PS_2025.02.03_05.09.36.csv"
    print(f"Carregando planetas: {caminho_csv}")
    handler_de_teste = DataHandler()
    handler_de_teste.load_planets_from_csv(caminho_csv)
    planetas_carregados = handler_de_teste.get_planets()

    if planetas_carregados:
        print(f"total de planetas carregados:{len(planetas_carregados)}" )
        for planeta in planetas_carregados[:5]:
            print(f"{planeta.get_nome_planeta()}")
    else:
        print("deu ruim")

