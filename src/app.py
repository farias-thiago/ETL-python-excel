import pandas as pd
import numpy as np
import streamlit as st
from validador import Anuncio
from pydantic import ValidationError

def validar_dados(df):
    erros = []
    dados_validados = []

    # Lista de colunas esperadas pelo modelo Anuncio
    expected_columns = [
        "Organizador", "Ano_Mes", "Dia_da_Semana", "Tipo_Dia", "Objetivo", "Date",
        "AdSet_name", "Amount_spent", "Link_clicks", "Impressions", "Conversions",
        "Segmentacao", "Tipo_de_Anuncio", "Fase"
    ]

    # Adicionar colunas ausentes com valor None
    for col in expected_columns:
        if col not in df.columns:
            df[col] = None

    # Converter NaN para None no DataFrame
    df = df.replace([np.nan, "nan", "NaN", "None"], None)

    for index, row in df.iterrows():
        try:
            # Converter a linha em dicionário
            anuncio = row.to_dict()
            # Garantir que strings "None" sejam convertidas em None
            for key, value in anuncio.items():
                if isinstance(value, str) and value.lower() == "none":
                    anuncio[key] = None
            # Validar com o modelo Anuncio
            usuario_validado = Anuncio(**anuncio)
            dados_validados.append(usuario_validado)
        except ValidationError as e:
            erros.append(f"Erro na linha {index + 2}: {str(e)}")
    
    return dados_validados, erros

def main():
    st.title("CSV Data Validator")
    st.write("Upload your CSV file for validation")
    
    # File uploader
    uploaded_file = st.file_uploader("Choose a CSV file", type=['csv'])
    
    if uploaded_file is not None:
        try:
            # Process the file when uploaded
            df = pd.read_csv(uploaded_file)
            st.write("### Validation Results")
            st.dataframe(df.head())

            if st.button("Validate"):
                with st.spinner("Validating data..."):
                    dados_validados, erros = validar_dados(df)

                    if erros:
                        st.error("Errors found in the file:")
                        for erro in erros:
                            st.write(erro)
                    else:
                        st.success("All rows are valid!")
                        st.write(f"Total of {len(dados_validados)} rows validated.")

                        df_validado = pd.DataFrame([d.dict() for d in dados_validados])
                        st.download_button(
                            label="Download Validated Data",
                            data=df_validado.to_csv(index=False),
                            file_name="validated_data.csv",
                            mime="text/csv"
                        )
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")   

if __name__ == "__main__":
    main()