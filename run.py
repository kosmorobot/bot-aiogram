from aiogram import types, executor, Dispatcher, Bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import requests
from datetime import datetime




TOKEN = "1854908281:AAFDQoSyv7JSWcR7FvVYCfQ6X-zFy_YoBrU"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def begin (message: types.Message):
    markup = InlineKeyboardMarkup()
    but_1 = InlineKeyboardButton("Как дила?", callback_data="but_1")
    markup.add(but_1)
    await bot.send_message(message.chat.id, "Привет, Лоло Лоло!", reply_markup=markup)




@dp.callback_query_handler(lambda c: c.data == "but_1")
async def button_reaction(call: types.callback_query):

    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, "Дела мои хорошуганские!")


@dp.message_handler(content_types=['text'])
async def text (message: types.Message):
    if message.text.lower() == 'пока':
        await bot.send_message(message.chat.id, 'пакеда!')
        #await message.reply('Пакеда!') #отвечает ! на сообщение !







executor.start_polling(dp)


