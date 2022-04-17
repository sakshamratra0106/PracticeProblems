-- https://leetcode.com/problems/rising-temperature/
-- https://leetcode.com/problems/rising-temperature/discuss/1949625/90-Faster-Solution-With-Lag-Function

--# Not Working
--# SELECT
--#     a.id
--# FROM Weather a
--# inner join Weather b
--# ON a.id - 1 = b.id
--# WHERE a.temperature > b.temperature
--
--# Working
--# SELECT w1.id
--# FROM Weather w1, Weather w2
--# WHERE w1.recordDate = Date_add(w2.recordDate, Interval 1 Day)
--# AND w1.temperature > w2.temperature


SELECT id FROM (
    SELECT
        *,
        LAG(temperature) OVER(ORDER BY recordDate) AS prevTemperature,
        DATEDIFF(recordDate, LAG(recordDate) OVER(ORDER BY recordDate)) AS dateDiff
    FROM Weather
) t
WHERE dateDiff = 1 AND temperature > prevTemperature;