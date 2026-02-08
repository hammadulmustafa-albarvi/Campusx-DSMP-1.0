select * from information_schema.tables
where table_schema = 'laptops' and table_name = 'laptopsdata';

-- select * from laptopdata;

-- alter table laptopdata drop column `Unnamed: 0`;

select * from laptops;

DELETE FROM laptops 
WHERE `Unnamed: 0` IN (select id from  (SELECT `Unnamed: 0` as id FROM laptops
WHERE Company IS NULL AND TypeName IS NULL AND Inches IS NULL
AND ScreenResolution IS NULL AND Cpu IS NULL AND Ram IS NULL
AND Memory IS NULL AND Gpu IS NULL AND OpSys IS NULL AND
WEIGHT IS NULL AND Price IS NULL ) as tmp );

select count(*) from laptops;

select distinct(typename) from laptops;

alter table laptops modify column inches decimal(10,1);

select distinct(screenresolution) from laptops;

select distinct(ram) from laptops;


alter table laptops 
change column `Unnamed: 0` id INT;


update laptops l1
set ram  =  replace(ram,'GB','') ;

select * from laptops;

alter table laptops modify column ram integer;

update laptops
set Weight = replace(Weight,'kg','');

select * from laptops;

alter table laptops modify column Weight FLOAT;

select distinct(opsys) from laptops;

update  laptops

set opsys = case
	when opsys like '%mac%' then 'macos'
    when opsys like 'windows%' then 'windows'
    when opsys like '%linux%' then 'linux'
    when opsys = 'No OS' then 'n/a'
    else 'other'
end ;

select * from laptops ;

alter table laptops 
add column gpu_brand varchar(255) after gpu,
add column gpu_name varchar(255) after gpu_brand;

update laptops
set gpu_brand =  substring_index(gpu,' ',1) ;


select * from laptops ;

--  select gpu,substring_index(gpu,' ',-3) from laptops;
update laptops
set gpu_name =  replace(gpu,gpu_brand,'');


alter table laptops drop column Gpu;

select * from laptops;

alter table laptops 
add column cpu_brand varchar(255) after cpu,
add column cpu_name varchar(255) after cpu_brand,
add column cpu_speed decimal(10,1) after cpu_name;

select * from laptops;

update laptops
set  cpu_brand = substring_index(cpu,' ',1);

select * from laptops;


update laptops 

set cpu_speed =  replace(substring_index(cpu,' ',-1),'GHz','') ;


update laptops
set cpu_name =  replace(replace(cpu,cpu_speed,''),cpu_brand,'');

select * from laptops;

alter table laptops 
drop column Cpu;

select screenresolution,
substring_index(substring_index(screenresolution,' ',-1),'x',1),
substring_index(substring_index(screenresolution,' ',-1),'x',-1)
from laptops;

alter table laptops
add column resolution_width integer after screenresolution,
add column resolution_height integer after resolution_width;


select * from laptops;

update laptops 
set resolution_width = substring_index(substring_index(screenresolution,' ',-1),'x',1),
resolution_height  = substring_index(substring_index(screenresolution,' ',-1),'x',-1);

select * from laptops;

alter table laptops 
add column touchscreen integer after resolution_height;

update laptops
set touchscreen = case
	when ScreenResolution like '%Touchscreen%' then 1
    else 0
end;

select * from laptops;


alter table laptops 
drop column ScreenResolution;

select * from laptops;

update laptops
set cpu_name =  substring_index(trim(cpu_name),' ',2) ;


select distinct(cpu_name) from laptops;

select memory from laptops;

alter table laptops
add column memory_type varchar(255) after memory,
add column primary_storage integer after memory_type,
add column secondary_storage integer after primary_storage;


update laptops
set memory_type = case
	when memory like '%SSD%' and  memory like '%HDD%'  then 'hybrid'
	when memory like '%SSD%' then 'ssd'
    when memory like '%HDD%' then 'hdd'
    when memory like '%Flash Storage%'  then 'flash storage'
    when memory like '%Hybrid%'  then 'hybrid'
    when memory like '%Flash Storage%' and  memory like '%HDD%'  then 'hybrid'
    else NULL
