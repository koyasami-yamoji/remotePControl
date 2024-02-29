from aiogram import Router

from .default.default import router, start_dialog


def setup_start_routers():
	setup_router = Router()
	setup_router.include_router(router)
	setup_router.include_router(start_dialog)

	return setup_router