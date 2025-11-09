import pandas as pd
from src.models.Exoplaneta import Exoplaneta
from src.const.genesis_consts import DatasetColumns

class DataHandler:
    COLUMN_MAP = {
        DatasetColumns.pl_name.value: "nome_planeta",
        DatasetColumns.hostname.value: "hostname_planeta",
        DatasetColumns.sy_snum.value: "estrelas_numero",
        DatasetColumns.sy_pnum.value: "planetas_numero",
        DatasetColumns.pl_orbper.value: "periodo_orbitas",
        DatasetColumns.pl_rade.value: "raio_planeta",
        DatasetColumns.discoverymethod.value: "metodo_descoberta",
        DatasetColumns.pl_bmasse.value: "massa_planeta",
        DatasetColumns.pl_insol.value: "insolacao_planeta",
        DatasetColumns.pl_eqt.value: "temperatura_equilibrio_planeta",
        DatasetColumns.sy_dist.value: "distancia_planeta",
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
    
        colunas_necessarias = [col.value for col in DatasetColumns]
        for col in colunas_necessarias:
            if col not in df.columns:
                print(f"Aviso: Coluna esperada '{col}' não encontrada no CSV. Será preenchida com NA.")
                df[col] = pd.NA

        df_filtrados = df[colunas_necessarias].copy()
        df_renomeado = df_filtrados.rename(columns=self.COLUMN_MAP)
        df_limpo = df_renomeado.fillna(0.0)
        self.planetas = []
        for _, row in df.iterrows():
            try:
                planeta = Exoplaneta(**row.to_dict())
                self.planetas.append(planeta)
            except Exception as e:
                print(f"Erro ao processar a linha: {e}")
                      
        print(f"Foram carregados {len(self.planetas)} planetas.")
                
    def get_planets(self):
        return self
                    
