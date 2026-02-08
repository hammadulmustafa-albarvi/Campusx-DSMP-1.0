delimiter $$
create procedure hello_world()
begin
select 'hello world';
end $$
delimiter ;

call hello_world();

delimiter $$
create procedure add_gmail(in gmail varchar(255),in names varchar(255))
begin
-- declare gmail varchar(255);
if exists(select * from users where email = gmail)
then select 'email already exist';
else
insert into users(name,email) values (gmail,names);
end if;
end $$
delimiter ;

call add_gmail('arslan','arslan@gmail.com');


delimiter $$
create procedure user_orders(in gmail varchar(255) )
begin
select * from users t1  join orders t2 on t1.user_id=t2.user_id where email = gmail;
end $$
delimiter ;

call user_orders('vartika@gmail.com');

delimiter $$
create procedure user_orders(in user_id_ int , in r_id_ int , in f_id_ int )
begin
declare order_id_ int ;
insert into orders(user_id,r_id) values (user_id_,r_id_);
select order_id into order_id_ from orders order by order_id desc limit 1 ;
insert into order_details(order_id,f_id) values (order_id_,f_id_);
select price from menu where f_id = f_id_ and r_id = r_id_;
end $$
delimiter ;

call user_orders(7,1,2)