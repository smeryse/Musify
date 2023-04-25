from typing import List

from pytube import Search, YouTube

from pytube import Playlist


def search_playlists(query):
    """
    Функция для поиска плейлистов на YouTube.

    Аргументы:
        query (str): Поисковый запрос для поиска плейлистов.

    Возвращает:
        Список объектов pytube.Playlist, соответствующих результатам поиска.
    """
    search_results = Playlist.search(query)
    return search_results


def download_audio_from_youtube(video_id):
    # создаем объект YouTube с заданным video_id
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    yt = YouTube(video_url)

    # получаем первый поток, содержащий только аудио
    audio_stream = yt.streams.filter(only_audio=True).first()

    # скачиваем аудио
    audio_path = audio_stream.download(output_path="..")

    return audio_path


def create_url(video_id: str) -> str:
    return f'https://www.youtube.com/watch?v={video_id}'
