
select year(os.sales_date) as year, month(os.sales_date) as month, 
    ui.gender, count(distinct ui.user_id) as users 
from online_sale os
join user_info ui on ui.user_id = os.user_id
where ui.gender is not null
group by year(os.sales_date), month(os.sales_date), ui.gender
order by year, month, gender