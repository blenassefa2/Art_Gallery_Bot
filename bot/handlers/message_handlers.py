from aiogram.filters import Command
from aiogram import Router, types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder

from ..keyboards import keyboard

message_router = Router()

@message_router.message(Command('start'))
async def start_handler(message: types.Message):
    try:
        await message.answer("Hello Welcome to our art gallery", reply_markup=keyboard.first_reply_keyboard)
    except:
        await message.answer("Some error occurred")


@message_router.message(Command('help'))
async def help_handler(message: types.Message):
    try:
        await message.answer("This is a bot where you can show your arts and see other people's art", reply_markup=keyboard.first_reply_keyboard)
    except:
        await message.answer("Some error occurred")

