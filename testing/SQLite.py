import sqlite3

conn = sqlite3.connect('../../database.db')
c = conn.cursor()

# is_in_database = f'''SELECT audio_youtube_url FROM users_audio_data
# WHERE user_id = {message.chat.id} AND
#       audio_youtube_url = {video_url}
# '''
#
# insert =  f'''INSERT INTO users_audio_data (user_id, audio_id, audio_youtube_url)
# VALUES ({message.chat.id}, {audio_id}, {video_url})
# '''}


result_bool = c.execute('''create table user_audio_data
(
    user_id           INTEGER(10),
    audio_youtube_url VARCHAR(41),
    audio_id          VARCHAR(71)
);
''')
print(result_bool)
conn.commit()
conn.close()
