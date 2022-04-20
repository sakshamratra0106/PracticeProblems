# https://leetcode.com/problems/market-analysis-i/

SELECT
    user_id AS buyer_id,
    join_date      ,
    count(orders.buyer_id) AS orders_in_2019
FROM users
left join orders
on users.user_id = orders.buyer_id and EXTRACT(year FROM orders.order_date) = 2019
GROUP BY users.user_id

# https://leetcode.com/problems/top-travellers/

SELECT
    users.name,
    CASE
        when sum(rides.distance) is null then 0
        else sum(rides.distance)
    END as travelled_distance
FROM users
left join rides
on users.id = rides.user_id
group by users.id
order by 2 desc, 1

# https://leetcode.com/problems/capital-gainloss/

with stock_profit_current_transaction as (
    SELECT
        stock_name,
        operation,
        LAG(operation) over(partition by stock_name order by operation_day) as previous_operation,
        price,
        LAG(price) over(partition by stock_name order by operation_day) as previous_price,
        CASE
            when operation = "Sell" then  price - LAG(price) over(partition by stock_name order by operation_day)
            else null
        END as profit_current_transaction
    FROM stocks
)

SELECT
    stock_name,
    sum(profit_current_transaction) as capital_gain_loss
FROM stock_profit_current_transaction
GROUP BY stock_name