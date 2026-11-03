from datetime import datetime
import pandas as pd
streemlit as st
from service import Service
class ListarHorariosConfirmadosHojeUI:
    @staticmethod
    def main():
        st.header("horarios cofimados")
        horarios=Service.horario_listar_confimados_hoje()
        if not horarios:
            st.info("sem horarios")
            return
        dados = []
        for h in horarios:
             cliente = Service.cliente_listar_id(get_id_cliente())
             servico = Service.servico_listar_id(get_id_servico())
             profissional = Service.profissional_listar_id(get_id_profissional()) 
        dados.append = [{
            "ID": h.get_id(),
            "Data / Hora": h.get_data().strftime("%d/%m/%Y %H:%M"),
            "Cliente": h.get_cliente_nome(),
            "Descrição do Serviço": h.get_servico_descricao()
        } for h in agenda_ordenada]
st.datafreme(pd.DataFrame(dados), hide_index=True)      

