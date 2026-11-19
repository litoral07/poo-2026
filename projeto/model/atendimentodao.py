from dao_sql.dao import DAO
from model.atendimento import Atendimento


class AtendimentoDAO(DAO):
    tabela = "atendimento"
    colunas = (
        "data",
        "queixa_principal",
        "historico_saude",
        "avaliacao",
        "prescricao",
        "id_horario",
    )

    def _objeto_da_linha(self, linha):
        return Atendimento.from_json(linha)