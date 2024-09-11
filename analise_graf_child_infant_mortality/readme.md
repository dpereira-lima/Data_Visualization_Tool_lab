# Explicação em Português

Neste diretório contém a analise exploratória sobre o dataset "Child and Infant Mortality".

Esta base de dados é um dos dataset oferecido pela plataforma Makeover Monday. Esta plataforma oferece desafio semanais de construção de dashboard.

Obs.: no final deste readme está o link para acesso ao dashboard, publicado na plataforma Tableau Public, e neste diretório há uma imagem para acesso rápido.

Antes de realizar analise dos dados, acrescentei o continente de cada país na base. E para agregar esta informação criei um dataset contendo os nomes dos países e o respectivo continente e utilizei o seguinte trecho de código Python para juntar os dois dataset.

```bash
# importação da biblioteca Pandas

import pandas as pd

# leitura dos datasets

df_country = pd.read_csv('child-mortality.csv')

df_continent = pd.read_csv('continents.csv', sep=';')

# alterando o nome das colunas no dataset Continente

df_continent.rename(columns={'País': 'Entity'}, inplace = True)
df_continent.rename(columns={'Continente': 'Continent'}, inplace = True)


# realizando o merge (join) entre os datasets

df_new = pd.merge(df_country, df_continent, on="Entity")

# convertendo o novo dataset para arquivo .CSV

df_new.to_csv('child-mortality-2.csv', index=False)

# Run Briefer and access it on http://localhost:3000
briefer
```

E após a criação do novo dataset, criei as visualizações e o dashboard no Tableau.

---

# English Explanation

In this directory it contains the exploratory analysis about the "Child and Infant Mortality" dataset.

This database is one of the dataset offered by the Makeover Monday platform. This platform offers weekly challenges of dashboard building.

Obs.: at the end of this readme is the link for access to the dashboard, posted on the Tableau Public platform, and in this directory there is an image for quick access.

Before conducting data analysis, I added each country's mainland on the base. And to aggregate this information I created a dataset containing the names of the countries and the respective continent and used the following Python code stretch to join the two dataset.

```bash
# Pandas Library Import

import pandas as pd

# reading of datasets

df_country = pd.read_csv('child-mortality.csv')

df_continent = pd.read_csv('continents.csv', sep=';')

# by changing the column name in the Continent dataset

df_continent.rename(columns={'Country': 'Entity'}, inplace = True)
df_continent.rename(columns={'Mainland': 'Continent'}, inplace = True)


# performing the merge (join) between the datasets

df_new = pd.merge(df_country, df_continent, on="Entity")

# converting the new dataset to .CSV file

df_new.to_csv('child-mortality-2.csv', index=False)

# Run Briefer and access it on http://localhost:3000
brief
```

And after the creation of the new dataset, I created the views and the dashboard on Tableau.


---

Check here dashboard: 

Check here data source: https://data.world/makeovermonday/child-and-infant-mortality/workspace/file?filename=child-mortality.csv
