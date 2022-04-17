--##users table
--
--columns	type
--id	int
--name	varchar
--created_at	datetime
--
--
--Given a users table, write a query to get the cumulative number of new users added by day, with the total reset every month.
--
--
--
--Example Output:
--
--Date	Monthly Cumulative
--2020-01-01	5
--2020-01-02	12
--...	...
--2020-02-01	8
--2020-02-02	17
--2020-02-03	23



WITH daily_total AS (
    SELECT
        DATE(created_at) AS created_at,
        COUNT(*) AS user_count
    FROM users
    GROUP BY 1
)

SELECT
    created_at,
    SUM(user_count) OVER (PARTITION BY DATE_FORMAT(created_at, '%Y-%m') ORDER BY date ASC) AS monthly_cumulative
FROM daily_total
GROUP BY 1
ORDER BY 1 ASC