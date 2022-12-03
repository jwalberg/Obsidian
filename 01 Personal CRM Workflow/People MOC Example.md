### Professional Contacts
```dataview
table rows.file.link,  rows.title, rows.file.cday as Created
FROM "03 Work/02 People"
where context="Work"
SORT company, file.cday DESC
group by company AS "Company"
limit 20
```

### Personal Contacts
```dataview
table rows.file.link,  rows.title, rows.file.cday as Created
FROM "03 Work/02 People"
where context="personal"
SORT company, file.cday DESC
group by company AS "Company"
limit 20
```

### 20 Most Recent People
```dataview
table file.cday as Created, company AS "Company", title as "Title"
FROM "03 Work/02 People"
SORT file.cday DESC
limit 20
```

