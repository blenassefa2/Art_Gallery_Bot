from aiogram import Router, F 
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from utils.pagination.image_paginator import ImagePaginator
from ..keyboards import keyboard
from utils.state import Art

from database.services.art_services import create_art, get_art_by_username
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
        
        await state.update_data(image = message.photo[-1].file_id)
        
        data = await state.get_data()
        inserted_art = await create_art(**data)
        await state.clear()

        if not inserted_art:
            await message.answer("Couldn't insert art")
        else:
            text_data = []
            
            current_user_arts = await get_art_by_username(message.from_user.username)
            
            for art in current_user_arts:
                text_data.append([art.image, [art.creator, art.tag]])

            paginator = ImagePaginator(
                data=text_data,
                router=art_router,
                pagination_buttons=["⏪", "⬅️", "➡️", "⏩"],
                per_page=1
            )

            current_message, reply_markup = paginator.current_message_data
            current_text_chunk, current_caption = current_message
            await message.answer_photo(
                current_text_chunk,
                caption=current_caption,
                reply_markup=reply_markup,
            )
        
    except Exception as e:
        
        await message.answer(f"Some error occurred {e}")

