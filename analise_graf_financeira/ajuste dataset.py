
import pandas as pd

# Carregar o arquivo Excel
df = pd.read_excel('DadosFinanceiros.xlsx')

# Identificar as colunas de data (todas as colunas a partir da terceira coluna)
date_columns = df.columns[2:]

# Substituir vírgulas por pontos e converter os valores das colunas de data para numérico
df[date_columns] = df[date_columns].replace({',': '.'}, regex=True).apply(pd.to_numeric)

# Transformar o DataFrame para ter as colunas 'Data' e 'Valores'
df_melted = df.melt(id_vars=['Tipo', 'Componente'], var_name='Data', value_name='Valores')

# Exibir o DataFrame ajustado
df_melted.head()

# Exportar o DataFrame ajustado para um arquivo Excel
df_melted.to_excel('DadosFinanceiros_ajustado2.xlsx', index=False)
