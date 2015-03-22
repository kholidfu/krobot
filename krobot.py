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


def get_users_info(uid):
    url = "https://slack.com/api/users.info?token=%s&user=%s" % (token, uid)
    resp = json.loads(urllib2.urlopen(url).read())
    return resp["user"]["name"]

if ws:  # connected
    while True:
        json_resp = json.loads(ws.recv())
        try:
            print "%s is currently: %s" % (get_users_info(json_resp["user"]), json_resp["type"])
        except:
            continue
        # print ws.recv()
