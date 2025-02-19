select * from car_rental_company_car car
where car.options like '%네비게이션%'
order by car.car_id desc