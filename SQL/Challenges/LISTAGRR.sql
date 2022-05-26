--###Maersk InterView Questions For Data Engineer
--
--==> Run Below in SQL Lite Chrome Extension
--drop table shipment_with_Date;
--
--CREATE TABLE Shipment_with_date (
--  shipment int,
--  place varchar(50),
--  date_recieved date);
--
--insert into shipment_with_date values ('100','Kolkata',to_date('01/09/2019','dd/mm/yyyy'));
--insert into shipment_with_date values ('100','Delhi',to_date('02/09/2019','dd/mm/yyyy'));
--insert into shipment_with_date values ('100','Banglore',to_date('03/09/2019','dd/mm/yyyy'));
--insert into shipment_with_date values ('100','Chennai',to_date('04/09/2019','dd/mm/yyyy'));
--insert into shipment_with_date values ('200','Srinagar',to_date('01/09/2019','dd/mm/yyyy'));
--insert into shipment_with_date values ('200','Chennai',to_date('02/09/2019','dd/mm/yyyy'));
--insert into shipment_with_date values ('200','Mumbai',to_date('03/09/2019','dd/mm/yyyy'));
--
--select * from shipment_with_Date;
--
--with shipment_with_Date_rank as (
--select a.*, rank() over(partition by a.shipment order by a.date_recieved) rank_date
--from shipment_with_Date a
--)
--
--select c.shipment,c.place,
--(select place from shipment_with_Date_rank b where b.shipment=c.shipment and c.rank_date=b.rank_date+1) Prev_Location,
--(select place from shipment_with_Date_rank b where b.shipment=c.shipment and c.rank_date=b.rank_date-1) Next_Location
--from shipment_with_Date_rank c

--==>>Concat strings in multiple rows
--WA SQL row per shipment and route consisting source, destination and intermediary stops with "->"
SELECT a.shipment,
LISTAGG(a.place, '-> ') WITHIN GROUP (ORDER BY a.date_recieved) AS route
FROM shipment_with_Date a
GROUP BY a.shipment