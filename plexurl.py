#!/usr/bin/python3

import sys

# Load user defined config
NGROK_URL = "https://" + sys.argv[1] + ":443"
PLEX_USER = sys.argv[2]
PLEX_PWORD = sys.argv[3]
PLEX_SERVER = sys.argv[4]

from plexapi.myplex import MyPlexAccount
account = MyPlexAccount(PLEX_USER, PLEX_PWORD)
plex = account.resource(PLEX_SERVER).connect()  # returns a PlexServer instance

print(plex.settings.customConnections)
#NGROK_URL = 'http://4743a8af.ngrok.io:80'
customUrl = plex.settings.get('customConnections')
customUrl.set(NGROK_URL)
plex.settings.save()

from plexapi.myplex import MyPlexAccount
account = MyPlexAccount(PLEX_USER, PLEX_PWORD)
plex = account.resource(PLEX_SERVER).connect()  # returns a PlexServer instance

print(plex.settings.customConnections)
