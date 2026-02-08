
create table uber_rides(
ride_id integer primary key auto_increment,
user_id integer ,
cab_id integer,
start_time datetime,
end_time datetime

);

 
insert into uber_rides(user_id,cab_id,start_time,end_time) values
(22,33,'2025-04-11 06:00:00',now());


-- curr_date()
-- curr_time()
-- now()

-- extraction fuctions

select date(start_time) from uber_rides;
select time(start_time) from uber_rides;
select year(start_time) from uber_rides;
select month(start_time) from uber_rides;
select monthname(start_time) from uber_rides;
select day(start_time) from uber_rides;
select dayofweek(start_time) from uber_rides;
select dayname(start_time) from uber_rides;
select quarter(start_time) from uber_rides;
select hour(start_time) from uber_rides;
select minute(start_time) from uber_rides;
select second(start_time) from uber_rides;
select dayofyear(start_time) from uber_rides;
select weekofyear(start_time) from uber_rides;
select last_day(start_time) from uber_rides;
select date_format(start_time,'%d %b %y')from uber_rides;
select date_format(start_time,'%l : %i %p') from uber_rides;

-- type conversion ( implicit ) 
select '2023-03-11' > '2023-03-09';
select '2023-03-11' > '09 Mar 2023';

-- explicit type conversion 

select monthname(str_to_date('8-Dec-hi-2024','%e-%b-hi-%Y'));


select datediff(end_time,start_time) from uber_rides;

select timediff(end_time,start_time) from uber_rides;

select date_add(now(),interval 10 YEAR);

select date_add(now(),interval 1 month);

select date_add(now(),interval 1 day);

select date_add(now(),interval 1 hour);

select date_add(now(),interval 1 minute);

select date_add(now(),interval 1 week);

select date_add(now(),interval 10 YEAR);

select date_sub(now(),interval 1 month);

select date_sub(now(),interval 1 day);

select date_sub(now(),interval 1 hour);

select date_sub(now(),interval 1 minute);

select date_sub(now(),interval 1 week);


-- time stamp

-- range : datetime support 1000-01-01  to 9999-01-01 where as time stamp only 
-- store upto 1970-01-01 to 2038-01-01

-- storage : date time use 8 bytes where as timestamp takes 4 bytes

-- behaviour on insertion/delete : date time on updation remains same
-- whereas the timestamp converts data in format of UTC 

-- precision : datetime can store upto seconds whereas timestamp can store 
-- upto seconds 

-- auto_update : timestamp can be set to update automatically when inserted 
-- on update current_time_stamp


create table posts(
post_id integer primary key auto_increment,
user_id integer,
content text,
created_at timestamp default current_timestamp(),
updated_ad timestamp default current_timestamp on update current_timestamp() ) ;

select * from posts;
insert into posts(user_id,content) values(1,'hello world');

update posts 
set content = 'No more hello world'
where post_id = 1;



select monthname(Date_of_Journey),count(*) from flights group by monthname(Date_of_Journey) order by count(*) desc limit 1;


select dayname(Date_of_Journey),avg(Price) from flights group by dayname(Date_of_Journey) order by avg(Price) desc limit 1;

select monthname(Date_of_Journey),count(*) from flights where Airline='IndiGo'  group by monthname(Date_of_Journey) ;

select * from flights where Source = 'Banglore' and Destination = 'New Delhi' and Dep_Time between '10:00' and '14:00';

select count(*) from  flights where Source = 'Banglore' and dayname(Date_of_Journey) in('Saturday','Sunday');

select *,str_to_date(Duration,'%i') from flights ;

alter table flights add column departure datetime;

update flights
set departure = str_to_date(concat(Date_of_Journey,' ',Dep_Time),'%Y-%m-%e %H:%i');


alter table flights add column arrival DATETIME;

update flights
set arrival = date_add(departure,interval Duration minute) ;


select time(arrival) from flights ;


select count(*) from flights where date(departure) != date(arrival);


select Source,Destination,time_format(sec_to_time(avg(duration)*60),'%k : %i m') from flights group by Source,Destination;

select * from flights  where date(departure) != date(arrival) and Total_Stops = 'non-stop' and date_format(arrival,'%H') = '00';

select quarter(departure),airline,count(*) from flights group by quarter(departure),airline;

select 
avg(case when Total_Stops = 'non-stop' then Duration end) as '1_stop',
avg(case when Total_Stops not in ('non-stop') then Duration  end) as 'more_than_1_stop'
from flights;

select * from flights where Airline = 'Air India' and departure between '2019-01-15' and '2019-01-20';

select Airline,max(Duration) from flights group by Airline;

select Source,Destination,avg((duration)) from flights  group by Source,Destination having avg(duration) > 180 ;


select dayname(departure) ,
sum(case when time(departure) between '00:00:00'  and '05:59:59' then 1 else 0 end),
sum(case when time(departure) between '06:00:00'  and '11:59:59' then 1 else 0 end),
sum(case when time(departure) between '12:00:00'  and '17:59:59' then 1 else 0 end),
sum(case when time(departure) between '18:00:00'  and '23:59:59' then 1 else 0 end)
from flights
where Source = 'Banglore' and Destination = 'Delhi' 
group by dayname(departure);




select dayname(departure) ,
avg(case when time(departure) between '00:00:00'  and '05:59:59' then price  end),
avg(case when time(departure) between '06:00:00'  and '11:59:59' then price end),
avg(case when time(departure) between '12:00:00'  and '17:59:59' then price  end),
avg(case when time(departure) between '18:00:00'  and '23:59:59' then price  end)
from flights
where Source = 'Banglore' and Destination = 'Delhi' 
group by dayname(departure);





















