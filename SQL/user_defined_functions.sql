-- user defined functions

select hello_world();

DELIMITER $$
create function calculate_age(dob date)
returns integer 
deterministic 
begin
declare age int;
set age = round(datediff(date(now()),dob)/365);
return age;
end $$
DELIMITER ;

select calculate_age('2000-10-11');

DELIMITER $$
create function proper_name(name varchar(255), gender varchar(255),married varchar(255))
returns varchar(255) 
deterministic 
begin 
declare title varchar(255);
set name = concat(upper(left(name,1)),lower(substring(name,2)));
if gender = 'M' then set title = concat('mr',' ',name);
else 
	if married = 'Y' then set title = concat('mrs',' ',name);
    else set title = concat('ms',' ',name);
    end if ;
end if;
return title;
end $$
DELIMITER ;

select proper_name('ahmeD','M','N')


DELIMITER $$
create function converted_date(date_to_convert varchar(255))
returns varchar(255) 
deterministic 
begin 
declare dates varchar(255);

set dates = str_to_date(date_to_convert,'%Y-%m-%d');
return date_format(dates,'%D %b %y');
end $$
DELIMITER ;

select converted_date('2002-09-01');




DELIMITER $$
create function deterministic_examp(city varchar(255))
returns int
not deterministic 
reads sql data
begin 
declare flights int ;
set flights = (select count(*) from flights.flights where Source = 'Banglore');
return flights;
end $$
DELIMITER ;

select deterministic_examp('Banglore')

