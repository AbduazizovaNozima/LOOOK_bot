
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
import logging
from aiogram import types
import sys
# from integration import mak..
from random import randrange
from aiogram.types.input_file import FSInputFile

number = 0

TOKEN = '7864725145:AAGd1cYg9nhD2ANqJZosvY2HYRIWXSjM9kM'
bot = Bot(token=TOKEN)
dp = Dispatcher()

def get_keyboards(number_button):
    
    kb = [
        [types.KeyboardButton(text='1', request_contact=True), types.KeyboardButton(text='2', request_location=True) ]
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

def get_inline_keyboards():
    kb = [
        [types.InlineKeyboardButton(text='random1-10', callback_data='generate_number')],
        [types.InlineKeyboardButton(text='google', url = 'https://google.com')]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=kb)

def decrease_insrease_keyboard():
    kb = [
        [types.InlineKeyboardButton(text='-1', callback_data='decrease'),types.InlineKeyboardButton(text='+1', callback_data='insrease') ],
        [types.InlineKeyboardButton(text='Tasdiqlash', callback_data= 'finish')]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=kb)
# @dp.message(CommandStart())
# async def start_button(message: Message):
#     user_data = f'ID:{message.from_user.id}, \nFirst name: {message.from_user.first_name}'
#     print(user_data)
#     await bot.send_message(chat_id=6387861882, text = user_data)
#     await message.reply(text =f'Assalomu alaykum', reply_markup=get_keyboards(number_button=3))

# @dp.message(CommandStart())
# async def start_button(message: Message):
#     await message.reply(text = 'Son: {number}', reply_markup=decrease_insrease_keyboard())

# @dp.message(CommandStart())
# async def start_button(message: Message):
#     await bot.send_location(
#         chat_id=message.chat.id,
#         latitude=41.29218825388536, 
#         longitude=69.22337589815257
#     )
    # await bot.send_photo(chat_id=message.chat.id,
    #                      photo = 'https://cdn.pixabay.com/photo/2024/02/28/07/42/european-shorthair-8601492_640.jpg')

    # image = FSInputFile('image.png')
    # await bot.send_photo(chat_id=message.chat.id,
    #                      photo=image)
    
    await bot.send_sticker(chat_id=message.chat.id, sticker = 'CAACAgIAAxkBAAENdo5nfhMedWFjazYcM-MAAW4jDhgYx9AAAr8XAAKOtaFKwAOwg6Uk-c42BA')

@dp.message(F.text.lower() == '/random')
async def generate_random(message: Message):
    await message.answer(text='1dan 10gacha son generatsiya qilish uchun pastdagi tugmani bosing', reply_markup=get_inline_keyboards())


@dp.callback_query(F.data == 'generate_number')
async def generate(callback: types.CallbackQuery):
    son = randrange(1,11)
    await callback.answer(text=str(son))

@dp.callback_query()
async def decrease_insrease(callback:types.CallbackQuery):
    global number
    if callback.data == 'decrease':
        number -= 1
        await callback.message.edit_text(text=f'son: {number}', reply_markup=decrease_insrease_keyboard)
    elif callback.data == 'insrease':
        number += 1
        await callback.message.edit_text(text=f'son: {number}', reply_markup=decrease_insrease_keyboard)
    elif callback.data == 'finish':
        await bot.send.message(
            chat_id= callback.message.chat.id,
            text=f'Natija: {number}')





# @dp.message()
# async def gemeni_speak(message: Message):
#     text = message.text
    # raqam_count = 0
    # harf_count = 0
    # for matn in text:
    #     if matn.isdigit():  
    #         raqam_count += 1
    #     elif matn.isalpha():  
    #         harf_count += 1
    # print(raqam_count, harf_count)
    # response = make_conversation(text = text)
    # await message.answer(text=response)
 

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())






