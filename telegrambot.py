from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, BufferedInputFile
from visualization import make_diagram
from data_request import get_data_from_api
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import asyncio
import io
import logging
import os
import sys

# initialization
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

# Handler of the command "/start"
@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(f"Hello, {message.from_user.full_name}! I am a bot on aiogram 3.x")

# Handler of the command "/help"
@dp.message(Command("help"))
async def command_help_handler(message: Message):
    await message.answer("This is the help menu. Write something to me!")

# Handler of the command "/show"
@dp.message(Command("show"))
async def command_show_handler(message: Message):
    fig = make_diagram(get_data_from_api())
    buf = io.BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    file = BufferedInputFile(buf.getvalue(), filename="storm_chart.png")
    await message.answer_photo(photo=file, caption="Your K-index forecast")
    plt.close(fig)
    buf.close()

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")