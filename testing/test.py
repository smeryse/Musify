# import sqlite3
#
# def check_audio_in_db(user_id, audio_id, audio_youtube_url):
#     with sqlite3.connect("database.db") as conn:
#         cursor = conn.cursor()
#         cursor.execute("SELECT audio_id FROM user_audio_data WHERE chat_id = ? AND (audio_id = ? OR url = ?)",
#                        (user_id, audio_id, audio_youtube_url))
#         result = cursor.fetchone()
#         if result is None:
#             return False
#         else:
#             return audio_id
#
#
# def save_audio_to_db(user_id, audio_id, audio_youtube_url):
#     exists = check_audio_in_db(user_id, audio_id, audio_youtube_url)
#     if not exists:
#         with sqlite3.connect("database.db") as conn:
#             cursor = conn.cursor()
#             cursor.execute("INSERT INTO user_audio_data (chat_id, audio_id, url) VALUES (?, ?, ?)",
#                            (user_id, audio_id, audio_youtube_url))
#             conn.commit()
#         return False
#     else:
#         return audio_id
#
#
# # создаем подключение к базе данных
# conn = sqlite3.connect('database.db')
#
# # создаем курсор для выполнения запросов
# cursor = conn.cursor()
#
# # создаем таблицу user_audio_data, если ее нет
# cursor.execute('''CREATE TABLE IF NOT EXISTS user_audio_data (
#                     chat_id VARCHAR(13),
#                     audio_id VARCHAR(71),
#                     video_id VARCHAR(11)
#                 )''')
#
# # сохраняем изменения и закрываем соединение
# conn.commit()
# conn.close()
import os

from pytube import YouTube
from time import time
import threading


def download_audio(video_id):
    # Создайте объект YouTube, используя ссылку на видео.
    url = f'https://www.youtube.com/watch?v={video_id}'
    video = YouTube(url)

    # Выберите наилучший доступный аудиопоток
    audio = video.streams.filter(only_audio=True).order_by('bitrate').last()

    # Скачайте аудиопоток и сохраните его в файл
    file_path = audio.download()
    file_name = video.title

    return file_name


def download_audio_1(video_id):
    # Создайте объект YouTube, используя ссылку на видео.
    url = f'https://www.youtube.com/watch?v={video_id}'
    video = YouTube(url)

    # Получите список доступных аудиопотоков
    audio_streams = video.streams.filter(only_audio=True).order_by('bitrate')

    # Создайте список потоков для загрузки каждого аудиопотока
    threads = []
    for audio in audio_streams:
        t = threading.Thread(target=audio.download)
        threads.append(t)

    # Запустите все потоки
    for thread in threads:
        thread.start()

    # Дождитесь завершения всех потоков
    for thread in threads:
        thread.join()


from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from pytube import YouTube
from moviepy import VideoFileClip

def download_audio(video_id):
    # Создайте объект YouTube, используя ссылку на видео.
    url = f'https://www.youtube.com/watch?v={video_id}'
    youtube = build('youtube', 'v3', credentials=Credentials.from_authorized_user_info(info=None))
    video = youtube.videos().list(part='snippet', id=video_id).execute()

    # Получите список доступных аудиопотоков
    request = youtube.videos().list(part="id,contentDetails", id=video_id)
    response = request.execute()
    audio_streams = []
    for item in response['items']:
        content_details = item['contentDetails']
        audio_streams = content_details['audioStreams']

    # Выберите наилучший доступный аудиопоток
    audio = max(audio_streams, key=lambda stream: stream['bitrate'])

    # Скачайте аудиопоток и сохраните его в файл
    filename = f"{video['items'][0]['snippet']['title']}.mp4"
    yt = YouTube(url)
    yt.streams.get_by_itag(audio['itag']).download(filename=filename)

    # Конвертируйте файл в формат mp3
    mp3_filename = f"{video['items'][0]['snippet']['title']}.mp3"
    video_clip = VideoFileClip(filename)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(mp3_filename)

    # Удалите исходный файл
    os.remove(filename)

    return mp3_filename


def test_download_by_video_id():
    time_start = time()
    video_id = "XlAul6spLkA"
    file_name = download_audio_1(video_id)
    print(f"File saved as {file_name}")
    time_end = time()
    print(time_end - time_start)


test_download_by_video_id()
