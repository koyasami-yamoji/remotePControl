import aiohttp

from config_data.config import AppConfig


async def fetch_weather_info(config: AppConfig):
	async with aiohttp.ClientSession() as session:
		url = _build_weather_url(config)
		async with session.get(url) as response:
			data = await response.json()
			return _build_weather_text(data)


def _build_weather_url(config: AppConfig):
	return (
		f'https://api.openweathermap.org/data/2.5/weather'
		f'?lat={config.api.latitude}'
		f'&lon={config.api.longitude}'
		f'&appid={config.api.weather}'
		f'&lang=ru'
		f'&units=metric'
	)


def _build_weather_text(data):
	return (
		f"\n☁ Погода в <b>{data['name']}</b>\n"
		f"🌡 Температура - <b>{data['main']['temp']}</b>º - {data['weather'][0]['description']}\n"
		f"🍤 Ощущается как - <b>{data['main']['feels_like']}</b>\n"
		f"💧 Влажность - <b>{data['main']['humidity']}%</b>\n"
	)
