import streamlit as st
import pandas as pd
import os

DB_FILE = "dados_formulario.csv"

# Carrega ou cria o banco de dados
if os.path.exists(DB_FILE):
    df = pd.read_csv(DB_FILE)
else:
    df = pd.DataFrame(columns=["Processo", "Procedimento", "ProcedimentoOutro", "TerrasIndigenas"])

# Interface
st.title("Formulário - Procedimentos em Terras Indígenas")

with st.form("formulario_principal"):
    processo = st.text_input("Processo nº")
    
    tipo_procedimento = st.selectbox(
        "Tipo de procedimento",
        ["Inquérito civil", "Notícia de fato", "PAJ coletivo", "Procedimento administrativo", "Outro"]
    )

    outro_procedimento = ""
    if tipo_procedimento == "Outro":
        outro_procedimento = st.text_input("Descreva o tipo de procedimento")

    terras_disponiveis = [
        "Terra Indígena Yanomami",
        "Terra Indígena Raposa Serra do Sol",
        "Terra Indígena Xingu",
        "Terra Indígena Truká",
        "Terra Indígena Guarani",
        "Outra"
    ]
    
    terras_selecionadas = st.multiselect(
        "Selecione a(s) Terra(s) Indígena(s)",
        terras_disponiveis
    )
    
    submitted = st.form_submit_button("Enviar")

    if submitted and processo:
        nova_linha = pd.DataFrame([{
            "Processo": processo,
            "Procedimento": tipo_procedimento,
            "ProcedimentoOutro": outro_procedimento,
            "TerrasIndigenas": "; ".join(terras_selecionadas)
        }])
        
        df = pd.concat([df, nova_linha], ignore_index=True)
        df.to_csv(DB_FILE, index=False)
        st.success("Dados salvos com sucesso!")

# Visualização opcional
if not df.empty:
    st.subheader("Dados salvos")
    st.dataframe(df)

    st.pyplot(fig)


