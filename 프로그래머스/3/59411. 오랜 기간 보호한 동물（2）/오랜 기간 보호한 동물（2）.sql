select ani.animal_id, ani.name from animal_outs ani
join animal_ins ins on ani.animal_id = ins.animal_id
order by datediff(ani.datetime, ins.datetime) desc
limit 2