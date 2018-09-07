import json


def parseUrlFunc():
    with open('url_data.json', encoding='utf-8') as f:
        data = f.read()
        jdata = json.loads(data)
        return jdata
