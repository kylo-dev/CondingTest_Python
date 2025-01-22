-- 코드를 입력하세요
SELECT ice.ingredient_type, sum(fh.total_order) as TOTAL_ORDER
from first_half fh
join icecream_info ice on fh.flavor = ice.flavor
group by ice.ingredient_type
order by total_order