-- https://leetcode.com/problems/fix-names-in-a-table/

--# Write your MySQL query statement below
--# Oracle
--# SELECT user_id, initcap(name) name
--# FROM users
--# ORDER BY user_id;

--# MySQL
SELECT user_id,
    CONCAT(UPPER(SUBSTRING(name,1,1)), LOWER(SUBSTRING(name,2, LENGTH(name) -1 ))) AS name
    FROM users ORDER BY user_id;

-- https://leetcode.com/problems/group-sold-products-by-the-date/
--# Write your MySQL query statement below

SELECT
    sell_date,
    COUNT(DISTINCT product) as num_sold,
    GROUP_CONCAT(DISTINCT product order by product) AS products
FROM Activities
GROUP BY sell_date

-- https://leetcode.com/problems/patients-with-a-condition/submissions/

--# Write your MySQL query statement below
SELECT
    *
FROM Patients
WHERE conditions  LIKE "% DIAB1%" OR
    conditions LIKE "DIAB1%"