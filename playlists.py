import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

# auth
auth = SpotifyOAuth(client_id=os.getenv('SPOTIPY_CLIENT_ID'),
                    client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
                    redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
                    scope="playlist-modify-public")

sp = spotipy.Spotify(auth_manager=auth)

# search
artist_name = input("Enter artist name: ")
artists = []
results = sp.search(q='artist:' + artist_name, type='artist', limit=50)
artists.extend(results['artists']['items'])

# pagination to get all results
while results['artists']['next']:
    results = sp.next(results['artists'])
    artists.extend(results['items'])

# show list of found artists
if not artists:
    print("No artists found with that name.")
    exit()

print(f"\nFound {len(artists)} artists:")
for i, artist in enumerate(artists, 1):
    print(f"{i}. {artist['name']}")

# select artist
while True:
    try:
        selection = int(input(f"\nSelect artist number (1-{len(artists)}): "))
        if 1 <= selection <= len(artists):
            artist_id = artists[selection-1]['id']
            artist_name = artists[selection-1]['name']
            break
        else:
            print("Please select a valid number.")
    except ValueError:
        print("Please enter a valid number.")

# get albums
albums = sp.artist_albums(artist_id, album_type='album', limit=50)
albums = albums['items']

# sort albums
albums.sort(key=lambda album: album['release_date'])

# create playlist
playlist_name = f"{artist_name} discography"
user_id = sp.current_user()['id']
playlist = sp.user_playlist_create(user=user_id, name=playlist_name)

# add album tracks
track_uris = []
for album in albums:
    album_name = album['name']
    album_uri = album['uri']
    print(f"Album: {album_name}")
    tracks = sp.album_tracks(album_uri)
    for track in tracks['items']:
        track_uris.append(track['uri'])

# divide tracks in batches of 100
batch_size = 100
for i in range(0, len(track_uris), batch_size):
    batch = track_uris[i:i + batch_size]
    sp.playlist_add_items(playlist_id=playlist['id'], items=batch)

print(f"'{playlist_name}' playlist created successfully!")
