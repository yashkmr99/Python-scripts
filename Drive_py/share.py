from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import json

SCOPES = 'https://www.googleapis.com/auth/drive'

folder_id_list = ['1qLTUcXFASDYosBmpjb8BAjBwcoaS4t1W', '1plDhebz3122hzl3akm-FRWIU3Du43kdJ', '1GynI3KKnFUOEXnNFwOuUC3NqWsBIfXhO', '1GMmFNtstGK4yrAfXMIJtj6ne1xhAW27l', '11h_mTJX6jaPM2mP91XlPCCcFd7xOl021', '1-L3OavGapGChemzXmVM6ms0kKxZN7w_b', '1nJLfIaNDprU6q7hNH5PcjpJrpS-vqBsj', '1Qw75otAicUf6BePDTOqFjSYkY-2EYtAx', '1obU4xgaNNQmJjppjSm_8iiyeDCFmVish', '1hX8d9BDwH7a0s9XakDmcVJzEXknXonD3', '1ngtKvKpOLjT9iyUdIKbWQcSgAl5t5yZV', '1HXOG8xAE72qetUhQWk5oEHd8Zk3-enYD', '1Dgx6K2ndrOeQtswX2vPpUP-Sl0g9W5Fj', '1-bRjbEa2A9ShZmewPcBcPOZHTmuJmgeD', '1oIJ2QUyX7sIWuHEH6sdTWII2H0szOc0H', '1nG2Tg8h6JLZNmrmEQo_lbMGHiRYIGMGH', '1NOVgvcU3PO4-EViXyIlXaYXXttvq1eWY', '1dBdenN5-vWhc20-YgtQ1veLFDSXP77pg', '1Vryp1yGyKsUYmq8Mrv-IANxq0XnhKbz0', '1wX1v06CayYCyuD9SCtTzFzM75FbTOUcH', '1sYU7BIT1ymxb-ZRJeUXtig67S421yM1J', '19Jxo2WASAuGuDnVxgGCEA25GeQaVJ_c0', '1NkrwwDgnZlkYNPnGOUmAYGvi7VacHAlX', '1FdojPRILYBt_KNnFxVtfmw3lgzTLb_E_', '1yuSreg6iYwF_Gbd4AaVowRSR7IZkr-qL', '1lPIsvpIPLFK-4DWG9koC2Rb1Rij9iPe0', '1ULoCs7UvM2Q3xMxBEeYGWUpwXMXQFtMS', '1AT1uqWgPEFiDzQzyldCTrb9yJ33M99bq', '1_-4L61DSSc_BlfEAlGjw-GBUwS56yIUG', '1bpINv9PhqdbeITxVE8mZnyxm4dYanbcq', '11xUCb65lqT76Zxlr__ak4nlrIAY4huGU', '17jqoxlIoWe_AJzvtKXh2A0PlhI5zpJoR', '1ovYozdrQA1cHHlRUKdrMy0uhkf6OZsRN', '1Qp0ixfr-2toVePypqGHXf9bHblvT9qE9', '1x5QVT85jhKw_lcd7w-vFJONmw7CPtTWc', '1GtldGaETziwdOKQnbXrSww1w8hLXt07W', '1LmVYeCzfI222NRDj_50qYw3NK_UyP8_0', '1EtzEzeA0uf46IADqtNqzm-4lV3zO1bor', '1MP_yild7OTU3KV6rXqLNRpBZVYo3R2ZQ', '1Cv9GdeKxNYivEm2ppannWIYUvSSgFTdF', '1CrVvjB21RCgNKGyLWolwhMsQMoNulNLZ', '1uEqRGXFHXXDY-yPSGdRQr3iiEJ3y8cYu', '1HSFJxmYS0gRgUWTPExxPgm362CkOpjRA', '1pF3fLD-glc89DWGC9SrDwDb8ywko-wMl', '1L8i5CWezf_lOWazM2I6swkt8pWTdVcuq', '1tJIm6HD_fiVsAkyJdRy6SVgMzxqCJJR-', '1k6zsIPrwtZ7mMfZVgQPbF6Sm36e71vBq', '1xNakDnyt2yJYt1akXskM3Mm7UH1wpCBw', '1jBIcPh9VZmHlk2Z3Z8m0Q-bCYB0LqivQ', '1w8tmYgCx7smSy1sZpuVjjId5Jnl5HCol', '15KBopfhn-sU95cWjbXeTmJHdU8089Qvr', '1viiHKLID9imbgZL7T5h0IIa4PyRzje69', '1hux9PneSEG9ytQAIcYd2gEmpmrNXdSzc', '1XCr9eQ809Jm-7YRwinEMaEbmpOieJx8b', '1MFOQBkccHLrKx9JuFOyF1TRWZrrb1dTr', '1gPh6NIxlC_Xf8MWCfTvR4njOqJE8uWqY', '1EPR0743YDjbMQBbvlE3cIOv3cTcsko1U', '1oyk8B2hJGXybQWElUAyjWsUgILRFA2VB', '12ElwLwY831MSYGes3jzK8PaF9cwtClt0', '1inC22Vbzk0rknLEvq979dsJVmbYuh9bD', '1PhOw5VQX9g29O0aZblcy5695mIHDAtsX', '1cLT1noM8hxmKBWkGyKPIxIXdJEi4NV_n', '1lElOeAda0zmZ_kF2189lrCql2FK0bIQf', '1x-aYoxIQL3NDjCcUHLYqgrmkw_g3hzsu', '1rol5dB88Zmrn5fGQhAvSIxsd_azMUE0O', '13sNAfBUJLyPQ-tO_UR0Ohsh001sudUAC', '1RPl7hQLznt6ONU_ViNnBVhyitf33EhcD', '1Ln3dMM0-nvbPjI0CByk-DKXa3wMdcwBW', '1-G9twSLPo1dkIyjWZ2GWT5GhM-qsoCEq', '1jy_1t-rl9diUGG-MJSPjqkhsJ66y81cp', '1LibMpYIrUTg7yKhCjZm_TcF2kgwd9kop', '113tLO8qGwGww6uH6c-qfso2bwZ0gRgYD', '19pnDuCLKIEd7W3uyWbZv7rXVmf4Vhcdq', '1a7JeWlk1WAGboE58Sg9lrAP6nTh6vIuf', '1Bvxryh1pDYsrjb7SBtS0DGvmuuKJY7Hf', '1kLeaoFcdbmFOHhf0xg5MH6m4tUAismK2', '1Vwm28knLTmm5M3qmJsQhNM0SCYfFXkpe', '1As1fZKaZc9ukR0eeqRqhX8FostI4nIdJ', '17PY-eCzIJKdtWtzscnU02gfcFaWW0eLD', '15tN0hMbAJrDIQE9bGqSAZSnoSRlmXg3K', '1NLAIOpdZuIDmzWyKPCFgXgyzsijbazZI', '1YWI5w6K7ko2S3OvjzBDKS4amkbEvzFnZ', '1OQ2ABODQhu6FL7C35xc_qdeR0DViSFkW', '1o9AWe7uT9voea0JwlMS818HiTr8cLHiT', '1Y8pb9R0HWVlfycWQuXdBZc_b5oakn8nq', '1xV1D5F8TJCw5DMTGfDSwEomgkxKmzf2f', '1MgeUS_uXxOudU2pqKU_r-EYiKwKmhFdu', '1-_qbYdU4d2SvT7K5I25OxqnddrDrzIpk', '1HwK58js3zgEg2rD54VAHuaUPJR2gy1gW', '1hcJwcybJx86ASqVWE7fDfWTtXx6HKj4h', '16kmPOfnRMRLynFHt5PumVNDwOfndp8Qf', '16fC35rKUFyk9SuKep8PwMMufJqO_8PPF', '1pFVwCOvhP1WuJ1EPvo79mHGhkFC8GwmU', '1Fpc4nD3kGzofZ7hqBH_pWxtRA-GvFsFM', '1VinAeZIVgOG24WSV8GACTjfUI8m9RZgr', '1uxfBrRSsLz_NE9V-tDDFsQgH8XeVi4UW', '1-sqm46JNAZZGNNHLs0L_JGMtS2WWAJ5A']

