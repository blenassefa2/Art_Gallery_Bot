from aiogram.filters import Command
from aiogram import Router, types, F 
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ContentType
from aiogram.filters import Command

from ..keyboards import keyboard
from utils.state import Form

registration_router = Router()

@registration_router.message(Command('Register'))
async def start_handler(message: Message, state: FSMContext):
    try:
        await state.set_state(Form.role)
        await message.answer("Hello Welcome to  our bot what do you want?")
    except:
        await message.answer("Some error occurred")

@registration_router.message(Form.role)
async def form_role(message: Message, state:FSMContext):
    try:
        await state.update_data(role=message.text)
        await state.set_state(Form.phone_number)
        await message.answer("Let's register your phone number")
    except:
        await message.answer("Some error occurred")

@registration_router.message(Form.phone_number)
async def form_phone(message: Message, state:FSMContext):
    try:
        
        await state.update_data(phone_number = message.text)
        await state.set_state(Form.name)
        await message.answer("Let's register your name")
    except:
        await message.answer("Some error occurred")

@registration_router.message(Form.name)
async def form_photo(message: Message, state:FSMContext):
    try:
        await state.update_data(name = message.text)
        await state.set_state(Form.photo)
        await message.answer("Let's register your profile picture")
    except:
        await message.answer("Some error occurred")

@registration_router.message(Form.photo, F.photo)
async def form_name(message: Message, state:FSMContext):
    try:
        photo_id = message.photo[-1].file_id
        data = await state.get_data()
        await state.clear()

        formatted_text = []
        [
            formatted_text.append(f"{key}: {value}")
            for key, value in data.items()
        ]

        await message.answer_photo(
            photo_id, "\n".join(formatted_text)
        )
    except:
        await message.answer("Some error occurred")