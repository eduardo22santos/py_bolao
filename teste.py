import pandas as pd
import sqlite3

banco = sqlite3.connect('bancoDeDados.db')
tabela = pd.read_sql_query("SELECT * from bolao",banco)
print(tabela.head())