select year(os.sales_date) as year, month(os.sales_date) as month,
count(distinct(u.user_id)) as purchased_users,
round(count(distinct(u.user_id)) / (
    select count(*) from user_info ui
    where year(ui.joined) = '2021'), 1) as puchased_ratio
from user_info u
join online_sale os on os.user_id = u.user_id
where year(u.joined) = '2021'
group by date_format(os.sales_date, '%Y-%m')
order by year, month