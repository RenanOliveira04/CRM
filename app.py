import streamlit as st
from data_contract import Vendas
from datetime import datetime, time

def main():
    st.title("CRM de Vendas")
    email = st.text_input("Campo de inserção de email do vendedor")
    data = st.date_input("Data da compra", datetime.now())
    hora = st.time_input("Hora da compra", value=time(9, 30))
    valor = st.number_input("Valor da venda")
    quantidade = st.number_input("Quantidade vendida")
    produtos = st.selectbox("Categoria de Produto",options= ["ChabotGPT", "ChatbotGemini", "ChatbotLlhama"])
    
    if  st.button("Salvar"):
        
        data_hora = datetime.combine(data, hora)
    
        venda = Vendas(email=email, data=data_hora, valor=valor, quantidade=quantidade, categoria=produtos)
    
if __name__ == "__main__":
    main()