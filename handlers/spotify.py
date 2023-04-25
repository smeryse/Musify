import asyncio
import os
from io import BytesIO

import spotipy
from aiogram import Router
from aiogram import types
from aiogram.filters import Command, Text
from aiogram.types import InputFile, Message, CallbackQuery
from pytube import YouTube

from create_bot import bot
from functions.database_func import is_audio_exists_in_db, add_data_to_db
from functions.youtube_func import find_on_youtube, create_url, download_audio_from_youtube


# All handlers should be attached to the Router (or Dispatcher)
router = Router()

@router.message(Command(commands=["spotify_search"]))
async def spotify_search(message: types.Message, type='track'):
    results = spotipy.search(q='artist:' + message.text, type=type)

