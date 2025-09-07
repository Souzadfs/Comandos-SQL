import sqlite3
import pandas as pd

# Conectar ao banco
conn = sqlite3.connect("avioes_treino.sqlite")

# Carregar toda a tabela 'avioes'
df = pd.read_sql_query("SELECT * FROM  avioes;", conn)

# Mostrar no console
print(df)

# Fechar conexão
conn.close()
