--1.	CDR Data: (Competency tested: SQL)
--TABLE: CDR
--Let’s say a telecom company stores customer information in a table. The table contains CDRs (Call Data Records) of every call customer makes. The columns of the tables are
---	customer_id (varchar 30)
---	call_start_day (date), e.g., 2021-03-02
---	call_end_day (date)
---	call_start_time (varchar 30), e.g., 14:21:15
---	call_end_time (varchar 30)
---	called_number (integer)
---	customer_call_location_city (varchar 30)
---	customer_call_location_state (varchar 30)
---	customer_call_location_zip (integer)
---	called_number_city (varchar 30)
---	called_number_state (varchar 30)
--Question: Write a query to find top 5 customer based on average monthly call_duration in last 12 months. (consider only complete months only e.g., if current date is 2021-03-07, last 12 months: 2020-03-01 – 2021-02-28. Monthly call duration = sum (call duration) where call duration = time difference of call_end_day+ call_end_time and call_start_day+call_start_time)
--Answer:

with customer_avg_monthly_call_duration as (
	select
		--Get Avergae monthly_call_duration
		customer_id,
		avg(monthly_call_duration) as avg_monthly_call_duration
	from (
		-- GET monthly call durations for each customer and month
		-- for past 12 month excluding current month
		select
		customer_id,
		month(call_start_day),
		sum(
			datedifference (
				to_date( to_char( call_end_day , 'YYYY-MM-DD' ) || call_end_time  ,'YYYY-MM-DD HH24:MI:SS.FF')
				-
				to_date( to_char( call_start_day, 'YYYY-MM-DD' ) || call_start_time  ,'YYYY-MM-DD HH24:MI:SS.FF')
			)
		) monthly_call_duration
		from cdr
		where add_months(trunc(sysdate, 'month'), -12) < call_start_day
		and call_end_day  < trunc(sysdate, 'month')
		group by customer_id, month(call_start_day)
	)
)


select
	-- Getting top 5 customers
	customer_id,
	avg_monthly_call_duration,
	ranked_by_avg_monthly_call_duration
from (
	-- Ranking the customers by avg_monthly_call_duration
	select
		customer_id,
		avg_monthly_call_duration,
		dense_rank() over(order by avg_monthly_call_duration desc) as ranked_by_avg_monthly_call_duration
	from customer_avg_monthly_call_duration )
where ranked_by_avg_monthly_call_duration <= 5


------2.	Flights Data: (Competency tested: SQL)
--Table: FLIGHTS
--The FLIGHTS table lists the airports we fly from, airports we fly to, and ticket price for each flight number and date. The primary key is Flight_Date and Flight_Number.
--Flight_Date	Flight_Number	Departure	Arrival	Flight_Cost
--2021-11-10	001	SEA	LAX	395
--2021-11-10	002	PDX	LAX	161
--2021-11-10	003	SFO	LAX	319
--2021-11-10	004	PHX	SEA	146
--2021-11-10	005	LAX	SFO	486
--2021-11-10	006	SEA	MCO	406
--2021-11-10	007	PDX	DEN	391
--2021-11-10	008	DEN	MCO	331
--2021-11-10	009	MCO	DEN	317
--2021-11-10	010	SEA	LAX	500
--Question: Print the list of distinct airports that have flights between them. Ex. SFO --> LAX and LAX --> SFO counts once.
--Answer:


SELECT f1.departure,
F1.arrival
FROM flights f1
Inner join flights f2
On f1.departure = f2.arrival and f1.departure = f2.arrival
Where f1.flight_number < f2.flight_number

--3.	Customer Orders Data: (Competency tested: SQL)
--Table: CUSTOMER_ORDERS
--Each row in the table is at the level of a customer's order. Order_ID is the PK.
--customer_id	order_id	sales_usd	order_datetime
--A2TF17PFR55MTB	4496	50.6	2021-11-30 16:10:10
--A32DOYMUN6DTXA	92589	27.81	2021-11-30 16:05:07
--A32DOYMUN6DTXA	80710	96.6	2021-11-30 16:18:22
--AB72C64C86AW2	32524	29.36	2021-11-30 16:20:45
--AB72C64C86AW2	74378	11.16	2021-11-30 18:16:08
--A3S5BH2HU6VAYF	47201	53.55	2021-11-30 16:20:43
--A3S5BH2HU6VAYF	50015	73.9	2021-11-30 18:08:19
--A3S5BH2HU6VAYF	81255	80.75	2021-11-30 20:18:52
--A1NL4BVLQ4L3N3	98671	95.75	2021-11-30 17:08:45
--
--Question:
--a.	Write a query that will count the number of unique customers and the average of customers’ average sales amount in November 2021 (01 Nov - 30 Nov 2021).
--b.	Write a query that will produce data used to populate a histogram that shows how many unique orders customers have during the month of November 2021. Ensure the query provides the count of customers who had zero orders in Nov 2021
--Answer: a.

WITH avg_customer_Sales as (
Select customer_id ,
avg(sales_usd) avg_Sales_nov_per_customer,
month(order_Datetime) sale_month
FROM customer_orders
Where month(order_Datetime) = 11
Group by customer_id )

SELECT count(*),
avg(avg_Sales_nov_per_customer)  as avg_Sales_nov
FROM avg_customer_Sales
Group by sale_month

--Answer: b.
--	Given we have customers table and customers_order table
--	Below query gives how many unique orders customers have during the month of November 2021
WITH unique_orders_customers as
(Select
	c.cutomer_id,
	count(co.cutomer_id) as order_count_nov,
month(order_Datetime) sale_month
FROM customers c
Left join customers_orders co
On c.customer_id = co.customer_id
Where month(co.order_Datetime) = 11
Group by c.customer_id)

--	Also if we want to see the count of customers who had zero orders in Nov 2021. We can create a query on top of above query. But it cant be the same query which will give the both the output as granuality of both the query is different.
Select count(*)
FROM unique_orders_customers
Where order_count_nov = 0

