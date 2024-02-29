import logging
from typing import Callable, Dict, Awaitable, Any

from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import User, Update, TelegramObject


logger = logging.getLogger(__name__)


class FilterUserMiddleware(BaseMiddleware):
	def __init__(self, user_id: int) -> None:
		self.user_id = user_id

	async def __call__(self,
					   handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
					   event: Update,
					   data: Dict[str, Any]
					   ) -> Any:
		user: User = data['event_from_user']
		if user.id != self.user_id:
			logger.info('skip')
			return
		return await handler(event, data)
