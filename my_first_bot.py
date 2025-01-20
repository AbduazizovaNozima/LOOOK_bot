
# import asyncio
# from aiogram import Bot, Dispatcher, F
# from aiogram.filters import CommandStart
# from aiogram.types import Message
# import logging
# from aiogram import types
# import sys


# logging.basicConfig(level=logging.INFO)

# TOKEN = '7864725145:AAGd1cYg9nhD2ANqJZosvY2HYRIWXSjM9kM'  
# bot = Bot(token=TOKEN)
# dp = Dispatcher()

# def buttons():
#     kb = [
#         [types.KeyboardButton(text = "Yordam")],
#         [types.KeyboardButton(text = "So'rov yuborish")]
#     ]
#     return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

# def buttons():
#     kb = [
#         [types.KeyboardButton(text = "Yordam")],
#         [types.KeyboardButton(text="Lokatsiya yuborish", request_location=True)],  
#         [types.KeyboardButton(text="Rasm yuborish")],
        
#     ]
#     return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

# def new_buttons():
#     kb = [
#         [types.KeyboardButton(text = "So'rov yuborish")],
#     ]
#     return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)


# @dp.message(CommandStart())  
# async def cmd_start(message: types.Message):
#     await message.reply("Salom! Botga xush kelibsiz!", reply_markup=buttons())


from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
import asyncio

TOKEN = '7864725145:AAGd1cYg9nhD2ANqJZosvY2HYRIWXSjM9kM'  
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Holatlar
class Registration(StatesGroup):
    ism = State()
    yosh = State()
    tel_raqam = State()

@dp.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer("Salom! Ismingizni kiriting: ")
    await state.set_state(Registration.ism)  # "ism" holatiga o'tamiz

@dp.message(Registration.ism)
async def get_ism(message: Message, state: FSMContext):
    await state.update_data(ism=message.text)  # Ismni saqlash
    await message.answer("Yoshingizni kiriting: ")
    await state.set_state(Registration.yosh)

@dp.message(Registration.yosh)
async def get_yosh(message: Message, state: FSMContext):
    await state.update_data(yosh=message.text)  # Yoshni saqlash
    await message.answer("Telefon raqamingizni kiriting: ")
    await state.set_state(Registration.tel_raqam)

@dp.message(Registration.tel_raqam)
async def get_tel_raqam(message: Message, state: FSMContext):
    await state.update_data(tel_raqam=message.text)  # Telefon raqamini saqlash
    user_data = await state.get_data()  # Foydalanuvchidan olingan barcha ma'lumotlarni olish
    await message.answer(f"Ro'yxatni to'ldirdingiz! \nIsmingiz: {user_data['ism']} \nYoshingiz: {user_data['yosh']} \nTelefon: {user_data['tel_raqam']}")
    await state.clear()  # Holatni tozalash

# Boshlash uchun polling
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())



# @dp.message(F.text == "Yordam")
# async def send_help(message: types.Message):
#     await message.answer("Bu bot orqali siz turli xizmatlardan foydalanishingiz mumkin!")

# @dp.message(F.text == "Yordam")
# async def send_help(message: types.Message):
#     await message.answer("Bu bot orqali siz turli xizmatlardan foydalanishingiz mumkin!", reply_markup=new_buttons())

# @dp.message(F.text == "Lokatsiya yuborish")
# async def send_location(message: types.Message):
#     latitude = 41.28139708691327 
#     longitude = 69.20476732562491  

#     await bot.send_location(message.chat.id, latitude=latitude, longitude=longitude)


# @dp.message(F.text == "So'rov yuborish")
# async def send_request(message: types.Message):
#     await message.answer("So'rov yuborildi! Biz tez orada sizga javob beramiz.")
    
# async def main():
#     await dp.start_polling(bot)

# if __name__ == '__main__':
#     asyncio.run(main())























