from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import json

SCOPES = 'https://www.googleapis.com/auth/drive'

file_id = '1qLTUcXFASDYosBmpjb8BAjBwcoaS4t1W'
def callback(request_id, response, exception):
    if exception:
        # Handle error
        print (exception)
    else:
        print ("Permission Id: %s" % response.get('id'))

store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
	flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
	creds = tools.run_flow(flow, store)
drive_service = build('drive', 'v3', http=creds.authorize(Http()))

batch = drive_service.new_batch_http_request(callback=callback)
user_permission = {
    'type': 'user',
    'role': 'writer',
    'emailAddress': 'duttasparsh18@gmail.com'
}
batch.add(drive_service.permissions().create(
        fileId=file_id,
        body=user_permission,
        fields='id',
))

batch.execute()
