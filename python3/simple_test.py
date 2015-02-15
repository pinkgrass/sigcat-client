#

import json
import requests
from uuid import uuid4

_LOCAL = False

if _LOCAL:
    _URL_BASE = 'http://localhost:8080/'
else:
    _URL_BASE = 'http://sigcatv1-datp.rhcloud.com/'

apikey = str(uuid4())

url = _URL_BASE + 'signaller'
payload = {'key': apikey, 'email': 'emma@pinkgrass.org'}
headers = {'content-type': 'application/json'}
print(url)
r = requests.post(url, data=json.dumps(payload), headers=headers)
print(json.dumps(payload))
print(r.json())


url = _URL_BASE + 'signal'
payload = {'key': apikey, 'type': 'buy', 'base': 'USD+rMwjYedjc7qqtKYVLiAccJSmCwih4LnE2q', 'counter': 'BTC+rMwjYedjc7qqtKYVLiAccJSmCwih4LnE2q'}
headers = {'content-type': 'application/json'}
print(url)
r = requests.post(url, data=json.dumps(payload), headers=headers)
print(json.dumps(payload))
print(r.json())

