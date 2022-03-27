#!/bin/python3

import urllib3
import requests
import base64
import time

iteration = 0
suffix = "MAT/22/000"
#you can change headers according to your requirements
headers = {'User-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:98.0) Gecko/20100101 Firefox/98.0','Accept':'application/json, text/javascript, */*; q=0.01','Referer': 'https://www.dcode.fr/code-barres','Accept-Language':'en-US,en;q=0.5','X-Requested-With':'XMLHttpRequest','Cookie':'PHPSESSID=055871c9ea57c69895ee45a414685683; session_id=a8a91769-c05a-4ca9-84ba-bd4e1bc84158; _ga=GA1.2.96898235.1647857579; __qca=P0-1414041781-1647857580823; __r=1.e4fcbce0ed724c6bbffd31d37b54a816'}

for i in range(1,100):
	iteration = i
	#r = http.request('GET','https://dcode.fr/code-barres', verify=False)
	r = requests.get('https://dcode.fr/code-barres',headers= headers)
	if i ==10:
		suffix = "MAT/22/000"
	elif i == 100:
		suffix = "MAT/22/00"
	elif i == 1000:
		suffix = "MAT/22/0"
	plaintext = suffix + str(iteration)
	
	fields = {'tool' : 'code-barres','plaintext' : plaintext,'type' : 'code93','bottom' : 'value','top' : 'custom','bottom_text' : ' DC0D3B4RR3','top_text' : 'UICF Property'}
	r = requests.post('https://www.dcode.fr/api/', headers= headers, data = fields)
	chaine = r.content.decode('utf-8')
	str_replacee = chaine.replace('\\','')
	str_nodiv = str_replacee.rsplit("/></div><div>")[0] 
	imagebase64 = str_nodiv.split('{"results":"<div style="overflow-y: auto;"><img src="data:image/png;base64,')
	image = imagebase64[1].strip('"')
	base64_img_bytes = image.encode('utf-8')
	fichier = "fichier" + str(iteration)
	with open(fichier,'wb') as file_to_save:
		decoded_image_data = base64.decodebytes(base64_img_bytes)
		file_to_save.write(decoded_image_data)
	time.sleep(10)
print("done")
print("By Amstaff")


