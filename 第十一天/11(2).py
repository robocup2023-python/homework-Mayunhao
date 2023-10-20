import requests
import json

url = "http://api.interpreter.caiyunai.com/v1/translator"
token = "5jjt1881hlnmboeyhftt"

payload = {
    # "source" : ["Where there is a will, there is a way.",
    # "ColorfulClouds Weather is the best weather service."],
    "source":"ガチョウを落とす魚を沈め、恥ずかしがり屋の花が月を閉じた",
    #、あなたは本当に美しく感動的です",
    #"ガチョウを落とす魚を沈め、恥ずかしがり屋の花が月を閉じた",
    "trans_type": "ja2zh",
    "request_id": "demo",
}

headers = {
    'content-type': "application/txt",
    'x-authorization': "token " + token,
}

response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

# print(response.text)
resp = json.loads(response.text)['target']

print(resp)
