from __future__ import print_function
from io import BytesIO
import os.path, time, dateutil.parser
from os.path import exists
import frontmatter
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import datetime
import yaml
import os
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/contacts.readonly']
global sPath="<FullPath>/PKM/300 CRM/02 People/"
global sMeetingPart="300 CRM/01 Meetings"

def main():
    global sPath
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('credentials/token.json'):
        creds = Credentials.from_authorized_user_file('credentials/token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials/peoplecreds.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('credentials/token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('people', 'v1', credentials=creds)

        # Call the People API
        print('List all connection names')
        results = service.people().connections().list(
            resourceName='people/me',
            pageSize=2000,
            sortOrder="LAST_MODIFIED_DESCENDING",
            personFields='metadata,names,emailAddresses,coverPhotos,genders,nicknames,occupations,organizations,urls,phoneNumbers,addresses,birthdays').execute()
        connections = results.get('connections', [])

        for person in connections:
            obsFrontmatter={}
            names = person.get('names', [])
            if names:
                name = names[0].get('displayName')
                print(name)
                obsFrontmatter["name"] = name 
                obsFrontmatter["aliases"] = name 
                obsFrontmatter["context"] = "gmail"
                obsFrontmatter["ping"] = ""
                
            else:
                continue
            obsFrontmatter["etag1"] = person["etag"]
            obsFrontmatter["modifyDate"] =  datetime.datetime.now()
            genders=person.get('genders', [])
            if genders:
                gender=genders[0].get('formattedValue')
            else:
                gender=""
            obsFrontmatter["gender"] = gender    
            obsFrontmatter["resourceName"] = person["resourceName"]

            birthdays=person.get('birthdays', [])
            if birthdays:
                birthday=birthdays[0].get('text')
            else:
                birthday=""
            obsFrontmatter["birthday"] = birthday 

            emailAddresses=person.get('emailAddresses', [])
            if emailAddresses:
                for index,emailAddress in enumerate(emailAddresses, start=1):
                    obsFrontmatter["emailAddress" + str(index)] = emailAddress["value"]
            else:
                obsFrontmatter["emailAddress1"] = ""

            metadatas=person.get('metadata', [])
            if metadatas:
                for index,metadata in enumerate(metadatas["sources"], start=2):
                    obsFrontmatter["etag" + str(index)] = metadata["etag"]
                    if metadata["type"] != "CONTACT":
                        continue
                    try:
                        obsFrontmatter["updateTime"] = metadata["updateTime"]
                        exit
                    except Exception as typeerr:
                        obsFrontmatter["updateTime"] =datetime.datetime.now().isoformat()
            else:
                obsFrontmatter["etag2"] = ""
                obsFrontmatter["updateTime"] = datetime.datetime.now().isoformat()

            urls=person.get('urls', [])
            if urls:
                for index,url in enumerate(urls, start=1):
                    obsFrontmatter["website" + str(index)] = url["value"]
            else:
                obsFrontmatter["website1"] = ""

            addresses=person.get('addresses', [])
            if addresses:
                for index,address in enumerate(addresses, start=1):
                    obsFrontmatter["address" + str(index)] = address["formattedValue"].replace("\n", "; ")
                    try:
                        obsFrontmatter["location"] = address["region"]
                    except Exception as typeerr:
                        obsFrontmatter["location"] = ""
            else:
                obsFrontmatter["address1"] = ""
                obsFrontmatter["location"] = ""

            phoneNumbers=person.get('phoneNumbers', [])
            if phoneNumbers:
                for index,phoneNumber in enumerate(phoneNumbers, start=1):
                    obsFrontmatter["phoneNumber" + str(index)] = phoneNumber["value"]
                    try:
                        obsFrontmatter["phoneNumberType" + str(index)] = phoneNumber["type"] 
                    except Exception as typeerr:
                        obsFrontmatter["phoneNumberType" + str(index)]=""
            else:
                obsFrontmatter["phoneNumbers1"] = ""
                obsFrontmatter["phoneNumberType1"]=""

            coverPhotos=person.get('coverPhotos', [])
            if coverPhotos:
                coverPhoto=coverPhotos[0].get('url')
            else:
                coverPhoto=""
            obsFrontmatter["coverPhoto"] = coverPhoto  

            nicknames=person.get('nicknames', [])
            if nicknames:
                nickname=nicknames[0].get('value')
                obsFrontmatter["aliases"]=obsFrontmatter["aliases"] + ", " + nickname
            else:
                nickname=""
            obsFrontmatter["nickname"]= nickname

            organizations=person.get('organizations', [])
            if organizations:
                organization=organizations[0].get('name')
                try:
                    title=organizations[0].get('title')
                except Exception as typeerr:
                    title=""
            else:
                organization=""
                title=""
            obsFrontmatter["company"] = organization  
            obsFrontmatter["title"] = title  

            
            filename=name
            body="".join(["\n","## Notes\n","-\n\n","## Meetings\n"])
            body="".join([body,"```dataview","\n","TABLE file.cday as Created, summary AS Summary","\n","FROM \"", sMeetingPart ,"\" where contains(file.outlinks, [[<% tp.file.title %>]])","\n","SORT file.cday DESC","\n","```","\n",])
            body="".join([body,"\n\n","tags:: [[People MOC]]"])
            filename="".join([c for c in filename if c.isalpha() or c.isdigit() or c==' ']).rstrip() + '.md'
            fullFile="".join([sPath,filename])
            if not exists(os.path.join(sPath,filename)):
                obsFrontmatter["created"] = datetime.datetime.now()
                with open(fullFile, 'w', encoding="utf-8") as outfile:
                    dump=yaml.dump(obsFrontmatter,  default_flow_style=False)
                    outfile.write ("".join(["---\n",dump,"---\n",body]))
            else:
                post={}
                #with open("".join([sPath,filename]),encoding="utf-8") as outfile:
                if dateutil.parser.isoparse(obsFrontmatter["updateTime"]) > dateutil.parser.isoparse(datetime.datetime.fromtimestamp(os.path.getmtime(fullFile)).isoformat()+ "+00:00"):
                    post = frontmatter.load(fullFile)
                    postSave=frontmatter.load(fullFile)
                    for item in obsFrontmatter:
                        try:
                            post[item]=obsFrontmatter[item]
                        except Exception as err:
                            post[item]=postSave[item]
                    for postitem in post.metadata:
                        try:
                            post[postitem]=obsFrontmatter[postitem]
                        except Exception as err:
                            post[postitem]=postSave[postitem]
                    for item in ["context","ping"]:
                        try:
                            post[item]=postSave[item]
                        except Exception as err:
                            post[item]=post[item]
                    with open("".join([sPath,filename]), 'w',encoding="utf-8") as outfile:     
                        print(frontmatter.dumps(post))  
                        outfile.write(frontmatter.dumps(post))  

                        pass #this will update frontmatter
    except Exception as err:
        print(err)


if __name__ == '__main__':
    main()
