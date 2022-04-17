--############Login Event

drop table  login_even

create table login_even(
userid varchar(50),
activity_type varchar(50),
label varchar(50),
app_Version varchar(50),
os_name varchar(50) );


INSERT INTO login_even VALUES('uid1','logged_in','successful',NULL,NULL);
INSERT INTO login_even VALUES ('uid2','logged_out','successful','1.2.4',NULL);
INSERT INTO login_even VALUES ('uid1','logged_out','successful','1.2.3',NULL);
INSERT INTO login_even VALUES ('uid1','scan_start','NULL',NULL,'android');
INSERT INTO login_even VALUES ('uid2','scan_stop','NULL','1.2.4','android');
INSERT INTO login_even VALUES ('uid1','logged_in','successful',NULL,NULL);

select * from login_even
order by userid

-- Populate unique userid with the os_name and app version
-- if any of it is different use the first occurred value in the rows

select
	DISTINCT userid,
	FIRST_VALUE(app_Version) OVER (PARTITION by userid ORDER by userid) app_version,
	FIRST_VALUE(os_name)  OVER (PARTITION by userid ORDER by userid) os_name
FROM login_even