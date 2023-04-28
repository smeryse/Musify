import youtube_dl

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


def download_audio_youtube(url_or_id: str) -> str:
    """
    Функция загружает аудио с YouTube видео, используя модуль YoutubeDL.

    Параметры:
    url_or_id (str): URL или идентификатор видео YouTube для загрузки аудио.

    Возвращаемое значение:
    str: Путь к загруженному аудио файлу.

    Исключения:
    None
    """
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'musics/%(title)s.%(ext)s',
        'noplaylist': True,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url_or_id, download=False)
        audio_url = info_dict['url']
        audio_title = info_dict['title']
        ydl.download(([url_or_id]))
        file_path = f"musics/{audio_title}.webm"
        return file_path


def create_url(video_id: str) -> str:
    return f'https://www.youtube.com/watch?v={video_id}'


if __name__ == '__main__':
    download_audio_youtube('L-iepu3EtyE')
