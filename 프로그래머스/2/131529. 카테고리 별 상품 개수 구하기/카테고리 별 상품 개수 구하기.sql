select left(product_code, 2) as category, count(left(product_code, 2)) as products 
from product
group by left(product_code, 2)
order by left(product_code, 2)