end ;

update laptops
set primary_storage =  regexp_substr( substring_index(Memory,'+',1),'[0-9]+'),
secondary_storage = case
when Memory like '%+%' then regexp_substr(substring_index(Memory,'+',-1),'[0-9]+')
else 0
end;

update laptops
set primary_storage = case 
	when primary_storage <= 2 then primary_storage*1024
    else primary_storage
    end
,

secondary_storage = case 
	when secondary_storage <= 2 then secondary_storage*1024
    else secondary_storage
    end;
    
select * from laptops;

alter table laptops drop column Memory;

select * from laptops;

alter table laptops drop column gpu_name;

select * from laptops;
-- EDA



-- head
select * from laptops limit 5;

-- tail
select * from laptops 
order by id limit 5;

-- random 
select * from laptops
order by rand() limit 5;

-- 8 number summart
select count(price),
min(price) over(),max(price) over(),avg(price) over(),std(price) over()
-- percentile_cont(0.25) within group(order by price) over()
-- percentile_cont(0.5) within group(order by price) over()
-- percentile_cont(0.75) within group(order by price) over()
from laptops limit 1;

-- missing values
select count(*) from laptops
where price is null


-- outliers
select * from(select *  ,
-- percentile_cont(0.25) within group(order by price) over()
-- percentile_cont(0.5) within group(order by price) over()
-- percentile_cont(0.75) within group(order by price) over()
from laptops) t
where t.price < t.q1 - (1.5*(t.q3-t.q1)) or
t.price > t.q1 + (1.5*(t.q3-t.q1)) ;

-- histogram
select t.buckets,repeat('*',count(*)/5) from(
select price,
case 
when price between 0 and 25000 then  '0-25k'
 when price between 25001 and 50000 then '25k-50k'
 when price between 50001 and 75000 then  '50k-75k'
 when price between 75001 and 100000 then  '75k-100k'
 when price > 100000 then  '>100k'
 end as 'buckets'
from laptops) t
group by buckets;


 -- use values to plot pie chart in excel sheets
select company,count(company) from laptops
group by company ;


-- plot scatter plot in excel
select price,cpu_speed from laptops;


-- find correlation in postgre sql
select corr(cpu_speed,price) from laptops;


-- find stacked bar chart
select company,
sum(case when touchscreen = 1 then 1 else 0 end ) as 'yes',
sum(case when touchscreen = 0 then 1 else 0 end ) as 'no'
from laptops
group by company;


select company,avg(price) from laptops
group by company;


update laptops 
set price = NULL  
where `id` in (7,869,1148,827,865,821);


select * from laptops
where price is null;

update laptops
set price = (select avg(price) from laptops)
where price is null;

update laptops t1 join
(select company,cpu_name,avg(price) as avg_price  from laptops t2 where price is not null group by company,cpu_name ) t2
on t1.company =t2.company
and t1.cpu_name = t2.cpu_name
set t1.price = t2.avg_price
where t1.price is null;

select * from laptops where price is null;

alter table laptops add column ppi integer;


select * from laptops;

update laptops
set ppi = round(sqrt((resolution_width * resolution_width)+(resolution_height*resolution_height))/inches) ;

select * from laptops order by ppi desc ;

alter table laptops add column screen_size varchar(255) after inches;

update laptops
set screen_size = case 
when inches < 14 then 'small'
when inches >= 14 and inches < 17 then 'medium'
else 'large'
end;

select screen_size,avg(price) from laptops group by screen_size;


select 
(case when gpu_brand = 'Intel' then 1 else 0 end) as 'Intel',
(case when gpu_brand = 'AMD' then 1 else 0 end) as 'AMD',
(case when gpu_brand = 'Nvidia' then 1 else 0 end) as 'Nvidia',
(case when gpu_brand = 'ARM' then 1 else 0 end) as 'ARM'
from laptops












