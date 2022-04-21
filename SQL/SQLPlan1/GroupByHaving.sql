-- https://leetcode.com/problems/sales-analysis-iii/submissions/

SELECT Sales.product_id, product_name
FROM Sales INNER JOIN Product ON Product.product_id=Sales.product_id
GROUP BY Sales.product_id
HAVING MAX(sale_date)<='2019-03-31' AND MIN(sale_date)>='2019-01-01'

-- https://leetcode.com/problems/bank-account-summary-ii/

SELECT
    users.name,
    sum(transactions.amount) as balance
FROM Transactions
left join Users
on transactions.account = users.account
GROUP BY transactions.account
HAVING sum(transactions.amount) > 10000

-- https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/submissions/

SELECT
    actor_id,
    director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(*) >= 3

-- https://leetcode.com/problems/duplicate-emails/submissions/

SELECT
    email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1