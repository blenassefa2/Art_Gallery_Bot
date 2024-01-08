
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

add_or_view_art_buttons= InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="🖼 Add your art", callback_data="add_art"),
        ],
        [
            InlineKeyboardButton(text="🎨 View Gallery", callback_data="view_gallery")
        ]
    ]
)

art_filtering_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👩‍🎨 Filter by Artist"),
            KeyboardButton(text="📓 Filter by Tag"),
            KeyboardButton(text="🔃 Random")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="dtrial",
    selective=True
)

create_art_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🖌 Let's gooo!!")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="dtrial",
    selective=True
)
