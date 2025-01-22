-- 코드를 작성해주세요

select count(*) as fish_count, max(ifnull(f.length, 10)) as max_length, fish_type
from fish_info f
group by f.fish_type
having avg(ifnull(f.length, 10)) >= 33
order by f.fish_type