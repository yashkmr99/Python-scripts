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
	
	rolls = ['180101003','180101015','180101048','180101052','180101053','180101054','180101055','180101056','180101057','180101058','180101065','180101072','180101076','180101079','180101081','180101084','180102005','180102010','180102014','180102020','180102022','180102022','180102039','180102042','180102051','180102053','180102064','180102074','180103002','180103020','180103041','180103047','180103051','180103051','180103051','180103052','180103052','180103052','180103059','180103070','180103073','180103081','180103087','180103089','180103092','180104001','180104002','180104010','180104015','180104019','180104022','180104037','180104042','180104044','180104056','180104057','180104063','180104079','180104086','180104087','180106001','180106036','180106043','180106050','180106052','180107026','180107036','180107057','180108001','180108002','180108003','180108004','180108017','180108020','180108024','180108030','180108036','180121001','180121016','180121040','180121042','180121043','180122015','180122020','180122025','180122027','180122029','180122048','180123029','180123031','180123033','180123037','180123040','180123041','180123045','180123051','180123053']
	gmails = ['anup09092001@gmail.com','bhasker2000goel@gmail.com','niharika.bhamer2@gmail.com','nishtha.idr@gmail.com','niyati2k@gmail.com','paidimar@iitg.ac.in','Param.Aryan@gmail.com','parth.titan@gmail.com ','pooja.bhagat2000@gmail.com','pranavgupta000@gmail.com','songra99@gmail.com','saurabhbaranwal12@gmail.com','shivanshmishra1003@gmail.com','tanneeru.jaswanth777@gmail.com','tejaskhairnar7@gmail.com','anirudh.varanasi1201@gmail.com','ajinkyabhandare01@gmail.com','khabarwalankit001@gmail.com','ashishxtrovert@gmail.com','likhithkumarreddy2001@gmail.com','tarunaguntaka@gmail.com','tarunaguntaka@gmail.com','mandeepchaudharyasawar@gmail.com','msk.mendu@gmail.com','pragthehurricane@gmail.com','hasitha.hastha@gmail.com','samarthsaraswat13@gmail.com','sourav.0344.goel@gmail.com','abhishekdeka31@yahoo.com','bhavya.agarwal2301@gmail.com','maddurinitham333@gmail.com','nihalmohammed79@gmail.com','nivedit20@gmail.com ','nivedit20@gmail.com ','nivedit20@gmail.com ','pathsvaghela@gmail.com','pathsvaghela@gmail.com','pathsvaghela@gmail.com','rahul111jakhad@gmail.com','shivampawar1717@gmail.com','shreyjani83@gmail.com','surendrakumark2012@gmail.com','urvigodha@gmail.com','vajjalavikram@gmail.com','Manan.svora@gmail.com','abhaykandhve6999@gmail.com','liveabhishek7@gmail.com','iamaman1004@gmail.com','ankitmaurya0564@gmail.com','dpraj049@gmail.com','bhaskarnandan52@gmail.com','Shriramgoyal31@gmail.com ','hardik7e@gmail.com ','himanshusingh1301@gmail.com','nikhilshukla721@gmail.com','nikitakhatriya@gmail.com','pratham.iitg@gmail.com','tushargautam588@gmail.com','vishwajiitgoopta@gmail.com','180104087@iitg.ac.in','abdullahjamilahmad@gmail.com','prakhargoyal106@gmail.com','sanskarmodi9@gmail.com','sidrjagtap@gmail.com','somyaagrawal.ime19@gmail.com','kunalagarwal101@gmail.com','rajkumarrajvanshi16@gmail.com','Shridam.mahajan@gmail.com','aryashrivastava19@gmail.com','ahad.jnv22@gmail.com','bansalaman2000@gmail.com','180108004@iitg.ac.in','kartikaeya@gmail.com','kousikr26@gmail.com','nayant1797@gmail.com','prabhakarsharma2001@gmail.com','rajsamal20@gmail.com','adityaadidangi@gmail.com','agarwal.harsh65@gmail.com','saumyashah02@gmail.com','sidd.relativity@gmail.com','sristy.sharma98@gmail.com','db.mail.765@gmail.com','hrithikkumarverma@gmail.com','mayankmalviya64@gmail.com','1512001sagir@gmail.com','nishuranjan95@gmail.com','vinayakagarwal43@gmail.com','ng24645@gmail.com','pankajdinker143@gmail.com ','prathapa@iitg.ac.in','Vijayrathod8422@gmail.com','Samikshasimi26@gmail.com','b.satyadev01@gmail.com','shreyanksnehal@gmail.com','dastrinayan25@gmail.com','vishishtpriyadarshi867@gmail.com']
	Folder_id_list = []
	Folder_id_dict = {}
	for roll in rolls:
		file_metadata = {
	    'name': roll,
	    'mimeType': 'application/vnd.google-apps.folder'
		}
		folder = drive_service.files().create(body=file_metadata,
	                                    fields='id').execute()
		print ('Folder ID for' + str(roll) + ':'' %s' % folder.get('id'))
		Folder_id_list.append(folder.get('id'))
		Folder_id_dict[roll] = folder.get('id')

	print(Folder_id_list)

	print()
	print()

	print(Folder_id_dict)
	

if __name__ == '__main__':
	main()

