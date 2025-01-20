

import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import logging
from aiogram import types
import sys

class OrderState(StatesGroup):
    chicky_burger_count = State()
    beef_longer_count = State()

logging.basicConfig(level=logging.INFO)

number = {}

TOKEN = '8110107223:AAHgquZQFY4AvOaO65xdh5U1Ka-bt5CitAM'  
bot = Bot(token=TOKEN)
dp = Dispatcher()

def buttons1():
    kb = [
        [types.KeyboardButton(text = " 🛍Buyurtma berish")],
        [types.KeyboardButton(text = "⚙️Sozlamalar")],[types.KeyboardButton(text = "ℹ️Biz haqimizda")],
        [types.KeyboardButton(text = "📋Mening buyurtmalarim")],[types.KeyboardButton(text = "✍️Izoh qoldirish")]
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

def button_buyurtma():
    kb = [
        [types.KeyboardButton(text = "Olib ketish")],[types.KeyboardButton(text = "Yetkazib berish")],
        [types.KeyboardButton(text = "⬅️Orqaga")]
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

def button_olibketish():
    kb = [
        [types.KeyboardButton(text = "📍Yunusobod")],[types.KeyboardButton(text = "📍Maksim Gorkiy")],
        [types.KeyboardButton(text = "📍Chilonzor")],[types.KeyboardButton(text = "📍Boulevard")],
        [types.KeyboardButton(text = "📍Beruniy")],[types.KeyboardButton(text = "⬅️Orqaga")]
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

def button_yetkazibberish():
    kb = [
        [types.KeyboardButton(text = "📍Lokatsiya yuborish", request_location=True)],
        [types.KeyboardButton(text = "Orqaga")]
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

def button_lokatsiya():
    kb = [
        [types.KeyboardButton(text = "📍Lokatsiya yuborish", request_location=True)],
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

def button_lokatsiya2():
    kb = [
        [types.KeyboardButton(text = "📍Lokatsiyani qayta yuborish")],[types.KeyboardButton(text = "Mening manzillarimga qo'shish")],
        [types.KeyboardButton(text = "Tasdiqlash")],[types.KeyboardButton(text = "⬅️Orqaga")]
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

def button_tasdiqlash():
    kb = [
        [types.KeyboardButton(text = "Tasdiqlash")],
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

def button_menu():
    kb = [
        [types.KeyboardButton(text = "🍔Burgerlar")],
        [types.KeyboardButton(text = "Sous")],
        [types.KeyboardButton(text = "Ichimliklar")],
        [types.KeyboardButton(text = "Savat")],
        [types.KeyboardButton(text = "⬅️Orqaga")]
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)


def button_burgerlar():
    kb = [
        [types.KeyboardButton(text = "🍔Chicky Burger")],
        [types.KeyboardButton(text = "🍔Beef Longer")],
        [types.KeyboardButton(text = "⬅️Orqaga")]

    ]
    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

def button_plus_minus():
    kb = [
        [types.InlineKeyboardButton(text='-1', callback_data='ayirish'),types.InlineKeyboardButton(text='+1', callback_data="qo'shish") ],
        [types.InlineKeyboardButton(text='Tasdiqlash', callback_data= 'finish')]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=kb)

def button_chickyburger():
    kb = [
        [types.KeyboardButton(text = "📥Savat")],
        [types.KeyboardButton(text = "⬅️Orqaga")],
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

def button_beeflonger():
    kb = [
        [types.KeyboardButton(text = "📥Savat")],
        [types.KeyboardButton(text = "⬅️Orqaga")],
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)



def button_sozlamalar():
    kb = [
        [types.KeyboardButton(text = "Telefon raqam kiritish")],
        [types.KeyboardButton(text = "⬅️Orqaga")]
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

def button_telraqam():
    kb = [
        [types.KeyboardButton(text = "Telefon raqam kiritish", request_contact=True)],
        [types.KeyboardButton(text = "⬅️Orqaga")]
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)



def button_bizhaqimizda():
    kb = [
        [types.KeyboardButton(text = "⬅️Orqaga")]
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

def button_meningbuyurtmalarim():
    kb = [
        [types.KeyboardButton(text = "⬅️Orqaga")]
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

def button_izoh():
    kb = [
        [types.KeyboardButton(text = "⬅️Orqaga")]
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)



@dp.message(CommandStart())  
async def cmd_start(message: types.Message):
    await message.reply("Buyurtma berishni boshlash uchun 🛍 Buyurtma berish tugmasini bosing.\nShuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin", reply_markup=buttons1())

@dp.message(F.text == "🛍Buyurtma berish")
async def send_buyurtma(message: types.Message):
    await message.answer("Yetkazib berish turini tanlang", reply_markup=button_buyurtma())

@dp.message(F.text == "Olib ketish")
async def send_olibketish(message: types.Message):
    await message.answer("Filialni tanlang", reply_markup=button_olibketish())

@dp.message(F.text.in_(["📍Yunusobod", "📍Maksim Gorkiy", "📍Chilonzor", "📍Boulevard", "📍Beruniy"]))
async def send_olibketish(message: types.Message):
    await message.answer("Tasdiqlashni bosing", reply_markup=button_tasdiqlash())


@dp.message(F.text == "Yetkazib berish")
async def send_yetkazibberish(message: types.Message):
    await message.answer("Buyurtmani davom ettirish uchun iltimos lokatsiyangizni yuboring ", reply_markup=button_yetkazibberish())

@dp.message(F.location)
async def send_lokatsiya(message: types.Message):
        latitude = message.location.latitude
        longitude = message.location.longitude
        await message.answer(f"Sizning lokatsiyangiz: \nLatitude: {latitude}\nLongitude: {longitude}\nManzilni tasdiqlaysizmi?", reply_markup=button_lokatsiya2())

@dp.message(F.text == "Lokatsiyani qayta yuborish")
async def send_qaytayuborish(message: types.Message):
    await message.answer("Iltimos, lokatsiyangizni qayta yuboring.",reply_markup=button_yetkazibberish())

@dp.message(F.text == "Mening manzillarimga qo'shish")
async def send_manzilqoshish(message: types.Message):
    await message.answer("Manzil qo'shildi")

@dp.message(F.text == "Tasdiqlash")
async def send_tasdiqlash(message: types.Message):
    await message.answer("Tasdiqlandi\nKategoriyani tanlang", reply_markup=button_menu())

@dp.message(F.text == "⬅️Orqaga")
async def send_back(message: types.Message):
    await message.answer("Asosiy menyuga qaytdingiz.", reply_markup=buttons1())


@dp.message(F.text == "🍔Burgerlar")
async def send_aksiya(message: types.Message):
    await message.answer("Burgerlar \n\nMahsulotni tanlang:", reply_markup=button_burgerlar())

@dp.message(F.text == "🍔Chicky Burger")
async def send_chickyburger(message: types.Message):
    keyboard = button_plus_minus()

    await message.answer_photo("https://assets.epicurious.com/photos/5c745a108918ee7ab68daf79/1:1/w_960,c_limit/Smashburger-recipe-120219.jpg", 
                               caption="🍔Chicky Burger \nNon, Mayonez, Aysberg, Pishloq, Kotlet (Tovuq)\n\nChicky Burger 60 000 x 1 = 60 000 \nUmumiy: 60 000 UZS",reply_markup=keyboard
)

@dp.message(F.text == "🍔Beef Longer")
async def send_beeflonger(message: types.Message):
    keyboard = button_plus_minus()

    await message.answer_photo("https://www.tasteofhome.com/wp-content/uploads/2017/09/exps28800_UG143377D12_18_1b_RMS.jpg", 
                               caption="🍔Beef Longer\nNon (Longer), Mayonez, Salsa Sous, Piyoz, Sho'rbodring \n(Manirovanniy), Pomidor, Aysberg, Kotlet (Mol Go'sht)\n\nBeef longer 30 000 x 1 = 30 000\nUmumiy: 30 000 UZS",reply_markup=keyboard
)

@dp.callback_query()
async def handle_callback(callback: types.CallbackQuery, state: FSMContext):
    global number
    # Chicky Burger
    if callback.data == 'ayirish' and "🍔Chicky Burger" in number and ["🍔Chicky Burger"] > 0:
        number["🍔Chicky Burger"] -= 1
        await callback.answer("🍔Chicky Burgerdan 1ta olib tashlandi!")
    elif callback.data == 'qo\'shish':
        if "🍔Chicky Burger" in number:
            number["🍔Chicky Burger"] += 1
        else:
            number["🍔Chicky Burger"] = 1
        await callback.answer("Chicky Burger savatga qo'shildi!")

    # Beef Longer
    elif callback.data == 'ayirish' and "🍔Beef Longer" in number and number["🍔Beef Longer"] > 0:
        number["🍔Beef Longer"] -= 1
        await callback.answer("🍔Beef Longerdan 1 ta olib tashlandi!")
    elif callback.data == 'qo\'shish':
        if "🍔Beef Longer" in number:
            number["🍔Beef Longer"] += 1
        else:
            number["🍔Beef Longer"] = 1
        await callback.answer("🍔Beef Longer savatga qo'shildi!")

    number_text = "📥Savat:\n"
    for item, quantity in number.items():
        number_text += f"{item}: {quantity}\n"

        await callback.message.answer(number_text, reply_markup=button_plus_minus())



@dp.message(F.text == "⚙️Sozlamalar")
async def send_sozlamalar(message: types.Message):
    await message.answer("Sozlamani tanlang", reply_markup=button_sozlamalar())

@dp.message(F.text == "Telefon raqam kiritish")
async def send_telraqam(message: types.Message):
    if message.contact:
        contact = message.contact
        phone_number = contact.phone_number
        await message.answer(f"Sizning telefon raqamingiz: {phone_number}\nYangi telefon raqam kiriting \n\nRaqamni +998********* shaklida yuboring.", reply_markup=button_telraqam())
    else:
        await message.answer("Iltimos, telefon raqamingizni yuboring.", reply_markup=button_telraqam())

@dp.message(F.text == "ℹ️Biz haqimizda")
async def send_biz(message: types.Message):
    await message.answer("LOOOK", reply_markup=button_bizhaqimizda())

@dp.message(F.text == "📋Mening buyurtmalarim")
async def send_biz(message: types.Message):
    await message.answer("Sizda buyurtmalar yo'q", reply_markup=button_meningbuyurtmalarim())

@dp.message(F.text == "✍️Izoh qoldirish")
async def send_izoh(message: types.Message):
    await message.answer("Izoh qoldiring. Sizning fikringiz biz uchun muhim", reply_markup=button_izoh())



async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())









