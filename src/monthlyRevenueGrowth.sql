with monthly (year, month, rev) as (
  select leftsubstr(date, 4) as year
  month,
  sum(revenue) as rev
  group by leftsubstr(date, 4), month
  order by year, month
)


