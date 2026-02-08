-- documentation on views
-- https://dev.mysql.com/doc/refman/8.4/en/view-updatability.html


create view indigo as 
select * from flights 
where airline ='indigo airline';

select * from indigo;

create view joined_order_data as 
select order_id,amount,r_name,name,date,delivery_time,delivery_rating,
restaurant_rating
 from orders t1
join users t2
on t1.user_id = t2.user_id 
join restaurants t3
on t1.r_id = t3.r_id;

select r_name,monthname(date),sum(amount) from joined_order_data group by r_name,monthname(date);

select * from flights;

update flights 
set source = 'Banglore'
where Source = 'Bengaluru';

update indigo 
set Destination = 'Delhi'
where Destination = 'New Delhi';

select * from flights;

delete from zomato.joined_order_data
where order_id = 1001; -- it cant be deleted because its 
-- read only view for further view the documentation
-- https://dev.mysql.com/doc/refman/8.4/en/view-updatability.html




