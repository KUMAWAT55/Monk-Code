/*ORACLE*/
select city,length(city) from (select city,rownum as rid from (select city,length(city) from station order by length(city),city)) where rid = 1 or rid = (select max(rownum) from station);
