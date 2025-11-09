import numpy

from src.const.genesis_consts import TerraParametros

class Exoplaneta():
    def __init__(self,
                 nome_planeta,
                 hostname_planeta,
                 estrelas_numero,
                 planetas_numero,
                 ano_descoberta,
                 periodo_orbita_dias,
                 raio_planeta,
                 massa_planeta,
                 insolacao_planeta,
                 temperatura_equilibrio_planeta,
                 gravidade_planeta,
                 distancia_planeta):

        self.nome_planeta = nome_planeta;
        self.hostname_planeta = hostname_planeta;
        self.estrelas_numero = estrelas_numero;
        self.planetas_numero = planetas_numero;
        self.ano_descoberta = ano_descoberta;
        self.periodo_orbitas = periodo_orbita_dias;
        self.raio_planeta = raio_planeta;
        self.massa_planeta = massa_planeta;
        self.insolacao_planeta = insolacao_planeta;
        self.temperatura_equilibrio_planeta = temperatura_equilibrio_planeta;
        self.gravidade_planeta = gravidade_planeta;
        self.distancia_planeta = distancia_planeta;

    @property
    def get_nome_planeta(self):
        return self.nome_planeta;
    @property
    def set_nome_planeta(self,value):
        self.nome_planeta = value;
    @property
    def get_hostname_planeta(self):
        return self.hostname_planeta;
    @property
    def set_hostname_planeta(self, value):
        self.hostname_planeta = value;
    @property
    def get_estrelas_numero(self):
        return self.estrelas_numero;
    @property
    def set_estrelas_numero(self, value):
        self.estrelas_numero = value;
    @property
    def get_planetas_numero(self):
        return self.planetas_numero;
    @property
    def set_planetas_numero(self, value):
        self.planetas_numero = value;
    @property
    def get_ano_descoberta(self):
        return self.ano_descoberta;
    @property
    def set_ano_descoberta(self, value):
        self.ano_descoberta = value;
    @property
    def get_periodo_orbita(self):
        return self.periodo_orbitas;
    @property
    def set_periodo_orbita(self, value):
        self.periodo_orbitas = value;
    @property
    def get_raio_planeta(self):
        return self.raio_planeta;
    @property
    def set_raio_planeta(self, value):
        self.raio_planeta = value;
    @property
    def get_massa_planeta(self):
        return self.massa_planeta;
    @property
    def set_massa_planeta(self, value):
        self.massa_planeta = value;
    @property
    def get_insolacao_planeta(self):
        return self.insolacao_planeta;
    @property
    def set_insolacao_planeta(self, value):
        self.insolacao_planeta = value;
    @property
    def get_temperatura_equilibrio_planeta(self):
        return self.temperatura_equilibrio_planeta;
    @property
    def set_temperatura_equilibrio_planeta(self, value):
        self.temperatura_equilibrio_planeta = value;
    @property
    def get_gravidade_planeta(self):
        return self.gravidade_planeta;
    @property
    def set_temperatura_equilibrio_planeta(self, value):
        self.gravidade_planeta = value;
    @property
    def get_distancia_planeta(self):
        return self.distancia_planeta;
    @property
    def set_distancia_planeta(self, value):
        self.distancia_planeta = value;

    @staticmethod
    def gaussian_on_ratio(x,x_ref,sigma_log):
        if x <= 0 or x_ref <= 0:
            return 0.0
        ln_ratio = numpy.log(x / x_ref)
        return numpy.exp(- (ln_ratio ** 2) / (2*(sigma_log ** 2)))
    @staticmethod
    def gaussian_abs(x,x_ref,sigma):
        return numpy.exp(- ((x - x_ref) ** 2) / (2 * (sigma ** 2)))

    def calcular_provabilidade_vida(self):
        w = {
            "raio": 0.18,
            "massa": 0.18,
            "insolacao": 0.22,
            "temp": 0.20,
            "gravidade": 0.12,
            "periodo": 0.05,
        }
        s_raio = self.gaussian_on_ratio(
            self.raio_planeta,
            TerraParametros.R_ref.value,
            TerraParametros.sigma_r.value
        )
        s_massa = self.gaussian_on_ratio(
            self.massa_planeta,
            TerraParametros.M_ref.value,
            TerraParametros.sigma_m.value
        )
        s_insolacao = self.gaussian_on_ratio(
            self.insolacao_planeta,
            TerraParametros.F_ref.value,
            TerraParametros.sigma_f.value
        )
        s_temp = self.gaussian_abs(
            self.temperatura_equilibrio_planeta,
            TerraParametros.T_ref.value,
            TerraParametros.sigma_t.value
        )
        s_grav = self.gaussian_on_ratio(
            self.gravidade_planeta,
            TerraParametros.g_ref.value,
            TerraParametros.sigma_g.value
        )
        periodo_norm = max(self.periodo_orbitas, 1e-9) / 365.0
        s_periodo = numpy.exp(- ((periodo_norm - 1.0) ** 2) / (2 * (0.7 ** 2)))
        score_raw = (
                w["raio"] * s_raio +
                w["massa"] * s_massa +
                w["insolacao"] * s_insolacao +
                w["temp"] * s_temp +
                w["gravidade"] * s_grav +
                w["periodo"] * s_periodo
        )
        penalidade = 1.0
        if self.estrelas_numero >= 2:
            penalidade *= 0.7
        if self.raio_planeta > 2.0:
            penalidade *= 0.6
        score = score_raw * penalidade
        score = min(max(score, 0.0), 1.0)
        return score

    def categoria_habitabilidade(self):
        p = self.calcular_provabilidade_vida()
        if p >= 0.75:
            return "Semelhante à Terra"
        elif p >= 0.5:
            return "Promissor"
        elif p >= 0.25:
            return "Possível"
        else:
            return "Improvável"
