#!/usr/bin/env python3
from aiogram import Bot, Dispatcher, executor, types  # pipenv install aiogram
from config import TOKEN
import open_meta


bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await message.answer('Developer is: @m1ck1e\n' +
                         '\nUSAGE:\n' +
                         'Just send a message with city name.\n' +
                         'For example: Irpin')


@dp.message_handler()
async def temperature(message: types.Message):
    answer = open_meta.main(message.text)
    if answer == '[-] An error happenned':
        await message.answer(answer)
    else:
        stri = ''
        for key, value in answer:
            stri += f'{key}: {value}\n'
        print('[+] Success, send results to request with city:' +
              f'{message.text}')
        await message.answer(stri)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
