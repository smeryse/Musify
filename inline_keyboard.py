from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

my_music = InlineKeyboardButton('Моя музыка', callback_data='my_music')
find_on_name = InlineKeyboardButton('Найти', callback_data='find_on_name')
download_by_url = InlineKeyboardButton('Скачать', callback_data='download_by_url')

main_menu = InlineKeyboardMarkup().add(my_music, find_on_name, download_by_url)
