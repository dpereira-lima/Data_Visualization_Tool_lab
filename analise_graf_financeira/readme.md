# Explicação em Português

Neste diretório contém uma analise gráfica, em Tableau, sobre dados financeiros de uma empresa

Há também uma imagem de acesso rápido ao dashboard. Mas no final deste readme há o endereço de acesso no portal Tableau Public.

Antes de criar o dasboard foi necessário ajustar a formatação dos dados no dataset. E para isto utilizei o seguinte código Python:

```bash

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

```

Após este ajuste pude construir o dashboard, no Tableau, utilizando alguns KPIs financeiros:

- Total de despesas e receitas;
- Margem de lucro;
- Acompanhamento das despesas e receitas no período;
- Despesas e receitas por componente;
- E realitório sumarizado em tabela.


---

# Explanation in English

This directory contains a graphical analysis, in Tableau, of a company's financial data

There is also an image for quick access to the dashboard. But at the end of this readme there is the access address on the Tableau Public portal.

Before creating the dashboard, it was necessary to adjust the formatting of the data in the dataset. And for this I used the following Python code:

```bash

import pandas as pd

# Upload the Excel file
df = pd.read_excel('DadosFinanceiros.xlsx')

# Identify date columns (all columns starting from the third column)
date_columns = df.columns[2:]

# Replace commas with periods and convert date column values ​​to numeric
df[date_columns] = df[date_columns].replace({',': '.'}, regex=True).apply(pd.to_numeric)

# Transform the DataFrame to have the columns 'Date' and 'Values'
df_melted = df.melt(id_vars=['Tipo', 'Componente'], var_name='Data', value_name='Valores')

# Display the adjusted DataFrame
df_melted.head()

# Export the adjusted DataFrame to an Excel file
df_melted.to_excel('DadosFinanceiros_ajustado2.xlsx', index=False)

```

After this adjustment I was able to build the dashboard, in Tableau, using some financial KPIs:

- Total expenses and revenues;
- Profit margin;
- Monitoring of expenses and revenues in the period;
- Expenses and revenues by component;
- And a summary report in a table.



---

Check here dashboard: https://public.tableau.com/views/Analisegraficafinanceira/Painel1?:language=pt-BR&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

