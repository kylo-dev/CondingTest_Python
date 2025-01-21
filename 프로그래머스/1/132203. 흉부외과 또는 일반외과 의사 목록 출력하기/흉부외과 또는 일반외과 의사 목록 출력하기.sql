-- 코드를 입력하세요
SELECT d.dr_name, d.dr_id, d.mcdp_cd, date_format(d.HIRE_YMD, '%Y-%m-%d') as hire_ymd from doctor as d
where d.mcdp_cd = 'cs' or d.mcdp_cd = 'gs'
order by d.HIRE_YMD desc, d.dr_name