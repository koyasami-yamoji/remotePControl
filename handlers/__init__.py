from aiogram import Router

from .default.start import router


def setup_start_routers():
	setup_router = Router()
	setup_router.include_router(router)
	return setup_router