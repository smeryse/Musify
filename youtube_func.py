from typing import List

from pytube import Search, YouTube


def find_on_youtube(track_name: str, count: int = 1) -> List[str]:
    """
    Searches for videos on YouTube with the given track name and returns the video_ids.
    """
    results = Search(track_name + ' Official music video')
    video_ids = [video.video_id for video in results.results[:count]]
    if count == 1:
        return video_ids[0]
    else:
        return video_ids


def download_audio_from_youtube(video_id):
    # создаем объект YouTube с заданным video_id
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    yt = YouTube(video_url)

    # получаем первый поток, содержащий только аудио
    audio_stream = yt.streams.filter(only_audio=True).first()

    # скачиваем аудио
    audio_path = audio_stream.download(output_path=".")

    return audio_path


def create_url(video_id: str) -> str:
    return f'https://www.youtube.com/watch?v={video_id}'
