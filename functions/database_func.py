import sqlite3


def is_audio_exists_in_db(video_id: str) -> str:
    """
    Проверяет, существует ли аудио-запись для заданного идентификатора видео в базе данных.

    Args:
        video_id (str): Идентификатор видео.

    Returns:
        str: Идентификатор аудио-записи, если она существует в базе данных, или пустую строку, если ее нет.
    """

    with sqlite3.connect("../database.db") as db:
        cursor = db.execute("SELECT audio_id FROM main.user_audio_data WHERE video_id = ?", (video_id,))
        audio_id = cursor.fetchone()
        if audio_id:
            return audio_id[0]
        else:
            return ''


def add_data_to_db(chat_id: str, video_id: str, audio_id: str) -> None:
    """
    Добавляет запись с заданным идентификатором пользователя, видео и аудио в базу данных.

    Args:
        chat_id (str): Идентификатор пользователя.
        video_id (str): Идентификатор видео.
        audio_id (str): Идентификатор аудио-записи.
    """

    with sqlite3.connect("../database.db") as db:
        db.execute("INSERT INTO main.user_audio_data (chat_id, video_id, audio_id) VALUES (?, ?, ?)",
                   (chat_id, video_id, audio_id))
        db.commit()
