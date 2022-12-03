
## Ping 

```dataview
table rows.file.link as Name,  rows.title as Title, rows.email as Email, rows.phone as Phone
FROM "03 Work/02 People" 
where context="personal" and ping="nea/<% tp.date.now("DD") %>" 
SORT company, file.cday DESC
group by company AS "Company"
limit 20
```



