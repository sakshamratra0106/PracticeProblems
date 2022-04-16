-- https://leetcode.com/problems/combine-two-tables/submissions/

SELECT
    person.firstName,
    person.lastName,
    address.city,
    address.state
FROM person
LEFT JOIN address
ON person.personId = address.personId

-- https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/submissions/

SELECT
    visits.customer_id,
    COUNT(*) AS count_no_trans
FROM visits
LEFT JOIN transactions ON visits.visit_id = transactions.visit_id
WHERE transactions.visit_id IS NULL
GROUP BY visits.customer_id
ORDER BY visits.customer_id

-- https://leetcode.com/problems/article-views-i/submissions/

SELECT
    DISTINCT author_id as id
FROM `views`
WHERE author_id = viewer_id
ORDER BY author_id