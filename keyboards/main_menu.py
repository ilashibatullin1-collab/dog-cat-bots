from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def get_reply_keyboard():
    kb = [
        [KeyboardButton(text="🐱 Кошечка")],
        [KeyboardButton(text="👗 Мой гардероб")],
        [KeyboardButton(text="🏆 Рейтинг и Бонусы")]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

def get_inline_keyboard():
    kb = [
        [InlineKeyboardButton(text="🐱 Кошечка", callback_data="cat")],
        [InlineKeyboardButton(text="👗 Мой гардероб", callback_data="inventory")],
        [InlineKeyboardButton(text="🏆 Рейтинг и Бонусы", callback_data="rating")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)

