import streamlit as st
import pandas as pd

class ListarAgendaProfissionalUI:
    @staticmethod
    def main():
        st.header(" Agenda do Profissional")
        
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

st.dataframe(pd.DataFrame(dados), use_container_width=True, hide_index=True)