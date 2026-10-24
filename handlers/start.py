from aiogram import Router, F
from aiogram.types import Message
from keyboards.main_menu import get_reply_keyboard

router = Router()

@router.message(F.command == "start")
async def cmd_start(message: Message):
    await message.answer(
        "Добро пожаловать в PetShop Stars!\n"
        "Выбери, что хочешь сделать:",
        reply_markup=get_reply_keyboard()
    )
