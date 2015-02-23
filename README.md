## Trade Signal Catcher API
Trade Signal Catcher (SigCat) is a digital asset trading platform using the Ripple Network. Clients connect to SigCat and submit Trade signals. The performance of all signals are tracked against market prices from the Ripple Network.

### Quick Start
#### Get a UUID (any UUID will do)
```terminal
curl -X GET http://sigcatv1-datp.rhcloud.com/uuid
```

#### Use your UUID and register it with an email address
```terminal
curl -X POST  -H "Accept: Application/json" -H "Content-Type: application/json" http://sigcatv1-datp.rhcloud.com/signaller -d '{"key": "8cb84c83-8327-42ca-a907-65e11b7e2dce", "email": "emma@pinkgrass.org"}'
```

#### Submit your first trade signal with your UUID
```terminal
curl -X POST  -H "Accept: Application/json" -H "Content-Type: application/json" http://sigcatv1-datp.rhcloud.com/signal -d '{"type": "buy", "counter": "BTC+rMwjYedjc7qqtKYVLiAccJSmCwih4LnE2q", "key": "3f96ac98-a77d-4c11-896c-811e5d5478d1", "base": "USD+rMwjYedjc7qqtKYVLiAccJSmCwih4LnE2q"}'
```

### Ripple Concepts
| field | type | description |
|---|---|---|
| currency	| String(ISO4217 currency code)	| Three digit currency code eg. USD |
| counterparty | String (Address) | A Ripple address eg. rMwjYedjc7qqtKYVLiAccJSmCwih4LnE2q |

rMwjYedjc7qqtKYVLiAccJSmCwih4LnE2q is SnapSwap Ripple address. 

### API Resources
Nothing pretty about this API. Expect major changes in V2.
  - [GET /uuid](#uuid)
  - [POST /signaller/](#post-signaller)
  - [POST /signal/](#post-signal)

### GET /uuid
Request a UUID. Optional. You can supply your own.

`GET http://sigcatv1-datp.rhcloud.com/uuid`

response:`{"uuid": "f327dfff-0d75-4792-b352-1e9fe9cead0a"}`

### POST /signaller/
Register a client with a UUID and email address

`POST http://sigcatv1-datp.rhcloud.com/signaller/`

| Field        | Type           | Description  |
| ------------- |-------------| -----|
| key      | string(UUID) | Client's UUID |
| email      | string | email address to register UUID to       |

Example Body:

    {
    'key': 'f327dfff-0d75-4792-b352-1e9fe9cead0a',
    'email': 'emma@pinkgrass.org'
    }

| Field        | Type           | Description  |
| ------------- |-------------| -----|
| success      | boolean | True if successfully registered |
| errors      | array | array of error messages       |

Example response:

    {'success': True,
    'errors': [],
    'data': {
        'email': 'emma@pinkgrass.org',
        'key': 'f327dfff-0d75-4792-b352-1e9fe9cead0a',
        'created': 1424691358.9287372
        }
    }

### POST /signal/
Submit a trade signal. Signal is validated against a JSON-Schema

`POST http://sigcatv1-datp.rhcloud.com/signaller/`

| Field        | Type           | Description  |
| ------------- |-------------| -----|
| key      | string | Client's UUID |
| type      | string | 'buy' or 'sell'       |
| base | string      | The base currency as currency+counterparty|
| counter | string      | The counter currency as currency+counterparty |

example body:

    `{
    'key': 'f327dfff-0d75-4792-b352-1e9fe9cead0a',
    'type': 'buy',
    'base': 'USD+rMwjYedjc7qqtKYVLiAccJSmCwih4LnE2q', 
    'counter': 'BTC+rMwjYedjc7qqtKYVLiAccJSmCwih4LnE2q'}`

| Field        | Type           | Description  |
| ------------- |-------------| -----|
| success      | boolean | True if successfully submitted |
| errors      | array | array of error messages       |

example response: 

    {'success': True,
    'errors': [],
    'data': {
        'ask': '0.00428265524625267666',
        'key': 'f327dfff-0d75-4792-b352-1e9fe9cead0a',
        'counter': 'BTC+rMwjYedjc7qqtKYVLiAccJSmCwih4LnE2q',
        'price': '0.00428265524625267666',
        'type': 'buy', 
        'bid': '0.004269722822681052', 
        'base': 'USD+rMwjYedjc7qqtKYVLiAccJSmCwih4LnE2q', 
        'created': 1424691359.2305076}}

### JSON-Schemas
The Signaller and Signal JSON are validated against the following JSON-Schemas:

#### SIGNALLER_SCHEMA
    {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "Trade Signaller",
    "description": "A trade signaller",
    'type': 'object',
    'properties': {
        'key':  {'type': 'string', 'pattern': '^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$', 'description': 'Your UUID for Signaller'},
        'email': { 'type': 'string', 'format': 'email', 'description': 'email address of trade signaller'}
    },
    'required': ['key', 'email']
}

#### SIGNAL_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "Trade Signal",
    "description": "A trade signal",
    "type": "object",
    'properties': {
        'key':  {'type': 'string', 'pattern': '^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$', 'description': 'Unique ID of Signaller'},
        'type': {'type' : 'string', 'enum': ['buy','sell'], 'description': 'Either buy or sell'},
        'base': {'type': 'string', 'pattern': '^[A-Z0-9]{3}\+r[rpshnaf39wBUDNEGHJKLM4PQRST7VWXYZ2bcdeCg65jkm8oFqi1tuvAxyz]{27,35}$', 'description': 'The base currency as currency+counterparty (e.g. USD+<rippleaddress>)'},
        'counter': {'type': 'string', 'pattern': '^[A-Z0-9]{3}\+r[rpshnaf39wBUDNEGHJKLM4PQRST7VWXYZ2bcdeCg65jkm8oFqi1tuvAxyz]{27,35}$', 'description': 'The counter currency as currency+counterparty (eg. BTC+<rippleaddress>)'}
    },
    'required': ['key', 'type', 'base', 'counter'],
    'additionalProperties': False
}

### Response Codes
Only three simple, common response codes are returned (1) success, (2) failure due to client-side problem, (3) failure due to server-side problem:
* 200 - OK
* 400 - Bad Request
* 500 - Internal Server Error
