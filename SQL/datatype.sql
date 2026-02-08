create table dt_practice(
user_id tinyint,
course_id tinyint unsigned
);

insert into dt_practice values(127,200,456.243);

select * from dt_practice;

alter table dt_practice add column price decimal(5,2);
alter table dt_practice add column height float;
alter table dt_practice add column weight double;
alter table dt_practice add column gender enum('male','female','others');
alter table dt_practice add column hobby set('gaming','football');
alter table dt_practice add column dp mediumblob;
alter table dt_practice add column latlong geometry;
alter table dt_practice add column descrip json;


update dt_practice
set dp = load_file('path');

update dt_practice
set latlong = point(67.456,89.763);

update dt_practice
set descrip = '{"os":"android","type":"smartphone"}';

select st_astext(latlong),st_x(latlong),st_y(latlong) from dt_practice;


select descrip->>'$.os' from dt_practice;


