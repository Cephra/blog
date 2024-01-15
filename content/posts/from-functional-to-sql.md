+++
title = "From Functional to SQL"
date = 2024-06-27 00:54:49+02:00
summary = "This post demonstrates how to calculate the normalized value of a meter type over time using SQL, highlighting its advantages in performing calculations directly on large datasets."
+++

In my previous post, I discussed a functional approach to solving the problem of calculating the normalized value of a meter type over time. However, not all data processing tasks can be solved using programming languages alone. In this post, I'll show you how to achieve the same result using SQL.

```sql
create or replace view v_value_stats as
with value_with_first_meter_date as (
    select
        v.id as "value_id",
        v.timestamp,
        v.value,
        m.id as "meter_id",
        mt.id as "meter_type_id",
        first_value(v.timestamp)
            over (partition by v.meter_id order by v."timestamp")
        as meter_first_date
    from t_value as v
    inner join t_meter as m on v.meter_id = m.id
    inner join t_meter_type as mt on m.meter_type_id = mt.id
    order by v.timestamp
),

adjusted_values as (
    select
        v.*,
        v.value - lag(v.value, 1, v.value)
            over (
                partition by v.meter_id
                order by v."timestamp", v.meter_first_date
            )
        as meter_adjusted_value
    from value_with_first_meter_date as v
    order by v.timestamp asc, v.meter_first_date asc
),

normalized_value as (
    select
        v.value_id as "id",
        v.timestamp,
        v.meter_id,
        v.meter_type_id,
        sum(v.meter_adjusted_value)
            over (
                partition by v.meter_type_id
                order by v.timestamp, v.meter_first_date
                rows between unbounded preceding and current row
            )
        as "value"
    from adjusted_values as v
    order by v.timestamp, v.meter_first_date
),

normalized_value_delta as (
    select
        nv.*,
        extract(
            day from nv.timestamp - lag(
                nv.timestamp, 1, nv.timestamp
            )
                over (
                    partition by nv.meter_type_id
                    order by nv.timestamp asc
                )
        )::double precision
        as "date_diff",
        nv.value
        - lag(nv.value, 1)
            over (partition by nv.meter_type_id order by nv.timestamp)
        as "delta"
    from normalized_value as nv
),

delta_year as (
    select
        nvd.*,
        case
            when nvd.date_diff = 0
                then 0
            else ((nvd.delta / nvd.date_diff) * 365)
        end as "delta_year"
    from normalized_value_delta as nvd
)

select
    dy.*,
    avg(dy.delta_year) over (
        partition by dy.meter_type_id
        order by dy.timestamp
        rows between 3 preceding and current row
    ) as delta_last4_avg,
    avg(dy.delta_year) over (
        partition by dy.meter_type_id
        order by dy.timestamp
        rows between 51 preceding and current row
    ) as delta_year_avg
from delta_year as dy
```

Calculating things like the normalized or average value of a meter type over time can be a complex task, especially when dealing with large datasets. One advantage of using SQL for this task is that it allows you to perform calculations directly on the data, without having to transfer it to another system or language. This can greatly improve performance and reduce the risk of errors.

On the other hand, SQL may not be as flexible as programming languages like Python or JavaScript, which can make it more difficult to implement certain types of logic. Additionally, SQL queries can become complex and difficult to read if they are not well-organized and documented.

Despite these limitations, SQL is a powerful tool for performing data analysis and calculations. With the right skills and knowledge, you can use it to solve a wide range of problems, including calculating the average value of a meter over time.

And let me tell you, constructing that SQL was a real "m!ndf**k". :sweat: :smile:
