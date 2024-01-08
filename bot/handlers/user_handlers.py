from aiogram.filters import Command
from aiogram import Router, types, F 
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ContentType
from aiogram.filters import Command
from aiogram_widgets.pagination import KeyboardPaginator

from database.services.user_services import create_user, get_user_by_username

from ..keyboards import keyboard
from utils.state import User

user_router = Router()

@user_router.message(F.text == "👋 Register!")
async def start_user_register(message: Message, state:FSMContext):
    try:
        
        current_user_name = message.from_user.username

        # Check if user is previously registered
        registered_user = await get_user_by_username(current_user_name)

        if registered_user:
            x = registered_user.model_dump()
            Useratted_text = ["🙌Welcome Back to our bot!!!🙌"]
            for key, value in x.items():
                if key != 'photo':
                    Useratted_text.append(f"{key}: {value}")
                
            
            await message.answer_photo(
                registered_user.photo, "\n".join(Useratted_text), reply_markup=keyboard.add_or_view_art_buttons,
                    
            )
        else:
            await state.update_data(user_name = current_user_name)
            await state.set_state(User.name)
            await message.answer("Hello Welcome to our bot; What do you want to be known as?")

    except Exception as e:
        await message.answer(f"Some error occurred {e}")


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
        await state.update_data(photo = photo_id)
        data = await state.get_data()
        await state.clear()
       
        await create_user(**data)
        
        
        Useratted_text = ["Successfully Registered ✔"]
        for key, value in data.items():
            if key != 'photo':
                Useratted_text.append(f"{key}: {value}")
            
        
        await message.answer_photo(
            photo_id, "\n".join(Useratted_text), reply_markup=keyboard.add_or_view_art_buttons,
                
        )
    
    except Exception as e:
        await message.answer(f"Some error occurred {e}")