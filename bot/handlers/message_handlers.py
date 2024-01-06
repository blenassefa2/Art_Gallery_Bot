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



@message_router.message(F.text == "🎨 View Gallery")
async def process_callback_respond_to_action1(message: types.message):
    await message.answer(f"you picked View Gallery")
