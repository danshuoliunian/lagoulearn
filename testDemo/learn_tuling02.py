# coding:utf-8

import requests

"""
data = {
    "reqType":0,
    "perception": {
        "inputText": {
            "text": "附近的酒店"
        },
            
        
    },
    "userInfo": {
        "apiKey": "XXX",
        "userId": "1"
    }
    }
"""


def to_tuling():
    data = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": "附近的酒店"
            }
        },
        "userInfo": {
            "apiKey": "fcf9d34ab2544d21b79c01a38bde2111",
            "userId": "jdbhg3"
        }
    }
    res = requests.post("http://openapi.tuling123.com/openapi/api/v2", json=data)
    new_res = res.json().get("results")[0].get("valus").get("text")
    print(new_res)
