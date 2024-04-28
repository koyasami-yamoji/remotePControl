from aiogram_dialog import DialogManager

from config_data.config import AppConfig
from services.api.get_currency import get_currency_course
from services.api.get_weather import get_weather_info


async def getter_currency(config: AppConfig, **_):
	usd_to_rub_text = await get_currency_course(config=config)
	weather_text = await get_weather_info(config=config)

	return {
		"currency": usd_to_rub_text,
		"weather_text": weather_text
	}