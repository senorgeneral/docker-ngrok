#!/usr/bin/python3

import sys
import json
import requests
import time

# need time for ngrok to start up before requesting data
time.sleep(15)

# acquires the Ngrok https url
def get_ngrok_url():
    url = "http://localhost:4040/api/tunnels"
    res = requests.get(url)
    res_unicode = res.content.decode("utf-8")
    res_json = json.loads(res_unicode)
    for i in res_json["tunnels"]:
       if i['proto'] == 'https':
          return i['public_url']
          break

# Load user defined config"
NGROK_URL = get_ngrok_url()
PLEX_USER = sys.argv[1]
PLEX_PWORD = sys.argv[2]
PLEX_SERVER = sys.argv[3]

# stores plex user login info into a variable
from plexapi.myplex import MyPlexAccount
account = MyPlexAccount(PLEX_USER, PLEX_PWORD)
plex = account.resource(PLEX_SERVER).connect()  # returns a PlexServer instance

# displays current plex custom url settings. Not needed but nice to see
print(plex.settings.customConnections)

# sets plex's "Custom server access URLs" with one from Ngrok  
customUrl = plex.settings.get('customConnections')
customUrl.set(NGROK_URL)
plex.settings.save()

# displays new custom plex url from Ngrok. Not needed but nice to see
from plexapi.myplex import MyPlexAccount
account = MyPlexAccount(PLEX_USER, PLEX_PWORD)
plex = account.resource(PLEX_SERVER).connect()  # returns a PlexServer instance
print(plex.settings.customConnections)

