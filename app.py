import streamlit as st
from data_contract import Vendas
from datetime import datetime, time
from pydantic import ValidationError
from database import save_in_postgres

def main():

    st.title("Sistema de CRM")
    email = st.text_input("email do vendedor")
    data = st.date_input("Data da compra", datetime.now())
    hora = st.time_input("Hora da compra", value=time(9, 0))  # Valor padrão: 09:00
    valor = st.number_input("Valor da venda", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade de produtos", min_value=1, step=1)
    setores = st.selectbox("Produto", options=["Varejo", "Atacado"])

    if st.button("Salvar"):
        try:
            data_hora = datetime.combine(data, hora)
            
            venda = Vendas(
                email = email,
                data = data_hora,
                valor = valor,
                quantidade = quantidade,
                setor = setores
            )
            st.write(venda)
            save_in_postgres(venda)
        except ValidationError as e:
            st.error(f"Deu erro {e}")

if __name__=="__main__":
    main()