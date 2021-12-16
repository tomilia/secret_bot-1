import requests
DISCORD_BASE_URI = 'https://discord.com/api/v8'
channel = '793929630234312735'
#client_id = 919973698927206401
#client_secret = 'sF6w79mw6RMtXHkGWmx1zMI5EMgqQkyQ'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Authorization': 'ODI0NTc2OTMxMjEwNDYxMTk1.Ybry-w.eGbYIYa1HjU1GfuFkjTMX2x_Dcw'
}
r = requests.get(f'%s/channels/{channel}/messages' % DISCORD_BASE_URI, headers=headers)
r.raise_for_status()

print(r.json()[0])