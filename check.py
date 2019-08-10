import requests
import os
import json
#from bs4 import BeautifulSoup as bs

live = 0

def changelive(l):
	global live
	live = l

config_file = open('/usr/CommentsLogByMySQL/config.json', encoding = "utf-8")
config = json.loads(config_file.read())['check']

headers = {}

headers['Accept'] = config['headers']['Accept']
headers['Origin'] = config['headers']['Origin']
headers['Referer'] = config['headers']['Referer']
headers['User-Agent'] = config['headers']['User-Agent']

#headers['Accept'] = 'application/json, text/plain, */*'
#headers['Origin'] = 'https://space.bilibili.com'
#headers['Referer'] = 'https://space.bilibili.com/349991143'
#headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'

#req = requests.get("https://api.live.bilibili.com/room/v1/Room/getRoomInfoOld?mid=349991143")
req = requests.get(config['url'])
result = req.json()['data']['liveStatus']
if result == 1:
	print("正在直播")
	#os.system("sudo ./auto_get.sh start")
	changelive(1)	
else:
	print("直播停止")
	if live == 1:
		#os.system("sudo ./auto_get.sh stop")
		changelive(0)
	else:
		pass
		#print("cccc")
