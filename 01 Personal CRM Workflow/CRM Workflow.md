# Summary
I use this setup to take meeting notes and set notes on people, which helps me remember what was talked about on which day.

When I'm in a meeting, I hit CTRL-M, which launches QuickAdd. I select Meeting, then it asks for the meeting name.  The date is appended to the filename automatically. The Meeting template includes a button to create a note from the People template.

The People template has a dataview snippet that fetches all of the meetings I've had with that person.

There is a Map of Content for Meetings and for People that uses Dataview let's me see all of the meetings I've had and all of the people I've had meetings with. I used YAML frontmatter to organize all of the dataview snippets. I haven't found myself using the MOCs much.

# Plugins
- [Templater](https://github.com/SilentVoid13/Templater)
- [Buttons](https://github.com/shabegom/buttons)
- [Quick Add](https://github.com/chhoumann/quickadd)
- [Dataview](https://github.com/blacksmithgu/obsidian-dataview)

# Templates
- Meeting Template
	- date: Date, filled in by the template
	- type: meeting
	- company: What company is driving the need for this meeting?
	- summary: A short summary that shows up in the dataview snippet.
	- context: This could be "Personal", "Work", "Family", etc.
- People Template
	- YAML
		- company: What company does this person work for?
		- location: Where are they located?
		- title: Job title
		- email: Their email address
		- phone: Their phone number
		- address: Their address on one line
		- website: Website, if relevant
		- aliases: This lets me reference notes by other names.
		- context: This could be "Personal", "Work", "Family", etc.
		- ping: This allows a dataview snippet to retrieve a person based on the day I want to ping them. It's a reminder to stay in contact with the people I care about.

# Ping
A ping is a contact. Based on the book [Never Eat Alone](https://amzn.to/3H8Q5EG), which I haven't read in 15 years, I like to contact the people I care about and I schedule that. It helps remind me to not let those people fall through the cracks when life gets busy.

"nea/" is the ping value that drives this. The number after the / tells dataview what day to remind me to ping that person. I have that in my daily note template.

# Configuration
- General
	- I create a hotkey using CTRL-M for the command QuickAdd: Run QuickAdd
- Templater
	- There's nothing special about this setup.
- Buttons
	- There's nothing to configure.
- Quick Add
	- I set up two templates, Meeting and People and put them in my templates folder.
	- I have a folder for each (Meetings and People).
	- ![[Pasted image 20221203144455.png]]
	- Also, enable a new vertical split and let the new note take focus. These didn't fit the screenshot.
- Dataview
	- There's nothing special about this setup.