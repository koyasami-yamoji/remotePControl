from typing import Callable, Dict, Awaitable, Any

from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import Update, TelegramObject
from pynput.keyboard import Controller


class KeyboardControllerMiddleware(BaseMiddleware):
	def __init__(self, controller: Controller):
		self.controller = controller

	async def __call__(self,
					   handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
					   event: Update,
					   data: Dict[str, Any]):

		data['controller'] = self.controller
		return await handler(event, data)