import os
from dataclasses import dataclass

from dotenv import load_dotenv, find_dotenv


@dataclass
class Tg:
	token: str
	owner: int


@dataclass
class Config:
	tg: Tg


def load_config():
	if not find_dotenv():
		exit('Переменные окружения не найдены')

	load_dotenv()
	config = Config(
		tg=Tg(os.getenv('TOKEN'),
			  int(os.getenv('OWNER')))
	)

	return config
