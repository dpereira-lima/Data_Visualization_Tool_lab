select
    'EURO STOXX 50' financ_index,
    euro_stoxx_50 value,
    dates dates
from indices ind
union all
select
    'FTSE 100',
    FTSE_100,
    dates
from indices
union all
select
    'MSCI CHINA',
    MSCI_CHINA,
    dates
from indices
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
from indices
union all
select
    'SP 500',
    SP_500,
    dates
from indices