# Python Script
The python script will pull your contacts from Google contacts and create files in the CRM format I've described here.

## Configuration
1.  Save the python script somewhere.
2.  Edit the paths on line 16 and 17 to match your Obsidian installation.
3.  Add a subfolder named "credentials"
4.  Follow the instructions here to set permissions and get the credentials file. Save it in the credentials folder as "peoplecreds.json"

## Oopsies
I didn't document as I did it, and I don't remember what libraries I had to add.

It's at least:
- pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
- pip install frontmatter, yaml

