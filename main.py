import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import requests
import base64


def main():
    # Set your Spotify API credentials
    load_dotenv()
    SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
    SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
    SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'  # You can change this to a different redirect URI

    # Initialize Spotify client
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                                client_secret=SPOTIPY_CLIENT_SECRET,
                                                redirect_uri=SPOTIPY_REDIRECT_URI,
                                                scope='playlist-modify-private'))

    # Get user's mood input
    user_mood = input("Enter your mood: ")

    # Create a new playlist
    playlist_name = f"{user_mood} Playlist"
    playlist = sp.user_playlist_create(sp.me()['id'], playlist_name, public=False)

    # Search for tracks based on the mood
    results = sp.search(q=user_mood, type='track', limit=10)  # You can adjust the limit as needed

    # Add tracks to the playlist
    track_uris = [track['uri'] for track in results['tracks']['items']]
    sp.playlist_add_items(playlist['id'], track_uris)

    print(f"Playlist '{playlist_name}' has been created with {len(track_uris)} tracks.")




if __name__ == '__main__':
    main()