import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineQuery
from spotify import generate_text, generate_inline


LOG_LEVEL = getenv("LOG_LEVEL")
if LOG_LEVEL is None:
    LOG_LEVEL = "INFO"

logging.basicConfig(level=logging.getLevelNamesMapping().get(LOG_LEVEL))

BOT_TOKEN = getenv("BOT_TOKEN")
if BOT_TOKEN is None:
    raise ValueError("BOT_TOKEN is not set")

dp = Dispatcher()
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


@dp.message(CommandStart())
async def command_start_handler(message: Message, bot: Bot) -> None:
    bot_self = await bot.get_me()
    await message.answer(
        f"🔗 Send me a Spotify link to share it with preview! Or use inline mode: type into message box @{bot_self.username} and spotify link"
    )


@dp.message()
async def message_handler(message: Message) -> None:
    query = message.text
    if not query:
        return
    await message.answer(generate_text(query))


@dp.inline_query()
async def inline_query_handler(inline_query: InlineQuery) -> None:
    query = inline_query.query
    if not query:
        return
    await inline_query.answer(results=generate_inline(query))


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
