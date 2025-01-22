-- 코드를 작성해주세요

select count(f.id) as fish_count, month(f.time) as month from fish_info f
group by month(f.time)
order by month