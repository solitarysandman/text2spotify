import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = sp.search(q='wish you were here', limit=1)
for idx, track in enumerate(results['tracks']['items']):
    # print(idx, track['name'], track.keys())
    # print(track)
    print(track['name'], track['artists'][0]['name'], track['uri'], sep="|")
    sys.exit()
