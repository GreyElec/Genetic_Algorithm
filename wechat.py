import json
import requests
from wxpy import *

def auto_reply(text):
	url = "http://www.tuling123.com/openapi/api"
	api_key = "bdca88555c6e4ac981323e658c68efcd"
	payload = {"key":api_key,"info":text,"userid":"123456"}
	r = requests.post(url,data=json.dumps(payload))
	result = json.loads(r.content)
	return result["text"]

bot = Bot()

@bot.register()
def forward_message(msg):
	return "[Robot reply：]"+auto_reply(msg.text)

embed()