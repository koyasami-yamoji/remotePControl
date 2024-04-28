import aiohttp

from config_data.config import AppConfig


async def get_currency_course(config: AppConfig):
	async with aiohttp.ClientSession() as session:
		async with session.get(f'https://v6.exchangerate-api.com/v6/{config.api.currency}/latest/USD') as response:
			data = await response.json()
			usd_to_rub = data["conversion_rates"]["RUB"]
		url = f"https://api.cryptorank.io/v1/currencies/1?api_key={config.api.crypto}"
		async with session.get(url=url) as response:
			data = await response.json()
			bitcoin_price = data['data']['values']['USD']['price']

	return (f"<b>Курс валют:</b>\n\n<b>"
			f"🎓 Доллар: {round(usd_to_rub, 2)} <i>rub</i></b>\n"
			f"💻 Bitcoin: <b>{round(bitcoin_price, 2)}💲</b>\n")
