from aiogram.filters import Command
from aiogram import Router, types 

from aiogram import F 
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.keyboards import keyboard

callback_router = Router()


@callback_router.callback_query(lambda c: c.data.startswith("view_gallery"))
async def view_gallery(callback_query: types.CallbackQuery):
    await callback_query.message.answer("How do you want to filter the arts?", reply_markup=keyboard.art_filtering_keyboard)

@callback_router.callback_query(lambda c: c.data.startswith("add_art"))
async def view_gallery(callback_query: types.CallbackQuery):
    await callback_query.message.answer("alright are you ready?:", reply_markup=keyboard.create_art_keyboard)




