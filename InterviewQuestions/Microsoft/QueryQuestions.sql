--##### SQL Given Sample Data and Schema
--
--
--id | name  | salary | departmentId |
--+----+-------+--------+--------------+
--| 1  | Joe   | 85000  | 1            |
--| 2  | Henry | 80000  | 2            |
--| 3  | Sam   | 60000  | 2            |
--| 4  | Max   | 90000  | 1            |
--| 5  | Janet | 69000  | 1            |
--| 6  | Randy | 85000  | 1            |
--| 7  | Will  | 70000  | 1            |
--
--
--
--
--1. name | salary(second highest ) | depart ID

with salaryRankedByDept as (
	select *,
	rank() over(patition by dept order by salary desc) as rankedSalaryByDept
	from emp
)

select
	name,
	salary,
	dept_id
from salaryRankedByDept
where rankedSalaryByDept = 2


-- 2. ## Rolling sum of salary

select
	*,
	sum(salary) over(order by id) as RolingSumSalary
from emp

-- 3. Given below tables find total base and annual salary of the person
--emp{id, name, date_modified}
--
--salary{id, component(hra, etc, basic), month, year, amount, date_modified }
--
--fact emp(id, name, total_annual_salary, total_annual_base_pay) ## This table we have to populate

SELECT
    emp.id,
    emp.name,
    salary.year,
    sum(amount) as total_annual_salary,
    sum(case
        when salary.component = "base" then amount
        else 0
        end) as total_annual_base_pay
FROM emp
inner join salary
on emp.id = salary.id
group by emp.id,salary.year
