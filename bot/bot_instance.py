
from aiogram import Bot, types


# Use the commented code below if you store the token api in .env
import os
from dotenv import load_dotenv
load_dotenv()

# For hosting on pythonanywhere use the following commented code
# from aiogram.client.session.aiohttp import AiohttpSession
# bot = Bot(
#     token=TOKEN_API,
#     parse_mode='HTML',
#     session=AiohttpSession(proxy='http://proxy.server:3128')
# )

bot = Bot(
    token=os.environ['TOKEN_API'],
    parse_mode='HTML'
)