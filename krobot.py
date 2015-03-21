from websocket import create_connection
import urllib2
import json


# define var
with open("token.txt") as f:
    token = f.read().strip()  # enter token here
url = "https://slack.com/api/rtm.start?token=%s" % token


resp = urllib2.urlopen(url).read()
login_data = json.loads(resp)

ws_status = login_data["ok"]  # must be True
ws_url = login_data["url"]

ws = create_connection(ws_url)

if ws:
    while True:
        print ws.recv()
