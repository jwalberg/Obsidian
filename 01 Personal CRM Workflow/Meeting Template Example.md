---
date: <% tp.file.creation_date() %>
type: meeting
company:
summary: " "
context: 
---
Date: [[<% tp.date.now("YYYY-MM-DD-dddd") %>]]
<% await tp.file.move("/03 Work/01 Meetings/" + tp.date.now("YYYY-MM-DD") + " " + tp.file.title) %>

# [[<% tp.date.now("YYYY-MM-DD") + " " + tp.file.title %>]]

**Attendees**:
```button
name Create Attendee
type command
action QuickAdd: People
```
- 

## Agenda/Questions
- 

### Todo
- 
## Notes
- 







tags: [[Meetings MOC]]