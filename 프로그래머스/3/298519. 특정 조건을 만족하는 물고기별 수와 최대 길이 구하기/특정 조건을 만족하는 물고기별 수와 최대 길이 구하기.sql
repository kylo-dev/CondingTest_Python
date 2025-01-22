-- 코드를 작성해주세요

select count(*) as fish_count, max(length) as max_length, fish_type
from fish_info f
group by f.fish_type
having avg(case 
           when f.length <= 10 then 10 
           else f.length 
         end) >= 33
order by f.fish_type