import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Conectar ao banco
conn = sqlite3.connect("treino.sqlite")

# Consulta SQL (entre aspas)
query = """
SELECT f.nome, SUM(p.valor) AS total_vendas
FROM funcionarios f
JOIN pedidos p ON f.id = p.funcionario_id
GROUP BY f.nome
ORDER BY total_vendas DESC;
"""

# Executar consulta e carregar no DataFrame
df = pd.read_sql_query(query, conn)

# Mostrar resultado no console
print(df)

# Gráfico de barras
df.plot(x="nome", y="total_vendas", kind="bar", legend=False)
plt.title("Vendas por Funcionário")
plt.xlabel("Funcionário")
plt.ylabel("Total de Vendas")
plt.tight_layout()
plt.show()

# Fechar conexão
conn.close()
