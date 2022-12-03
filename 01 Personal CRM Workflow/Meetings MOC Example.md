### 20 Most Recent Meetings
```dataview
table WITHOUT ID file.link as Meeting, company AS "Company", summary as "Summary", file.cday as Created
FROM "03 Work/01 Meetings"
SORT file.cday DESC
limit 20
```


### Meetings by Company
```dataview
table rows.file.link as Meeting,  rows.summary as Summary, rows.file.cday as Created
FROM "03 Work/01 Meetings"
SORT company, rows.file.cday DESC
group by company AS "Company"
limit 200
```

