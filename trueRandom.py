import json, requests

def randomOrgRPC():
    json_request_data = {
        "jsonrpc": "2.0",
        "method": "generateIntegers",
        "params": {
            "apiKey": "dontknowhahaha",
            "n": 21,
            "min": 1,
            "max": 7,
            "replacement": True
        },
        'id':1
    }
    headers = {'Content-type': 'application/json', 'Content-Length': '200', 'Accept': 'application/json'}
    data = json.dumps(json_request_data)
    response = requests.post(
        url = 'https://api.random.org/json-rpc/2/invoke',
        data = data,
        headers = headers
        )
    return response.json()['result']['random']['data']
