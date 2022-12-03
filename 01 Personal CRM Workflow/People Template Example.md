---
company:
location:
title:
email:
phone:
address:
website:
aliases:
context: 
ping: #nea/
---

# <% tp.file.title %>
<% await tp.file.move("/03 Work/02 People/" + tp.file.title) %>

## Notes
-

## Meetings

```dataview
TABLE file.cday as Created, summary AS "Summary"
FROM "03 Work/01 Meetings" where contains(file.outlinks, [[<% tp.file.title %>]])
SORT file.cday DESC
```


tags:: [[People MOC]]