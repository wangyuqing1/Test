import json
import requests

def sendmessage(message):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=ae03cc317ed7391e2f655cb7b27f84c1f2c7b1c96aaebfb52a71cf41532d6055'
    headers = {
        "Content-Type": "application/json ;charset=utf-8 "
    }
    message = message
    String_textMsg = {
        'msgtype':'text',
        'text':{"content":message},
        "at":{
            'atMobiles':[
                '15237774366'
            ],
            'isAtAll':False
        }
    }
    string_textmsg = json.dumps(String_textMsg)
    res = requests.post(url,data=string_textmsg,headers=headers)