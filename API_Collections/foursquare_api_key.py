import json, requests
url = 'https://api.foursquare.com/v1/venues/explore'

params = dict(
    client_id='4YUTC2USRBOIDLC4XGN45LQ1IOB3PMPSFYLOYUAG3QEB0T1V',
    client_secret='BZQA1EULBADIJEBSAZSNBNQ2UNZYMLUGWDWBXEHGXGBWRIKA',
    v='20170801',
    ll='37.392971, -122.076044',
    query='pizza',
    limit=1
)
resp = requests.get(url=url, params=params)
data = json.loads(resp.text)
