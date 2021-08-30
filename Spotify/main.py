from spotipy import Spotify, SpotifyException
from spotipy.oauth2 import SpotifyOAuth
import json

client_id = CLIENT_ID
client_secret = SECRET_KEY
redirect_uri = "http://example.com"
scope = "playlist-modify-private"
user = USER
playlist_id = "https://open.spotify.com/playlist/7KYVgAfpuh4q9B7GWGWJlS?si=99f6154bedbf4fc8"

sp = Spotify(
    auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        scope=scope,
        redirect_uri=redirect_uri
    )
)


def create_playlist(name, description):
    sp.user_playlist_create(
        user=user,
        name=name,
        public=False,
        collaborative=False,
        description=description
    )


def write_to_file(text):
    with open("data.json", "w") as f:
        json.dump(text, f, indent=4)


def add_song(items):
    try:
        sp.playlist_add_items(
            playlist_id=playlist_id,
            items=items,
            position=None
        )
        return 1
    except SpotifyException:
        return 0






