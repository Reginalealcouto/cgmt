import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Nome do arquivo
DB_FILE = "respostas.csv"

# Carrega ou cria o "banco de dados"
if os.path.exists(DB_FILE):
    df = pd.read_csv(DB_FILE)
else:
    df = pd.DataFrame(columns=["Nome", "Escolha"])

# Formulário
st.title("Formulário de Respostas")

with st.form("form1"):
    nome = st.text_input("Seu nome")
    escolha = st.selectbox("Escolha uma opção", ["Maçã", "Banana", "Uva", "Laranja"])
    submitted = st.form_submit_button("Enviar")

    if submitted and nome:
        novo_dado = pd.DataFrame([[nome, escolha]], columns=["Nome", "Escolha"])
        df = pd.concat([df, novo_dado], ignore_index=True)
        df.to_csv(DB_FILE, index=False)
        st.success("Resposta registrada com sucesso!")

# Gráfico de frequência
st.subheader("Distribuição das escolhas")

if not df.empty:
    contagem = df["Escolha"].value_counts()
    fig, ax = plt.subplots()
    contagem.plot(kind="bar", ax=ax)
    st.pyplot(fig)


