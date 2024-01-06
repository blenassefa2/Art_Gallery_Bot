from aiogram.filters import Command
from aiogram import Router, types 

from aiogram import F 
from aiogram.utils.keyboard import InlineKeyboardBuilder


callback_router = Router()


@callback_router.callback_query(lambda c: c.data.startswith("view_gallery"))
async def view_gallery(callback_query: types.CallbackQuery):
    await callback_query.message.answer("🔃 loading 🔃")




