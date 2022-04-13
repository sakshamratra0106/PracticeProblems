-- https://leetcode.com/problems/calculate-special-bonus/

SELECT
    employee_id,
    CASE
        WHEN employee_id % 2 != 0 AND name not LIKE "M%" THEN salary
        ELSE 0
    END bonus
FROM Employees

-- https://leetcode.com/problems/swap-salary/

UPDATE Salary SET sex = IF(sex='m','f','m')

-- https://leetcode.com/problems/delete-duplicate-emails/

DELETE p1 FROM Person p1 INNER JOIN Person p2
WHERE p1.email = p2.email AND p1.id > p2.id;