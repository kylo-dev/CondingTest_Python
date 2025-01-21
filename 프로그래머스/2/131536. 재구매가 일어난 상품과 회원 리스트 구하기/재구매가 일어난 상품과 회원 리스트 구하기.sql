SELECT os.user_id, os.product_id 
from (select oss.user_id, oss.product_id
     from online_sale as oss
     group by oss.user_id, oss.product_id
     having count(oss.user_id) > 1 and count(oss.product_id) > 1
     ) as os
order by os.user_id, os.product_id desc