
import pandas as pd
from ydata_profiling import ProfileReport
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Gerar relatório para uma Análise Exploratória Inicial
df = pd.read_csv('data.csv')
profile = ProfileReport(df, title='DATA csv Report', explorative=True)
profile.to_file("report.html")


