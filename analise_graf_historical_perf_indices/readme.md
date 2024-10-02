# Explicação em Português

Neste diretório contém a analise exploratória sobre o dataset "Historical Performances of Indices".

Esta base de dados é um dos dataset oferecido pela plataforma Makeover Monday. Esta plataforma oferece desafio semanais de construção de dashboard.

Obs.: no final deste readme está o link para acesso ao dashboard, publicado na plataforma Tableau Public, e neste diretório há uma imagem para acesso rápido.

Com este dataset criei um indicador bem simples. Que com um gráfico de linha apresenta a performance dos indices financeiros através de um período de tempo.

Porém como não consegui encontrar uma opção no Tableau para gerar o gráfico de linha com mais dois eixos. Tive que aplicar um pequeno ajustes na formatação da planilha através da linguagem SQL.

```bash
select
    'EURO STOXX 50' financ_index,
    euro_stoxx_50 value,
    dates dates
from indixes ind
union all
select
    'FTSE 100',
    FTSE_100,
    dates
from indixes
union all
select
    'MSCI CHINA',
    MSCI_CHINA,
    dates
from indixes
union all
select
    'NASDAQ 100',
    NASDAQ_100,
    dates
from indices
union all
select
    'NYSE ARCA GOLD BUGS',
    NYSE_ARCA_GOLD_BUGS,
    dates
from indixes
union all
select
    'SP 500',
    SP_500,
    dates
from indixes;

```

**Antes**

![img relacionamento](https://drive.google.com/uc?id=1yqDUmDZr7-HriX6NNNsS1Ifg8Mri1yBS)


**Depois**

![img relacionamento](https://drive.google.com/uc?id=1mG7I7PCcs2nssEYqBBjQgr5vyfGNs3FA)


---

# Explanation in English

This directory contains the exploratory analysis of the "Historical Performances of Indices" dataset.

This database is one of the datasets offered by the Makeover Monday platform. This platform offers weekly dashboard building challenges.

Note: at the end of this readme is the link to access the dashboard, published on the Tableau Public platform, and in this directory there is an image for quick access.

With this dataset I created a very simple indicator. Which with a line graph presents the performance of financial indexes over a period of time.

However, as I could not find an option in Tableau to generate the line graph with two more axes, I had to apply a small adjustment to the spreadsheet formatting using SQL.

```bash
select
    'EURO STOXX 50' financ_index,
    euro_stoxx_50 value,
    dates dates
from indixes ind
union all
select
    'FTSE 100',
    FTSE_100,
    dates
from indixes
union all
select
    'MSCI CHINA',
    MSCI_CHINA,
    dates
from indixes
union all
select
    'NASDAQ 100',
    NASDAQ_100,
    dates
from indices
union all
select
    'NYSE ARCA GOLD BUGS',
    NYSE_ARCA_GOLD_BUGS,
    dates
from indixes
union all
select
    'SP 500',
    SP_500,
    dates
from indixes;

```

**Before**

![img relacionamento](https://drive.google.com/uc?id=1yqDUmDZr7-HriX6NNNsS1Ifg8Mri1yBS)


**After**

![img relacionamento](https://drive.google.com/uc?id=1mG7I7PCcs2nssEYqBBjQgr5vyfGNs3FA)


---

Check here dashboard: https://public.tableau.com/views/FinancialMarketsHistoricalPerformance_17278040903050/Painel1?:language=pt-BR&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

Check here data source: https://data.world/makeovermonday/financial-markets-historical-performance