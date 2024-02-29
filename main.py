import asyncio
import logging

from aiogram import Bot, Dispatcher, F, Router
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message
from aiogram_dialog import setup_dialogs

from handlers import setup_start_routers
from config_data.config import load_config
from middleware import FilterUserMiddleware


logger = logging.getLogger(__name__)

router = Router()


async def main():
	config = load_config()
	bot = Bot(token=config.tg.token)
	dp = Dispatcher(storage=MemoryStorage())
	dp.include_router(router)
	dp.include_router(setup_start_routers())
	setup_dialogs(dp)
	dp.update.outer_middleware(FilterUserMiddleware(config.tg.owner))
	# dp.message.filter(F.from_user.id == 1835906223)
	# dp.update.filter(MagicData(F.event_from_user.id == 1835906223))

	await bot.delete_webhook(drop_pending_updates=True)
	await dp.start_polling(bot)


@router.message()
async def echo(message: Message):
	print(message.from_user.id)
	await message.answer('123')


if __name__ == "__main__":

	logging.basicConfig(
		level=logging.INFO,
		format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
	)

	try:
		logger.info('Starting bot...')
		asyncio.run(main())
	except KeyboardInterrupt:
		logger.info("Bot stopped")