gmails = ['anup09092001@gmail.com','bhasker2000goel@gmail.com','niharika.bhamer2@gmail.com','nishtha.idr@gmail.com','niyati2k@gmail.com','paidimar@iitg.ac.in','Param.Aryan@gmail.com','parth.titan@gmail.com ','pooja.bhagat2000@gmail.com','pranavgupta000@gmail.com','songra99@gmail.com','saurabhbaranwal12@gmail.com','shivanshmishra1003@gmail.com','tanneeru.jaswanth777@gmail.com','tejaskhairnar7@gmail.com','anirudh.varanasi1201@gmail.com','ajinkyabhandare01@gmail.com','khabarwalankit001@gmail.com','ashishxtrovert@gmail.com','likhithkumarreddy2001@gmail.com','tarunaguntaka@gmail.com','tarunaguntaka@gmail.com','mandeepchaudharyasawar@gmail.com','msk.mendu@gmail.com','pragthehurricane@gmail.com','hasitha.hastha@gmail.com','samarthsaraswat13@gmail.com','sourav.0344.goel@gmail.com','abhishekdeka31@yahoo.com','bhavya.agarwal2301@gmail.com','maddurinitham333@gmail.com','nihalmohammed79@gmail.com','nivedit20@gmail.com ','nivedit20@gmail.com ','nivedit20@gmail.com ','pathsvaghela@gmail.com','pathsvaghela@gmail.com','pathsvaghela@gmail.com','rahul111jakhad@gmail.com','shivampawar1717@gmail.com','shreyjani83@gmail.com','surendrakumark2012@gmail.com','urvigodha@gmail.com','vajjalavikram@gmail.com','Manan.svora@gmail.com','abhaykandhve6999@gmail.com','liveabhishek7@gmail.com','iamaman1004@gmail.com','ankitmaurya0564@gmail.com','dpraj049@gmail.com','bhaskarnandan52@gmail.com','Shriramgoyal31@gmail.com ','hardik7e@gmail.com ','himanshusingh1301@gmail.com','nikhilshukla721@gmail.com','nikitakhatriya@gmail.com','pratham.iitg@gmail.com','tushargautam588@gmail.com','vishwajiitgoopta@gmail.com','180104087@iitg.ac.in','abdullahjamilahmad@gmail.com','prakhargoyal106@gmail.com','sanskarmodi9@gmail.com','sidrjagtap@gmail.com','somyaagrawal.ime19@gmail.com','kunalagarwal101@gmail.com','rajkumarrajvanshi16@gmail.com','Shridam.mahajan@gmail.com','aryashrivastava19@gmail.com','ahad.jnv22@gmail.com','bansalaman2000@gmail.com','180108004@iitg.ac.in','kartikaeya@gmail.com','kousikr26@gmail.com','nayant1797@gmail.com','prabhakarsharma2001@gmail.com','rajsamal20@gmail.com','adityaadidangi@gmail.com','agarwal.harsh65@gmail.com','saumyashah02@gmail.com','sidd.relativity@gmail.com','sristy.sharma98@gmail.com','db.mail.765@gmail.com','hrithikkumarverma@gmail.com','mayankmalviya64@gmail.com','1512001sagir@gmail.com','nishuranjan95@gmail.com','vinayakagarwal43@gmail.com','ng24645@gmail.com','pankajdinker143@gmail.com ','prathapa@iitg.ac.in','Vijayrathod8422@gmail.com','Samikshasimi26@gmail.com','b.satyadev01@gmail.com','shreyanksnehal@gmail.com','dastrinayan25@gmail.com','vishishtpriyadarshi867@gmail.com']
rolls = ['180101003','180101015','180101048','180101052','180101053','180101054','180101055','180101056','180101057','180101058','180101065','180101072','180101076','180101079','180101081','180101084','180102005','180102010','180102014','180102020','180102022','180102022','180102039','180102042','180102051','180102053','180102064','180102074','180103002','180103020','180103041','180103047','180103051','180103051','180103051','180103052','180103052','180103052','180103059','180103070','180103073','180103081','180103087','180103089','180103092','180104001','180104002','180104010','180104015','180104019','180104022','180104037','180104042','180104044','180104056','180104057','180104063','180104079','180104086','180104087','180106001','180106036','180106043','180106050','180106052','180107026','180107036','180107057','180108001','180108002','180108003','180108004','180108017','180108020','180108024','180108030','180108036','180121001','180121016','180121040','180121042','180121043','180122015','180122020','180122025','180122027','180122029','180122048','180123029','180123031','180123033','180123037','180123040','180123041','180123045','180123051','180123053']

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

dict_id = dict(zip(gmails,folder_id_list))

for gmail,folder_id in dict_id.items():
	batch = drive_service.new_batch_http_request(callback=callback)
	user_permission = {
	    'type': 'user',
	    'role': 'writer',
	    'emailAddress': gmail
	}
	batch.add(drive_service.permissions().create(
	        fileId=folder_id,
	        body=user_permission,
	        fields='id',
	))

	batch.execute()

for gmail,folder_id in dict_id.items():
	batch = drive_service.new_batch_http_request(callback=callback)
	user_permission = {
	    'type': 'user',
	    'role': 'writer',
	    'emailAddress': "bsuhas116@gmail.com"
	}
	batch.add(drive_service.permissions().create(
	        fileId=folder_id,
	        body=user_permission,
	        fields='id',
	))

	batch.execute()
