-- https://leetcode.com/problems/sales-person/submissions/

WITH salesRepRed as (
    SELECT
        o.sales_id
    FROM orders o
    LEFT JOIN company c
    ON o.com_id  = c.com_id
    WHERE c.name = "RED"

)


SELECT name
FROM SalesPerson
WHERE sales_id not in (SELECT
                        distinct sales_id
                        FROM salesRepRed
                       )