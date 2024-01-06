from aiogram.filters import Command
from aiogram import Router, types, F 
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ContentType
from aiogram.filters import Command
from aiogram_widgets.pagination import KeyboardPaginator

from ..keyboards import keyboard
from utils.state import User

user_router = Router()

@user_router.message(F.text == "👋 Register!")
async def start_user_register(message: Message, state:FSMContext):
    try:
        current_user_name = message.from_user.username
        await state.update_data(user_name = current_user_name)
        await state.set_state(User.name)
        await message.answer("Hello Welcome to our bot; What do you want to be known as?")
    except:
        await message.answer("Some error occurred")


@user_router.message(User.name)
async def User_photo(message: Message, state:FSMContext):
    try:
        await state.update_data(name = message.text)
        await state.set_state(User.photo)
        await message.answer("Let's register your profile picture")
    except:
        await message.answer("Some error occurred")

@user_router.message(User.photo, F.photo)
async def final_state(message: Message, state:FSMContext):
    try:
        photo_id = message.photo[-1].file_id
        data = await state.get_data()
        await state.clear()

        Useratted_text = []
        [
            Useratted_text.append(f"{key}: {value}")
            for key, value in data.items()
        ]

        await message.answer_photo(
            photo_id, "\n".join(Useratted_text), reply_markup=KeyboardPaginator(
                data=keyboard.add_or_view_art_buttons,
                router=user_router,
                per_page=20,
                per_row=1,
                
                ).as_markup()
        )
    
    except:
        await message.answer("Some error occurred")