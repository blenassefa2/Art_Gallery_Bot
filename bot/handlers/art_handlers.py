from aiogram.filters import Command
from aiogram import Router, types, F 
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ContentType
from aiogram.filters import Command
from aiogram_widgets.pagination import KeyboardPaginator

from ..keyboards import keyboard
from utils.state import Art

art_router = Router()

@art_router.message(F.text == "🎨 View Gallery")
async def process_callback_respond_to_action1(message: Message):
   await message.answer("How do you want to filter the arts?", reply_markup=keyboard.art_filtering_keyboard)

@art_router.message(F.text == "🖌 Let's gooo!!")
async def start_user_register(message: Message, state:FSMContext):
    try:
        current_user_name = message.from_user.username
        await state.update_data(creator = current_user_name)
        await state.set_state(Art.tag)
        await message.answer("What is the tag for your art?")
    except:
        await message.answer("Some error occurred")


@art_router.message(Art.tag)
async def Art_photo(message: Message, state:FSMContext):
    try:
        await state.update_data(tag ='#'+message.text)
        await state.set_state(Art.image)
        await message.answer("Let's register your art")
    except:
        await message.answer("Some error occurred")

@art_router.message(Art.image, F.photo)
async def final_state(message: Message, state:FSMContext):
    try:
        photo_id = message.photo[-1].file_id
        data = await state.get_data()
        await state.clear()

        Artatted_text = []
        [
            Artatted_text.append(f"{key}: {value}")
            for key, value in data.items()
        ]
        
        await message.answer_photo(
            photo_id, "\n".join(Artatted_text), reply_markup=KeyboardPaginator(
                data=keyboard.add_or_view_art_buttons,
                router=art_router,
                per_page=20,
                per_row=1,
                
                ).as_markup()
        )
    
    except:
        await message.answer("Some error occurred")

