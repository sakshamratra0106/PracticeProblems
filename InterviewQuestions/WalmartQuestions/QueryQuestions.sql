--## EMP
--EMP DEPT SALARY
-- 1. Show in each depart 2nd and 3rd hieghts salaries
WITH rankedSalaryByDept as (
    SELECT
        emp,
        dept,
        salary,
        dense_rank() over(partition dept order by salary desc) rankedBySalary
    FROM EMP
)

SELECT
    dept,
    salary
FROM rankedSalaryByDept
WHERE rankedBySalary in (2, 3)
ORDER BY dept,rankedBySalary

-- 2. Difference between 2nd and 3rd hieghties salary

WITH rankedSalaryByDept as (
    SELECT
        emp,
        dept,
        salary,
        dense_rank() over(partition dept order by salary desc) rankedBySalary,
        LEAD(salary) over(partition dept order by salary desc) next_lowest_Salary
    FROM EMP
)

SELECT
    dept,
    (salary - next_lowest_Salary) as Difference
FROM rankedSalaryByDept
WHERE rankedBySalary in (3)
ORDER BY dept,rankedBySalary



--## Delete from table where we have duplicates and no primary key
--A Common Table Expression, also called as CTE in short form, is a temporary named result set that you can reference within a
--SELECT, INSERT, UPDATE, or DELETE statement. The CTE can also be used in a View.


WITH table_nameCTE AS
(
   SELECT*, ROW_NUMBER() over (PARTITION BY ID ORDER BY ID) as < alias_name >
   FROM table_name
)

DELETE FROM table_nameCTE WHERE alias_name >1
