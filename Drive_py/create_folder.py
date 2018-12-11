from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import json

SCOPES = 'https://www.googleapis.com/auth/drive'

def main():
	store = file.Storage('token.json')
	creds = store.get()
	if not creds or creds.invalid:
		flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
		creds = tools.run_flow(flow, store)
	drive_service = build('drive', 'v3', http=creds.authorize(Http()))
	file_metadata = {
	    'name': 'hello_edit',
	    'mimeType': 'application/vnd.google-apps.folder'
	}
	folder = drive_service.files().create(body=file_metadata,
	                                    fields='id').execute()
	print ('Folder ID: %s' % folder.get('id'))
	
	#https://drive.google.com/drive/folders/1KUqiSfEprOuNeRrxj6vWQAfMsWrrWLc6?usp=sharing
	print()

if __name__ == '__main__':
	main()

