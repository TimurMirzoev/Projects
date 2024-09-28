from aiogram import Bot, Dispatcher, executor, types

import python_weather
import asyncio

bot = Bot(token="7898385167:AAGy2-ho6sYQYTPheZo20fxeDY9haoH7THY")

client = python_weather.Client(format=python_weather.IMPERIAL)

dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):

    weather = await client.find(message.text)

    celcius = round((weather.current.temperature - 32) / 1.8)

    resp_msg = weather.location_name + "\n"
    resp_msg += f"Current temperature: {celcius}°\n"
    resp_msg += f"Weather condition: {weather.current.sky_text}"

    await message.answer(resp_msg)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

