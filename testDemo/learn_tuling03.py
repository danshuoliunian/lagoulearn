# coding:utf-8
import itchat as itchat
import requests


def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'Key': 'fcf9d34ab2544d21b79c01a38bde2111',
        'info': msg,  # 这是要发出的信息
        'useId': 'test'
    }
    try:
        r = request.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return


# 通过定义装饰器加强函数 tuling_reply(msg) 功能，获取注册文本信息
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'I received:' + msg['Text']
    reply = get_response(msg['Text'])
    return reply or defaultReply


# 使用热启动，不需要多次扫码
itchat.auto_login(hotReload=True)
itchat.run()
