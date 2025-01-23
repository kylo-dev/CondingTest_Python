select sum(g.score) as score, e.emp_no, e.emp_name, e.position, e.email from hr_employees e
join hr_department d on e.dept_id = d.dept_id
join hr_grade g on e.emp_no = g.emp_no
where g.year = 2022
group by e.emp_no
having score = (
    select max(sub.sub_score) from (
        select sum(gs.score) as sub_score from hr_employees es
        join hr_grade gs on es.emp_no = gs.emp_no
        where gs.year = 2022
        group by es.emp_no
    ) as sub
)
