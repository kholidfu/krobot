from websocket import create_connection
import urllib2
import json


# define var
with open("token.txt") as f:
    token = f.read().strip()  # enter token here
url = "https://slack.com/api/rtm.start?token=%s" % token

# authenticating
resp = urllib2.urlopen(url).read()
login_data = json.loads(resp)

auth_status = login_data["ok"]  # must be True
auth_url = login_data["url"]

ws = create_connection(auth_url)

if ws:  # connected
    while True:
        print ws.recv()
