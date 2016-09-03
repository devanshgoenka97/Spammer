#!/usr/bin/python
#Google Form Spammer
#https://docs.google.com/forms/d/e/1FAIpQLScENJsiop7yKEnS3-Wv2dFA7xxXOp1YA46922L9-ORSxBRCNQ/formResponse
import requests

try :
 i=0
 url = "https://docs.google.com/forms/d/e/1FAIpQLScp8GLVOGeJM2Lq1iYjUO-2gD0PxCtE-t8zQ7JuTmDVcPeaSg/formResponse"
 user_agent = {
	'Referer'   : 'https://docs.google.com/forms/d/e/1FAIpQLScp8GLVOGeJM2Lq1iYjUO-2gD0PxCtE-t8zQ7JuTmDVcPeaSg/viewform?c=0&w=1',
	'User-Agent' : 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36'}
 while 1:
	 spam_data = {"entry.2056656144"  : "HEY HEY"}
	 r=requests.post(url,data=spam_data,headers=user_agent)
	 i=i+1
	 if(i%3==0):
	 	print(r)
	 	print('\nTotal Count = ')
	 	print(i)
	 	print('\n')
except KeyboardInterrupt:
	print('Goodbye!\n')