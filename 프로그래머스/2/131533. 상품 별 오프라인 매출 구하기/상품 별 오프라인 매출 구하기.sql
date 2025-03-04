select p.product_code, p.price * sum(os.sales_amount) as sales
from product p
join offline_sale os on p.product_id = os.product_id
group by p.product_id
order by sales desc, p.product_code