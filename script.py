#!/usr/bin/python
#Google Form Spammer
#https://docs.google.com/forms/d/e/1FAIpQLScENJsiop7yKEnS3-Wv2dFA7xxXOp1YA46922L9-ORSxBRCNQ/formResponse
import requests

i=0
url = "https://docs.google.com/forms/d/e/1FAIpQLScENJsiop7yKEnS3-Wv2dFA7xxXOp1YA46922L9-ORSxBRCNQ/formResponse"
user_agent = {
	"Referer"    : "https://docs.google.com/forms/d/e/1FAIpQLScENJsiop7yKEnS3-Wv2dFA7xxXOp1YA46922L9-ORSxBRCNQ/viewform"
	"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}
while 1:
	spam_data = {"entry.410813173"  : "Yes",
	             "entry.1269816401" : "10",
	             "entry.1963899682" : "560",
	             "entry.1616294512" : "10"}
     r=requests.post(url,data=spam_data,headers=user_agent)
     i=i+1
     if(i%10==0):
     	print(r)
     	print('\nTotal Count = ')
     	print(i)
     	print('\n')