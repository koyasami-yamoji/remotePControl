from  pydantic import BaseModel, SecretStr
from pydantic_settings import BaseSettings as _BaseSettings
from pydantic_settings import SettingsConfigDict


class BaseSettings(_BaseSettings):
	model_config = SettingsConfigDict(extra='ignore', env_file='.env', env_file_encoding='utf-8')


class Tg(BaseSettings, env_prefix="TG_"):
	token: str = SecretStr
	owner: int
	use_redis: bool = True


class Api(BaseSettings, env_prefix="API_"):
	currency: str = SecretStr
	weather: str = SecretStr
	crypto: str = SecretStr
	latitude: float
	longitude: float


class AppConfig(BaseModel):
	tg: Tg
	api: Api


def load_config() -> AppConfig:
	return AppConfig(
		tg=Tg(),
		api=Api()
	)
