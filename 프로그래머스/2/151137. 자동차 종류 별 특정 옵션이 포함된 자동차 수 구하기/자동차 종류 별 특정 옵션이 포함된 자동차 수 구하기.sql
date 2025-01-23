select car.car_type, count(car_id) as cars from car_rental_company_car car
where car.options like '%통풍시트%' 
or car.options like '%열선시트%'
or car.options like '%가죽시트%'
group by car_type
order by car_type