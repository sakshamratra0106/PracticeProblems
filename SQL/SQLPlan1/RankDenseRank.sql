--https://leetcode.com/problems/find-total-time-spent-by-each-employee/submissions/

SELECT
    event_day   AS day,
    emp_id,
    SUM(out_time - in_time) AS  total_time
FROM Employees
GROUP BY event_Day, emp_id

-- https://leetcode.com/problems/the-latest-login-in-2020/submissions/

SELECT
    user_id         ,
    time_stamp  as last_stamp
FROM (
    SELECT
        *,
        EXTRACT(year FROM time_stamp) loginYear,
        dense_rank() OVER(PARTITION BY user_id ORDER BY time_stamp desc) as rankedLogin
    FROM Logins
    WHERE EXTRACT(year FROM time_stamp) = 2020 ) rankedLogins
WHERE rankedLogin = 1

-- https://leetcode.com/problems/game-play-analysis-i/submissions/

SELECT
    player_id ,
    event_date  as first_login
FROM (
    SELECT
        *,
        dense_rank() OVER(PARTITION BY player_id ORDER BY event_date) as rankedLogin
    FROM Activity) rankedActivity
WHERE rankedLogin = 1

-- https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/

WITH rankedCustomers AS (
    SELECT
        *,
        dense_rank() over(order by number_of_orders desc) rankedCustomer
    FROM (
        SELECT
            customer_number,
            count(*) number_of_orders
        FROM orders
        GROUP BY customer_number ) innerTable
)

SELECT
    customer_number
FROM rankedCustomers
WHERE rankedCustomer = 1