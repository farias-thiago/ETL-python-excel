#Usar o pydantic para validar dados de entrada
#Contrato de Dados
from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class Anuncio(BaseModel):
    Organizador: int = Field(
        description="Identificador único do organizador do anúncio."
    )
    Ano_Mes: str = Field(
        description="Ano e mês referente ao período do anúncio.",
        pattern=r"^\d{4} \| (Janeiro|Fevereiro|Março|Abril|Maio|Junho|Julho|Agosto|Setembro|Outubro|Novembro|Dezembro)$"
    )
    Dia_da_Semana: str = Field(
        description="Dia da semana em que o anúncio foi veiculado.",
        enum=["Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado", "Domingo"]
    )
    Tipo_Dia: str = Field(
        description="Tipo de dia (útil, fim de semana, feriado, etc.).",
        enum=["Dia útil", "Final de Semana"]
    )
    Objetivo: str = Field(
        description="Objetivo do anúncio (ex: Leads, Vendas, Branding).",
        enum=["Leads", "Awareness"]
    )
    Date: date = Field(
        description="Data em que o anúncio foi veiculado.",
        ge=date(2024, 1, 1),
        le=date(2099, 12, 31)
    )
    AdSet_name: str = Field(
        description="Nome do conjunto de anúncios (AdSet).",
        min_length=1,
        max_length=200
    )
    Amount_spent: float = Field(
        description="Valor gasto no anúncio.",
        ge=0.0,
        le=1200.00
    )
    Link_clicks: Optional[int] = Field(
        default=None,
        description="Número de cliques no link do anúncio.",
        ge=0,
        nulable=True
    )
    Impressions: Optional[int] = Field(
        default=None,
        description="Número de impressões do anúncio.",
        ge=0,
        nulable=True
    )
    Conversions: Optional[int] = Field(
        default=None,
        description="Número de conversões geradas pelo anúncio.",
        ge=0,
        nulable=True
    )
    Segmentacao: Optional[str] = Field(
        default=None,
        description="Segmentação do público-alvo do anúncio.",
        enum=["Full", "Rmkt_All_90dias", "Interesses em Ferramentas e Tecnologias de Dados", 
              "LookALike_Compradores_1", "Interesses_Dados"],
        nulable=True
    )
    Tipo_de_Anuncio: Optional[str] = Field(
        default=None,
        description="Tipo de anúncio (ex: Estático, Vídeo, Carrossel).",
        enum=["Video", "Estático"],
        nulable=True
    )
    Fase: str = Field(
        description="Fase da campanha em que o anúncio foi veiculado.",
        min_length=1,
        max_length=100 
    )