select distinct d.id, d.email, d.first_name, d.last_name
from developers d
    join skillcodes s on d.skill_code = s.code | d.skill_code
where s.category like '%Front End%'
order by d.id