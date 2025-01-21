-- 코드를 입력하세요
SELECT an.animal_id, an.name from animal_ins as an
where an.intake_condition = 'sick'
order by an.animal_id