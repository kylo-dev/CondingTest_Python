with value as (
    select car.daily_fee, car.car_type, his.history_id,
        (datediff(end_date, start_date) + 1) as period,
        case
            when (datediff(end_date, start_date) + 1) >= 90 then '90일 이상'
            when (datediff(end_date, start_date) + 1) >= 30 then '30일 이상'
            when (datediff(end_date, start_date) + 1) >= 7 then '7일 이상'
            else null
        END as duration_type
    from car_rental_company_rental_history his
    join car_rental_company_car car on car.car_id = his.car_id
    where car.car_type = '트럭'
)

# select * from value

select value.history_id, 
    round(value.daily_fee * value.period * ((100 - IFNULL(plan.discount_rate, 0)) / 100)) as fee
from value
left join car_rental_company_discount_plan as plan
    on plan.duration_type = value.duration_type
    and plan.car_type = value.car_type
order by fee desc, value.history_id desc

