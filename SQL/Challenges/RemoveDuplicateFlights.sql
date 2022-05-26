--Remove duplicates from Flight table
--https://www.interviewquery.com/questions/flight-records
--
-- table
--
--column	type
--id	integer
--source_location	string
--destination_location	string
--Write a query to create a new table, named flight routes, that displays unique pairs of two locations.
--
--Example:
--
--Duplicate pairs from the flights table, such as Dallas to Seattle and Seattle to Dallas, should have one entry in the flight routes table.
--
--Output:
--
--column	type
--destination_one	string
--destination_two	string




drop table  flights;

create table flights(
id	integer,
source_location	string,
destination_location	string );


INSERT INTO flights VALUES('1','delhi','mumbai');
INSERT INTO flights VALUES ('2','mumbai','delhi');
INSERT INTO flights VALUES ('3','mumbai','banglore');
INSERT INTO flights VALUES ('4','banglore','mumbai');
INSERT INTO flights VALUES ('5','banglore','delhi');
INSERT INTO flights VALUES ('6','delhi','banglore');

select * from flights;

select
    f1.id AS f1_id,
--    f2.id AS f2_id,
    f1.source_location source_location1,
    f2.source_location
from flights f1
inner join flights f2
on f1.source_location = f2.destination_location
and f2.source_location = f1.destination_location
and f1.id>f2.id

-- OR

WITH dup_record AS (
    select
        f1.id AS f1_id,
        f2.id AS f2_id
 from flights f1
inner join flights f2
on f1.source_location = f2.destination_location
and f2.source_location = f1.destination_location
and f1.id>f2.id
)

SELECT
    c.id,
    c.source_location,
    c.destination_location
FROM
    flights c
    inner join dup_record d
    on c.id=d.f1_id;