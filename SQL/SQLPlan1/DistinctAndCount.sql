-- https://leetcode.com/problems/find-followers-count/

SELECT
    user_id,
    count(*) AS followers_count
FROM followers
GROUP BY user_id
ORDER BY user_id

-- https://leetcode.com/problems/daily-leads-and-partners/

SELECT
    date_id,
    make_name,
    count(DISTINCT lead_id) AS unique_leads ,
    count(DISTINCT partner_id ) AS unique_partners
FROM DailySales
GROUP BY date_id, make_name

-- https://leetcode.com/problems/user-activity-for-the-past-30-days-i/

SELECT
    activity_date AS day,
    count(DISTINCT user_id) AS active_users
FROM ACTIVITY
WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27'
GROUP BY activity_date
HAVING COUNT(*) > 0