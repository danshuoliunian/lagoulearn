# coding：utf-8

import json

import urllib.request

api_url = "http://openapi.tuling123.com/openapi/api/v2"
text_input = input('我:')

req = {
    "perception":
        {
            "inputText":
                {
                    "text": text_input
                },
            "selfInfo":
                {
                    "location":
                        {
                            "city": "上海",
                            "province": "上海",
                            "street": "文汇路"
                        }
                }
        },
    "userInfo":
        {
            "apiKey": "fcf9d34ab2544d21b79c01a38bde2111",
            "userId": "d3bf2"
        }

}
# print(req)
# 将字典格式的req编码为utf8
req = json.dumps(req).encode('utf8')
# print(req)


http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
response = urllib.request.urlopen(http_post)
response_str = response.read().decode('utf8')

print(response_str)
response_dic = json.loads(response_str)
print(response_dic)

intent_code = response_dic['intent']['code']
result_text = response_dic['results'][0]['values']['text']
print('Tuling的回答')
print('code:' + str(intent_code))
print('text:' + result_text)
