-- https://leetcode.com/problems/customers-who-never-order/

-- Write your MySQL query statement below

SELECT
    customers.name as Customers
FROM Customers
left outer join Orders
    on Customers.id = Orders.customerId
where Orders.customerId is Null
