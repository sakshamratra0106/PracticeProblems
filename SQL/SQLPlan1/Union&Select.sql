-- https://leetcode.com/problems/second-highest-salary/submissions/

-- Write your MySQL query statement below

WITH RankedSalary as (
    SELECT
        id,
        salary,
        rank() over(order by salary desc) rankedSalary
    FROM Employee
)


SELECT
    X.*
FROM (SELECT
        SALARY as SecondHighestSalary
    FROM RankedSalary
    WHERE rankedSalary = 2

    UNION

    SELECT
        NULL as SecondHighestSalary
    FROM RankedSalary) X
LIMIT 1


--https://leetcode.com/problems/tree-node/submissions/

SELECT
    DISTINCT
    a.id,
    CASE
        WHEN a.p_id IS NULL THEN "Root"
        WHEN b.p_id IS NULL THEN "Leaf"
        ELSE "Inner"
    END AS type

FROM Tree a
    LEFT JOIN Tree b
    ON a.id = b.p_id

-- https://leetcode.com/problems/employees-with-missing-information/submissions/

SELECT T.employee_id
FROM
  (SELECT * FROM Employees LEFT JOIN Salaries USING(employee_id)
   UNION
   SELECT * FROM Employees RIGHT JOIN Salaries USING(employee_id))
AS T
WHERE T.salary IS NULL OR T.name IS NULL
ORDER BY employee_id;

-- https://leetcode.com/problems/rearrange-products-table/submissions/

SELECT
    product_id,
    "store1" as store,
    store1  as price
FROM Products
WHERE store1 is not null

union

SELECT
    product_id,
    "store2" as store,
    store2  as price
FROM Products
WHERE store2 is not null

union

SELECT
    product_id,
    "store3" as store,
    store3  as price
FROM Products
WHERE store3 is not null