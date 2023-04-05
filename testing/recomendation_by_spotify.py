import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from Musify.config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET


def get_recommendations(track_name):
    # Авторизуемся в Spotify API
    client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID,
                                                          client_secret=SPOTIFY_CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Ищем трек по названию
    results = sp.search(q=track_name, type='track', limit=1)

    # Получаем рекомендации на основе найденного трека
    if results['tracks']['items']:
        track_id = results['tracks']['items'][0]['id']
        recommendations = sp.recommendations(seed_tracks=[track_id], limit=10)
        tracks = []
        for track in recommendations['tracks']:
            artists = [artist['name'] for artist in track['artists']]
            track_info = {'name': track['name'], 'artists': artists}
            tracks.append(track_info)
        return tracks
    else:
        return None


def format_track_info(track_info):
    title = track_info['name']
    artists = ', '.join(track_info['artists'])
    return f"{title} - {artists}"


tracks_names = get_recommendations('Komarovo (DVRST Phonk Remix)')

for track_name in tracks_names:
    print(format_track_info(track_name))
