import streamlit as st
from data_contract import Vendas
from datetime import datetime, time
from pydantic import ValidationError

from database import save_in_postgres

def main():
    st.title("CRM para Consultoria")
    email = st.text_input("Insira Seu Email:")
    data = st.date_input("Data da compra", datetime.now())
    hora = st.time_input("Hora da compra", value=time(9, 30))
    valor = st.number_input("Valor da venda", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade vendida", min_value=0, step=1)
    categorias = st.selectbox("Setor do Cliente",options= ["Varejo", "Setor Financeiro", "Saúde"])
    
    if  st.button("Salvar"):
        
        try:
            data_hora = datetime.combine(data, hora)
        
            venda = Vendas(               
                email=email, 
                data=data_hora, 
                valor=valor, 
                quantidade=quantidade, 
                categoria=categorias,
                
            )
            st.success("Venda salva com sucesso!")
            save_in_postgres(venda)
        except ValidationError as e:
            st.error(f"Erro de validação: {e}")
    
if __name__ == "__main__":
    main()