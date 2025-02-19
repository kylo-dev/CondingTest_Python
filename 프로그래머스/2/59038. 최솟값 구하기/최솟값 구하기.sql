select an.datetime as '시간' from animal_ins an
where an.datetime = (
    select min(ani.datetime) from animal_ins ani
)