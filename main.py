import asyncio
import logging

import betterlogging as bl
from aiogram import Bot, Dispatcher, F, Router
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from aiogram_dialog import setup_dialogs

from handlers import setup_start_routers
from config_data.config import load_config
from middleware import FilterUserMiddleware
from dialog import include_dialogs


router = Router()


def setup_logging():

    log_level = logging.INFO
    bl.basic_colorized_config(level=log_level)

    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
    )
    logger = logging.getLogger(__name__)
    logger.info("Starting bot")


async def main():
    setup_logging()
    config = load_config()
    bot = Bot(token=config.tg.token)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(setup_start_routers(), include_dialogs())
    setup_dialogs(dp)
    dp.update.outer_middleware(FilterUserMiddleware(config.tg.owner))
    # dp.message.filter(F.from_user.id == 1835906223)
    # dp.update.filter(MagicData(F.event_from_user.id == 1835906223))

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.error("bot stopped")
