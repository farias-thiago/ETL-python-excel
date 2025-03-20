# Validação e Análise de Dados 

Este projeto é uma ferramenta de análise e validação de dados de anúncios, desenvolvida para ajudar na gestão e análise de campanhas de marketing. Ele inclui funcionalidades para validação de dados, geração de relatórios exploratórios e visualização de KPIs.

## Funcionalidades

1. **Validação de Dados**: Utiliza o `pydantic` para validar os dados de entrada conforme um contrato de dados definido.
2. **Análise Exploratória**: Gera um relatório exploratório inicial usando `ydata_profiling`.
3. **Dashboard Interativo**: Um dashboard desenvolvido com `Streamlit` que permite a visualização de KPIs e análise interativa dos dados.

## Estrutura do Projeto

- **main.py**: Script principal para gerar o relatório exploratório.
- **validador.py**: Contém o modelo `Anuncio` para validação dos dados de entrada.
- **app.py**: Aplicação Streamlit para validação de arquivos CSV.
- **dashboard.py**: Dashboard interativo para análise de KPIs de anúncios.