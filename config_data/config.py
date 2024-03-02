import os
from dataclasses import dataclass

from dotenv import load_dotenv, find_dotenv


@dataclass
class Tg:
	token: str
	owner: int
	use_redis: bool


@dataclass
class Config:
	tg: Tg


def load_config():
	if not find_dotenv():
		exit('Переменные окружения не найдены')

	load_dotenv()
	config = Config(
		tg=Tg(token=os.getenv('TOKEN'),
			  owner=int(os.getenv('OWNER')),
			  use_redis=True if (os.getenv('USE_REDIS') == "TRUE") else False)
	)

	return config
