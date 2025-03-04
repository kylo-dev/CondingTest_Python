select j.flavor
from july j
join first_half fh on j.flavor = fh.flavor
group by j.flavor
order by (sum(j.total_order) + fh.total_order) desc
limit 3