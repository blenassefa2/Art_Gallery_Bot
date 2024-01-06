
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton


first_reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👋 Register!")
        ],
        [
            KeyboardButton(text="🎨 View Gallery")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="dtrial",
    selective=True
)

add_or_view_art_buttons = [
    InlineKeyboardButton(text="🖼 Add your art", callback_data="add_art"),
    InlineKeyboardButton(text="🎨 View Gallery", callback_data="view_gallery")
]
